from service.models.channel import Channel
from service.models.stream import Stream
from service.services.web_service_base import WebServiceBase


class TwitchWebService(WebServiceBase):
    def get_source(self):
        return "Twitch"

    def get_auth_token(self):
        pass

    def get_channel(self, channel_name):
        channel: Channel = Channel()
        channel.id = "12345"
        channel.name = "Placeholder Channel"
        channel.web_service_source = self.get_source()

    def get_stream(self, channel_name):
        stream: Stream = Stream()
        stream.id = "12345"
        stream.title = "Placeholder stream title"
        stream.game = self.get_game(1)
        stream.start_time = "2020-01-16 10:09:08"
        stream.viewer_count = 123

        return stream

    def get_game(self, game_id):
        return "Placeholder game"
