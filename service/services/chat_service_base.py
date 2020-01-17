class ChatServiceBase(object):
    def start_collecting_chat(self, channel_name):
        raise NotImplementedError("Method implementation required.")

    def stop_collecting_chat(self, channel_name):
        raise NotImplementedError("Method implementation required.")