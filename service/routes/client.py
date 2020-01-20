from service import app
from service import channel_provider


@app.route("/")
def index():
    return channel_provider.get_channel("Twitch", "livibee").to_json()
