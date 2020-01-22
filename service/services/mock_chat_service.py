import sched
import threading
import time
from datetime import datetime

from service.db.db_base import DBBase
from service.models.chat_message import ChatMessage
from service.services.chat_service_base import ChatServiceBase


class MockChatService(ChatServiceBase):
    db: DBBase
    chat_workers: dict

    def __init__(self, source, db: DBBase):
        self.source = source
        self.db = db
        self.chat_workers = {}
        self.scheduler = sched.scheduler(time.time, time.sleep)
        self.interval = 5
        self.max_iterations = 60

    def get_source(self):
        return self.source

    def start_collecting_chat(self, channel_name):
        if channel_name in self.chat_workers:
            if self.chat_workers[channel_name].is_alive():
                return

        thread = threading.Thread(target=self.chat_collector_worker, args=(channel_name, 1))
        thread.setName("[%s_%s]" % (thread.getName(), channel_name))
        thread.start()

        self.chat_workers[channel_name] = thread

    def stop_collecting_chat(self, channel_name):
        pass

    def chat_collector_worker(self, channel_name, iteration):
        message = ChatMessage()
        message.channel_name = channel_name
        message.web_service_source = self.get_source()
        message.timestamp = datetime.utcnow()
        message.content = "Mock message"

        self.db.store_chat_messages(self.get_source(), channel_name, [message, message, message])

        thread = threading.current_thread().getName()
        print("%s: [%s/%s] Chat collected for channel '%s'." % (
            thread, iteration, self.max_iterations, channel_name))

        if iteration >= self.max_iterations:
            return

        print("%s: [%s/%s] Checking chat for channel '%s' in %s seconds." % (
            thread, iteration, self.max_iterations, channel_name, self.interval))

        self.scheduler.enter(self.interval, 1, self.chat_collector_worker, (channel_name, iteration + 1))
        self.scheduler.run()
