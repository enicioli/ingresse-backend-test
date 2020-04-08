from flask import Flask, g
from config._abstract import AbstractConfig

from api.routes.event import EventController
from api.routes.interest import InterestController


def create_flask_app():
    app = Flask(__name__)
    db = AbstractConfig.set_up_db(True)

    def before_setup_db():
        g.db = db

    app.before_request(before_setup_db)

    app.register_blueprint(EventController)
    app.register_blueprint(InterestController)

    return app


def read_fixture_file(file):
    with open('./tests/fixtures/{}'.format(file), 'r') as f:
        return f.read()
