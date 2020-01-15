from service import app


@app.route("/metrics/example")
def example():
    return {"avgMsgPerMinute": 12, "avgMsgPerHour": 642, "msgLast5Mins": 75, "msgLast1Min": 12, "mood": "Excited!"}
