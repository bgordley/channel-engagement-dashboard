from datetime import datetime

from service.db.db_base import DBBase


class SQLiteDB(DBBase):
    def count_chat_messages_as_of(self, web_service_source, channel_id, timestamp: datetime):
        return 10

    def store_chat_messages(self, web_service_source, channel_id, chat_messages):
        pass

    def read_chat_messages(self, web_service_source, channel_id, max_count=10):
        pass
