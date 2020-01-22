from unittest import TestCase
from unittest.mock import MagicMock, Mock

from service.config.service_config import ServiceConfig
from service.db.db_base import DBBase
from service.models.channel import Channel
from service.models.channel_metrics import ChannelMetrics
from service.models.chat_mood import ChatMood
from service.models.stream import Stream
from service.providers.channel_provider import ChannelProvider
from service.services.chat_service_base import ChatServiceBase
from service.services.web_service_base import WebServiceBase


def build_test_stream():
    stream: Stream = Stream()
    stream.id = "12345"
    stream.title = "TestTitle"
    stream.game = "TestGame"
    stream.start_time = "2020-01-16 10:09:08"
    stream.viewer_count = 10

    return stream


def build_test_metrics():
    metrics: ChannelMetrics = ChannelMetrics()
    metrics.mood = ChatMood.engaged
    metrics.msg_per_min = 50
    metrics.msg_per_sec = (50 / 60).__round__(1)

    return metrics


def build_test_channel():
    channel: Channel = Channel()
    channel.id = "12345"
    channel.name = "TestChannel"
    channel.web_service_source = "Test"
    channel.stream = build_test_stream()
    channel.metrics = build_test_metrics()

    return channel


class TestChannelProvider(TestCase):

    def setUp(self) -> None:
        self.config = ServiceConfig()
        self.web_service_mock: WebServiceBase = Mock()
        self.chat_service_mock: ChatServiceBase = Mock()
        self.db_mock: DBBase = Mock()

    def tearDown(self) -> None:
        pass

    def test_get_channel(self):
        expected_channel: Channel = build_test_channel()

        self.web_service_mock.get_channel = MagicMock(return_value=expected_channel)
        self.web_service_mock.get_stream = MagicMock(return_value=expected_channel.stream)
        self.web_service_mock.get_source = MagicMock(return_value=expected_channel.web_service_source)
        self.chat_service_mock.get_source = MagicMock(return_value=expected_channel.web_service_source)
        self.chat_service_mock.st
        self.db_mock.get_source = MagicMock(return_value="SQLite")
        self.db_mock.count_chat_messages_as_of = MagicMock(return_value=expected_channel.metrics.msg_per_min)

        provider = ChannelProvider(self.config, self.web_service_mock, self.chat_service_mock,
                                   self.db_mock)

        actual_channel: Channel = provider.get_channel("Test", "TestChannel")

        self.assertEqual(expected_channel, actual_channel)

    def test_service_registration(self):
        source = "Test".upper()
        self.web_service_mock.get_source = MagicMock(return_value=source)
        self.chat_service_mock.get_source = MagicMock(return_value=source)
        self.db_mock.get_source = MagicMock(return_value=source)

        provider = ChannelProvider(self.config, self.web_service_mock, self.chat_service_mock,
                                   self.db_mock)

        self.assertIsNotNone(provider.web_services[source])
        self.assertIsNotNone(provider.chat_services[source])
        self.assertIsNotNone(provider.dbs[source])
