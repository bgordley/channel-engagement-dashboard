import requests


class WebServiceBase(object):
    def __init__(self, _requests: requests):
        self.requests = _requests

    def get_channel(self, channel_name):
        raise NotImplementedError("Method implementation required.")

    def get_stream(self, channel_name):
        raise NotImplementedError("Method implementation required.")

    def get_game(self, game_id):
        raise NotImplementedError("Method implementation required.")

    def get_source(self):
        raise NotImplementedError("Method implementation required.")
