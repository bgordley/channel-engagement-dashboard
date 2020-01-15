from flask import Flask

app = Flask(__name__, instance_relative_config=True)

# Register API routes here
from service.routes import client, health, metrics

app.config.from_object('service.config')
