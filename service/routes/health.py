from service import app


@app.route("/health")
def health():
    return "Service is healthy."
