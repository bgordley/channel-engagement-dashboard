from service.models.model_base import ModelBase


class ChatMessage(ModelBase):
    content: str
    timestamp: str
