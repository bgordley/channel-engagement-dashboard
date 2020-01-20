from service.config.service_config import ServiceConfig
from service.errors.web_service_exception import WebServiceException
from service.models.channel import Channel
from service.models.game import Game
from service.models.stream import Stream
from service.services.web_service_base import WebServiceBase


class TwitchWebService(WebServiceBase):
    def __init__(self, requests, config: ServiceConfig):
        super().__init__(requests)
        self.config = config

    def get_client_id(self):
        return self.config.twitch["client_id"]

    def get_source(self):
        return "Twitch"

    def get_channel(self, channel_name):
        headers = {"Client-ID": self.get_client_id()}
        response = self.requests.get("https://api.twitch.tv/helix/users?login=%s" % channel_name, headers=headers)
        print("GET request sent - %s" % response.url)

        if not response.status_code == 200:
            raise WebServiceException(response.status_code, response.url)

        if len(response.json()["data"]) == 0:
            raise WebServiceException(404, response.url)

        data = response.json()["data"][0]

        channel: Channel = Channel()
        channel.id = data["id"]
        channel.name = data["login"]
        channel.web_service_source = self.get_source()

        return channel

    def get_stream(self, channel_name):
        headers = {"Client-ID": self.get_client_id()}
        response = self.requests.get("https://api.twitch.tv/helix/streams?user_login=%s" % channel_name,
                                     headers=headers)
        print("GET request sent - %s" % response.url)

        if not response.status_code == 200:
            raise WebServiceException(response.status_code, response.url)

        if len(response.json()["data"]) == 0:
            raise WebServiceException(404, response.url)

        data = response.json()["data"][0]

        stream: Stream = Stream()
        stream.id = data["id"]
        stream.title = data["title"]
        stream.game = self.get_game(data["game_id"])
        stream.start_time = data["started_at"]
        stream.viewer_count = data["viewer_count"]

        return stream

    def get_game(self, game_id):
        headers = {"Client-ID": self.get_client_id()}
        response = self.requests.get("https://api.twitch.tv/helix/games?id=%s" % game_id, headers=headers)
        print("GET request sent - %s" % response.url)

        if not response.status_code == 200:
            raise WebServiceException(response.status_code, response.url)

        if len(response.json()["data"]) == 0:
            raise WebServiceException(404, response.url)

        data = response.json()["data"][0]

        game: Game = Game()
        game.id = data["id"]
        game.name = data["name"]

        return game
