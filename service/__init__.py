from flask import Flask

from service.db.db_base import DBBase
from service.db.sqlite_db import SQLiteDB
from service.providers.channel_provider import ChannelProvider
from service.services.chat_service_base import ChatServiceBase
from service.services.twitch_chat_service import TwitchChatService
from service.services.twitch_web_service import TwitchWebService
from service.services.web_service_base import WebServiceBase

# Construct global dependencies
DB: DBBase = SQLiteDB()
WEB_SERVICE: WebServiceBase = TwitchWebService()
CHAT_SERVICE: ChatServiceBase = TwitchChatService()
CHANNEL_PROVIDER: ChannelProvider = ChannelProvider(WEB_SERVICE, CHAT_SERVICE, DB)

app = Flask(__name__, instance_relative_config=True)

# Register API routes here
from service.routes import client, health, metrics

app.config.from_object('service.config')
