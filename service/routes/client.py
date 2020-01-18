from service import app
from service import web_service


@app.route("/")
def index():
    return web_service.get_game(33214)
