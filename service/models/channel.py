from service.models.channel_metrics import ChannelMetrics
from service.models.model_base import ModelBase
from service.models.stream import Stream


class Channel(ModelBase):
    web_service_source: str
    id: str
    name: str
    stream: Stream
    metrics: ChannelMetrics
    is_streaming: bool
    is_tracking: bool
