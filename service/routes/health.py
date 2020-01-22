from flask_restplus import Resource

from service import app

namespace = app.namespace('health', description='Health-check endpoints')


@namespace.route("/")
class HealthCheckRoute(Resource):
    def get(self):
        return "Service is healthy."
