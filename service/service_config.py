import json
from pathlib import Path


class ServiceConfig:
    flask = {}
    twitch = {}

    def load_json_config(self, path):
        if not Path(path).is_file():
            print("Failed to load config file '%s'. Does not exist." % path)
            return

        with open(path) as file:
            data = json.load(file)

            self.flask = data["flask"]
            self.twitch = data["twitch"]

        return self
