from flask import Flask
from flask_restplus import Api

from service.config.service_dependencies import ServiceDependencies

dependencies = ServiceDependencies()

flask_app: Flask = Flask(__name__, instance_relative_config=True)
app = Api(app=flask_app)
