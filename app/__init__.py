#coding=utf-8
__author__ = 'yanghuihui'

from flask import Flask
from app.conf.config import config
import os
from datetime import timedelta


project_dir = os.path.dirname(os.path.abspath(__file__))


def create_app(config_name):
    app = Flask(__name__)
    app.secret_key = os.urandom(24)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    app.config.setdefault('BOOTSTRAP_SERVE_LOCAL', True)

    from .controllers import main as main_blueprint
    app.register_blueprint(main_blueprint)

    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)

    @app.before_request
    def before_request():
        app.permanent_session_lifetime = timedelta(minutes=30)

    return app
