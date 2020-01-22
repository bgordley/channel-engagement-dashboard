from service.models.model_base import ModelBase


class ChatMessage(ModelBase):
    web_service_source: str
    channel_name: str
    content: str
    timestamp: str
