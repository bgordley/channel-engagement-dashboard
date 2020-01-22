from os import path

import requests

from service import dependencies, flask_app
from service.config.service_config import ServiceConfig
from service.db.sqlite_db import SQLiteDB
from service.providers.channel_provider import ChannelProvider
from service.services.mock_chat_service import MockChatService
from service.services.twitch_web_service import TwitchWebService

if __name__ == '__main__':
    if not path.isfile("config.json"):
        raise Exception("No config file found, expected config.json file in root directory.")

    dependencies.config = ServiceConfig().load_json_config("config.json")

    dependencies.db = SQLiteDB(dependencies.config)
    dependencies.db.migrate()

    dependencies.web_service = TwitchWebService(requests, dependencies.config)
    dependencies.chat_service = MockChatService("Twitch", dependencies.db)
    dependencies.channel_provider = ChannelProvider(dependencies.config, dependencies.web_service,
                                                    dependencies.chat_service, dependencies.db)

    flask_app.config.from_object(dependencies.config.flask)

    # Register API routes here
    from service.routes import channel, health

    flask_app.run()
