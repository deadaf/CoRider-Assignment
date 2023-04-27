from flask import Flask
from flask_restful import Api
from config import DevelopmentConfig
from resources import UserResource


def create_app(config_object=DevelopmentConfig):
    app = Flask(__name__)
    app.config.from_object(config_object)

    api = Api(app)
    api.add_resource(UserResource, "/users", "/users/<string:id>")
    return app


# Run the application
if __name__ == "__main__":
    app = create_app()
    app.run(debug=True, port=8001, host="0.0.0.0")
