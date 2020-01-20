from unittest import TestCase
from unittest.mock import Mock, MagicMock

import requests
from requests import Response

from service.config.service_config import ServiceConfig
from service.models.channel import Channel
from service.models.game import Game
from service.models.stream import Stream
from service.services.twitch_web_service import TwitchWebService
from service.services.web_service_base import WebServiceBase


def build_test_stream():
    stream: Stream = Stream()
    stream.id = "12345"
    stream.title = "TestTitle"
    stream.game = build_test_game()
    stream.start_time = "2020-01-16 10:09:08"
    stream.viewer_count = 10

    return stream


def build_test_channel():
    channel: Channel = Channel()
    channel.id = "12345"
    channel.name = "TestChannel"
    channel.web_service_source = "Twitch"

    return channel


def build_test_game():
    game: Game = Game()
    game.id = "12345"
    game.name = "TestGame"

    return game


class TestTwitchWebService(TestCase):
    def setUp(self) -> None:
        self.requests: requests = Mock()
        self.config = ServiceConfig()

    def test_get_source(self):
        service: WebServiceBase = TwitchWebService(self.requests, self.config)

        self.assertIsNotNone(service.get_source())

    def test_get_channel(self):
        expected_channel = build_test_channel()

        response = Response()
        response.status_code = 200
        body = {
            "data": [
                {
                    "id": expected_channel.id,
                    "login": expected_channel.name
                }
            ]
        }

        response.json = MagicMock(return_value=body)
        self.requests.get = MagicMock(return_value=response)

        service: WebServiceBase = TwitchWebService(self.requests, self.config)

        actual_channel: Channel = service.get_channel(expected_channel.name)

        self.assertEqual(expected_channel.to_json(), actual_channel.to_json())

    def test_get_stream(self):
        expected_stream = build_test_stream()

        response = Response()
        response.status_code = 200
        body = {
            "data": [
                {
                    "id": expected_stream.id,
                    "title": expected_stream.title,
                    "game_id": expected_stream.game.id,
                    "started_at": expected_stream.start_time,
                    "viewer_count": expected_stream.viewer_count
                }
            ]
        }

        response.json = MagicMock(return_value=body)
        self.requests.get = MagicMock(return_value=response)

        service: WebServiceBase = TwitchWebService(self.requests, self.config)

        service.get_game = MagicMock(return_value=expected_stream.game)

        actual_stream: Stream = service.get_stream("Test")

        self.assertEqual(expected_stream.to_json(), actual_stream.to_json())

    def test_get_game(self):
        expected_game = build_test_game()

        response = Response()
        response.status_code = 200
        body = {
            "data": [
                {
                    "id": expected_game.id,
                    "name": expected_game.name,
                }
            ]
        }

        response.json = MagicMock(return_value=body)
        self.requests.get = MagicMock(return_value=response)

        service: WebServiceBase = TwitchWebService(self.requests, self.config)

        actual_stream: Stream = service.get_game(expected_game.id)

        self.assertEqual(expected_game.to_json(), actual_stream.to_json())
