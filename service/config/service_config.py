import json
from pathlib import Path


class ServiceConfig:
    flask: dict
    twitch: dict
    db: dict

    def __init__(self):
        self.flask = {
            "DEBUG": True
        }
        self.twitch = {
            "client_id": "TWITCH_CLIENT_ID_HERE",
            "client_secret": "TWITCH_CLIENT_SECRET_HERE"
        }
        self.db = {
            "source": "SQLite"
        }

    def load_json_config(self, path):
        if not Path(path).is_file():
            print("Failed to load config file '%s'. Does not exist." % path)
            return

        with open(path) as file:
            data = json.load(file)

            self.flask = data["flask"]
            self.twitch = data["twitch"]
            self.db = data["db"]

        return self
