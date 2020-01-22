import os
import sqlite3
from datetime import datetime

from service.config.service_config import ServiceConfig
from service.db.db_base import DBBase


class SQLiteDB(DBBase):
    def __init__(self, config: ServiceConfig):
        super().__init__(config)

    def get_source(self):
        return "SQLite"

    def get_db_path(self):
        return self.config.db["path"]

    def migrate(self):
        path = self.get_db_path()

        os.makedirs(os.path.dirname(path), exist_ok=True)

        conn = sqlite3.connect(path)
        conn.execute("DROP TABLE IF EXISTS messages")
        conn.execute("CREATE TABLE IF NOT EXISTS messages "
                     "(web_service_source text, channel_name text, content text, timestamp datetime)")
        conn.commit()
        conn.close()

        print("Migration completed for SQLite DB '%s'." % path)

    def count_chat_messages_as_of(self, web_service_source, channel_name, timestamp: datetime):
        path = self.get_db_path()

        conn = sqlite3.connect(path)
        result = conn.execute(
            "SELECT * FROM messages WHERE web_service_source = '%s' AND channel_name = '%s' AND timestamp >= '%s'" % (
                web_service_source, channel_name, timestamp))
        count = len(result.fetchall())
        conn.commit()
        conn.close()

        return count

    def store_chat_messages(self, web_service_source, channel_name, chat_messages):
        path = self.get_db_path()

        conn = sqlite3.connect(path)

        for message in chat_messages:
            conn.execute("INSERT INTO messages VALUES ('%s', '%s', '%s', '%s');\n" % (
                web_service_source, message.channel_name, message.content, message.timestamp))

        conn.commit()
        conn.close()

        print("Inserted %s chat message(s) into SQLite DB '%s'." % (len(chat_messages), path))

    def read_chat_messages(self, web_service_source, channel_name, max_count=10):
        pass
