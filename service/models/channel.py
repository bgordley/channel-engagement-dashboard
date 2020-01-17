from service.models.channel_metrics import ChannelMetrics
from service.models.stream import Stream


class Channel(object):
    def __init__(self):
        self.web_service_source = ""
        self.id = ""
        self.name = ""
        self.stream: Stream = Stream()
        self.metrics: ChannelMetrics = ChannelMetrics()
        self.is_streaming = False
        self.is_tracking = False
