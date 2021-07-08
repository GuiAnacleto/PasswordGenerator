import os
from flask import Flask
from app.routes import routes


def create_app():
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)

    routes(app)

    return app

app = create_app()

app.run(debug=True)