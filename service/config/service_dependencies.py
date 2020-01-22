from service.config.service_config import ServiceConfig
from service.db.db_base import DBBase
from service.providers.channel_provider import ChannelProvider
from service.services.chat_service_base import ChatServiceBase
from service.services.web_service_base import WebServiceBase


class ServiceDependencies(object):
    config: ServiceConfig
    db: DBBase
    web_service: WebServiceBase
    chat_service: ChatServiceBase
    channel_provider: ChannelProvider
