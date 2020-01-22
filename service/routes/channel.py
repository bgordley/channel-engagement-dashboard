from flask_restplus import Resource

from service import app, dependencies

namespace = app.namespace('channel', description='Channel endpoints')
channel_provider = dependencies.channel_provider


@namespace.route("/<name>")
class ChannelRoute(Resource):
    def get(self, name):
        return channel_provider.get_channel("Twitch", name).to_json()
