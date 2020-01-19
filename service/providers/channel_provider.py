import datetime

from service.db.db_base import DBBase
from service.errors.web_service_exception import WebServiceException
from service.models.channel import Channel
from service.models.channel_metrics import ChannelMetrics
from service.models.chat_mood import ChatMood
from service.services.chat_service_base import ChatServiceBase
from service.services.web_service_base import WebServiceBase


def get_chat_mood(msg_per_minute):
    if msg_per_minute <= 15:
        return ChatMood.calm
    elif msg_per_minute <= 30:
        return ChatMood.chatty
    elif msg_per_minute <= 60:
        return ChatMood.engaged
    elif msg_per_minute > 60:
        return ChatMood.hyped


def get_channel_key(source, channel_name):
    return "%s/%s" % (source.upper(), channel_name)


class ChannelProvider(object):
    web_services: dict
    chat_services: dict
    dbs: dict
    channel_cache: dict
    chat_cache: dict

    def __init__(self, web_service: WebServiceBase, chat_service: ChatServiceBase, db: DBBase):
        self.web_services = {}
        self.chat_services = {}
        self.dbs = {}
        self.channel_cache = {}
        self.chat_cache = {}

        self.register_web_service(web_service)
        self.register_chat_service(chat_service)
        self.register_db(db)

    def register_web_service(self, web_service: WebServiceBase):
        key = web_service.get_source().upper()
        self.web_services[key] = web_service

    def register_chat_service(self, chat_service: ChatServiceBase):
        key = chat_service.get_source().upper()
        self.chat_services[key] = chat_service

    def register_db(self, db: DBBase):
        key = db.get_source().upper()
        self.dbs[key] = db

    def get_web_service(self, source):
        key = source.upper()
        if key not in self.web_services:
            raise Exception("Web service '%s' has not been registered." % source)

        return self.web_services[key]

    def get_chat_service(self, source):
        key = source.upper()
        if key not in self.chat_services:
            raise Exception("Chat service '%s' has not been registered." % source)

        return self.chat_services[key]

    def get_db(self, source):
        key = source.upper()
        if key not in self.dbs:
            raise Exception("DB '%s' has not been registered." % source)

        return self.dbs[key]

    def get_channel(self, source, channel_name):
        key = get_channel_key(source, channel_name)
        web_service: WebServiceBase = self.get_web_service(source)

        channel: Channel

        if key in self.channel_cache:
            channel = self.channel_cache[key]
        else:
            channel = web_service.get_channel(channel_name)

        try:
            channel.stream = web_service.get_stream(channel_name)
        except WebServiceException:
            channel.is_streaming = False
        else:
            channel.is_streaming = True

        channel.metrics = self.build_channel_metrics(source, channel_name)

        self.channel_cache[key] = channel

        return channel

    def build_channel_metrics(self, source, channel_name):
        db = self.get_db("SQLite")

        source = source
        as_of_time: datetime = datetime.datetime.now() - datetime.timedelta(minutes=1)
        msg_per_min = db.count_chat_messages_as_of(channel_name, source, as_of_time)

        metrics: ChannelMetrics = ChannelMetrics()
        metrics.mood = get_chat_mood(msg_per_min)
        metrics.msg_per_min = msg_per_min
        metrics.msg_per_sec = (msg_per_min / 60).__round__(1)

        return metrics
