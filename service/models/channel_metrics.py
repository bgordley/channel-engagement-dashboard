from service.models.chat_mood import ChatMood
from service.models.model_base import ModelBase


class ChannelMetrics(ModelBase):
    mood: ChatMood
    msg_per_sec: int
    msg_per_min: int
