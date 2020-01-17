import datetime

from service.db.db_base import DBBase
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


class ChannelProvider(object):
    def __init__(self, web_service: WebServiceBase, chat_service: ChatServiceBase, db: DBBase):
        self.web_service = web_service
        self.chat_service = chat_service
        self.db = db
        self.channel_cache = {}
        self.chat_cache = {}

    def get_channel(self, channel_name):
        channel = self.web_service.get_channel(channel_name)

        stream = self.web_service.get_stream(channel_name)
        channel.stream = stream
        channel.is_streaming = stream is not None

        channel.metrics = self.build_channel_metrics(channel_name)

        return channel

    def build_channel_metrics(self, channel_name):
        source = self.web_service.get_source()
        as_of_time: datetime = datetime.datetime.now() - datetime.timedelta(minutes=1)
        msg_per_min = self.db.count_chat_messages_as_of(channel_name, source, as_of_time)

        metrics: ChannelMetrics = ChannelMetrics()
        metrics.mood = get_chat_mood(msg_per_min)
        metrics.msg_per_min = msg_per_min
        metrics.msg_per_sec = (msg_per_min / 60).__round__(1)

        return metrics
