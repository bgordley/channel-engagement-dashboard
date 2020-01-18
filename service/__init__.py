from flask import Flask

from service.service_config import ServiceConfig
from service.db.db_base import DBBase
from service.db.sqlite_db import SQLiteDB
from service.providers.channel_provider import ChannelProvider
from service.services.chat_service_base import ChatServiceBase
from service.services.twitch_chat_service import TwitchChatService
from service.services.twitch_web_service import TwitchWebService
from service.services.web_service_base import WebServiceBase

# Global vars
config = ServiceConfig().load_json_config("config/config.json")
twitch_client_id = config.twitch["client_id"]

# Construct global dependencies
db: DBBase = SQLiteDB()
web_service: WebServiceBase = TwitchWebService(twitch_client_id)
chat_service: ChatServiceBase = TwitchChatService()
channel_provider: ChannelProvider = ChannelProvider(web_service, chat_service, db)

app = Flask(__name__, instance_relative_config=True)

# Register API routes here
from service.routes import client, health, metrics

app.config.from_object(config.flask)
