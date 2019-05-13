from apispec import APISpec
from apispec_webframeworks.flask import FlaskPlugin
from apispec.ext.marshmallow import MarshmallowPlugin
from marshmallow import Schema, fields


class HttpErrorSchema(Schema):
    """
    Schema for standard HTTP errors (4XX,5XX)
    """
    message = fields.String(
        description='Description of the error happened during the response')
    code = fields.Integer(description='HTTP code of the response')


class HttpErrorResponseSchema(Schema):
    error = fields.Nested(HttpErrorSchema)


def init_spec(app):
    app.spec = APISpec(
        openapi_version='2.0',
        title='Screenwriter API requirements',
        version='1.0.0',
        plugins=[
            FlaskPlugin(),
            MarshmallowPlugin()
        ]
    )

    with app.app_context():
        views = [
            'logging.get_log_file_groups',
            'logging.get_log_file_raw',
            'playlist.get_playlist',
            'playlist.get_screen_playlist',
            'pack.get_last_modified',
            'pack.get_packs',
            'configuration.get_complex_data',
            'configuration.get_monitoring_data',
            'content.get_last_modified',
            'content.get_validation',
            'content.get_validation_last_modified',
            'content.get_cpl_xml',
            'scheduling.get_last_modified',
        ]
        for view in views:
            app.spec.path(view=app.view_functions[view])
