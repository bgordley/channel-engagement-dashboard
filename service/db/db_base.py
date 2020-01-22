from datetime import datetime

from service.config.service_config import ServiceConfig


class DBBase(object):
    def __init__(self, config: ServiceConfig):
        self.config = config

    def migrate(self):
        raise NotImplementedError("Method implementation required.")

    def get_source(self):
        raise NotImplementedError("Method implementation required.")

    def store_chat_messages(self, web_service_source, channel_name, chat_messages):
        raise NotImplementedError("Method implementation required.")

    def read_chat_messages(self, web_service_source, channel_name, max_count=10):
        raise NotImplementedError("Method implementation required.")

    def count_chat_messages_as_of(self, web_service_source, channel_name, timestamp: datetime):
        raise NotImplementedError("Method implementation required.")
