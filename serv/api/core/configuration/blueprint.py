from flask import Blueprint

configuration = Blueprint(
    'configuration', __name__, url_prefix='/core/configuration'
)


@configuration.route("/complex_data")
def get_complex_data():
    """
    Get non-volatile complex data.

    ---
    get:
      tags:
        - core
        - configuration
        - new
      description:
        Get non-volatile complex data. Currently componing an 'flm' data
        message from the following endpoints. Some of them like monitoring/info
        contain volatile info such as disk usage we would like to pull more
        often independently from the other complex data.
        screenwriter_data_endpoints = [
            '/core/configuration/get_addresses',
            '/core/configuration/get_contacts',
            '/core/complex_infos',
            '/get_license',
            '/core/configuration/device',
            '/core/configuration/screen',
            '/core/monitoring/info',
        ]
        We need two different endpoints, one that combines more static data
        from the above routes and one that provides only volatile data we can
        pull more often.
      responses:
        200:
          description: Success
        400:
          description: Invalid request data provided
          schema: HttpErrorSchema
    """
    pass


@configuration.route("/monitoring_data")
def get_monitoring_data():
    """
    Get volatile complex data.

    ---
    get:
      tags:
        - core
        - configuration
        - new
      description:
        Get volatile complex data. Currently componing an 'flm' data
        message from the following endpoints. Some of them like monitoring/info
        contain volatile info such as disk usage we would like to pull more
        often independently from the other complex data.
        screenwriter_data_endpoints = [
            '/core/configuration/get_addresses',
            '/core/configuration/get_contacts',
            '/core/complex_infos',
            '/get_license',
            '/core/configuration/device',
            '/core/configuration/screen',
            '/core/monitoring/info',
        ]
        We need two different endpoints, one that combines more static data
        from the above routes and one that provides only volatile data we can
        pull more often.
      responses:
        200:
          description: Success
        400:
          description: Invalid request data provided
          schema: HttpErrorSchema
    """
    pass
