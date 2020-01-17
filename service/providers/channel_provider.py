import datetime
import math

from service.db.db_base import DBBase
from service.models.channel_metrics import ChannelMetrics
from service.services.chat_service_base import ChatServiceBase
from service.services.web_service_base import WebServiceBase


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
        as_of_time: datetime = datetime.datetime.now() - datetime.timedelta(minutes=1)
        msg_per_min = self.db.read_chat_messages_as_of(channel_name, self.web_service.get_source(), as_of_time)

        metrics: ChannelMetrics = ChannelMetrics()
        metrics.mood = self.get_chat_mood(msg_per_min)
        metrics.msg_per_min = msg_per_min
        metrics.msg_per_sec = (msg_per_min / 60).round()
        return metrics

    def get_chat_mood(self, msg_per_minute):
        if msg_per_minute <= 15:
            return "Calm"
        elif msg_per_minute <= 30:
            return "Chatty"
        elif msg_per_minute <= 60:
            return "Engaged"
        elif msg_per_minute > 60:
            return "Hyped"
