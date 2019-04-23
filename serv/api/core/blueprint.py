from flask import Blueprint, current_app, jsonify

core_api = Blueprint('core_api', __name__)


@core_api.route("/status")
def status():
    """
    Status endpoint for the application.

    ---
    get:
      tags:
        - core
      description: Status endpoint for the application.
      responses:
        200:
          description: Success.
          schema:
            type: object
            properties:
              service:
                type: string
              status:
                type: integer
                example: 200
    """
    return jsonify(service='scwr-api-requirements', status='ok')


@core_api.route('/swagger.json')
def swagger():
    """
    View a JSON representation of the swagger documentation.

    ---
    get:
      tags:
        - core
      description: View a JSON representation of the swagger documentation.
      responses:
        200:
          description: Success.
          schema:
            type: object
    """
    return jsonify(current_app.spec.to_dict())
