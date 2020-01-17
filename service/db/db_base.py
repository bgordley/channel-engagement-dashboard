from datetime import datetime


class DBBase(object):
    def store_chat_messages(self, web_service_source, channel_id, chat_messages):
        raise NotImplementedError("Method implementation required.")

    def read_chat_messages(self, web_service_source, channel_id, max_count=10):
        raise NotImplementedError("Method implementation required.")

    def read_chat_messages_as_of(self, web_service_source, channel_id, timestamp: datetime):
        raise NotImplementedError("Method implementation required.")
