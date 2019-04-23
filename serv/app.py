from flask import Flask, jsonify
from marshmallow.exceptions import ValidationError
from werkzeug.exceptions import MethodNotAllowed

from serv import exceptions
from serv.spec import init_spec, HttpErrorResponseSchema
from serv.api.core.blueprint import core_api
from serv.api.core.logging.blueprint import logging
from serv.api.core.playlist.blueprint import playlist
from serv.api.core.pack.blueprint import pack
from serv.api.core.configuration.blueprint import configuration
from serv.api.core.content.blueprint import content
from serv.api.core.scheduling.blueprint import scheduling


def create_app(cfg):
    """
    Central factory for creating and configuring the Flask app
    """
    app = Flask(__name__)
    app.config.update(cfg)
    return app


def init_app(app):
    """
    Configuring the Flask app's extensions
    """
    app.register_blueprint(core_api)
    app.register_blueprint(logging)
    app.register_blueprint(playlist)
    app.register_blueprint(pack)
    app.register_blueprint(configuration)
    app.register_blueprint(content)
    app.register_blueprint(scheduling)

    init_spec(app)

    @app.errorhandler(exceptions.BadRequest)
    @app.errorhandler(MethodNotAllowed)
    @app.errorhandler(ValidationError)
    def handle_invalid_usage(exc):
        data = {}

        if isinstance(exc, MethodNotAllowed):
            data['message'] = f'{exc.description}, \
                              methods allowed {exc.valid_methods}'
        elif isinstance(exc, ValidationError):
            exc.code = 500
            data['message'] = f'Message serialization error. \
                              Errors:{exc.messages}, Data: {exc.data}'
        else:
            data['message'] = exc.message

        data['code'] = exc.code

        return jsonify(
            HttpErrorResponseSchema().dump({'error': data})
        ), data['code']

    return app
