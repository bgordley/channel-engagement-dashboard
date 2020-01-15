from service import app


@app.route("/")
def index():
    return "CED - Channel Engagement Dashboard [WIP]"
