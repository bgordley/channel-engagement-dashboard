from service.models.chat_mood import ChatMood


class ChannelMetrics(object):
    def __init__(self):
        self.mood = ChatMood.calm
        self.msg_per_sec = 0
        self.msg_per_min = 0
