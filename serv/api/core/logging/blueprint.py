from flask import Blueprint

from serv.api.core.logging import schemas  # noqa

logging = Blueprint(
    'logging', __name__, url_prefix='/core/logging'
)


@logging.route("/log_file_groups")
def get_log_file_groups():
    """
    List all the available log file groups. Response returns log file detail
    wrapped into log_file_uuid and grouped by date.

    ---
    get:
      tags:
        - core
        - logging
        - potentially-new
      parameters:
        - in: query
          schema: LogFileGroupsSchema
          required: false
      description: List of all available log files grouped by date.
        Response returns log file detail wrapped into log_file_uuid and
        grouped by date.
      responses:
        200:
          description: Success
          schema: LogFileGroupsResponseSchema
        400:
          description: Invalid request data provided
          schema: HttpErrorSchema
    """
    pass


@logging.route("/raw")
def get_log_file_raw():
    """
    Request specific log files by uuid, date or screen_identifier.
    If the log file is not available yet, Screenwriter should schedule a
    collection as soon as it is possible. Having the possibility to filter
    by screen_identifier and/or date sort of make /logging/log_file_groups

    ---
    get:
      tags:
        - core
        - logging
      parameters:
        - in: query
          schema: LogFileRawSchema
          required: false
      description: Request specific log files by uuid, date or
        screen_identifier. If the log file is not available yet, Screenwriter
        should schedule a collection as soon as it is possible. Having the
        possibility to filter by screen_identifier and/or date sort of make
        /logging/log_file_groups obsolete.
      responses:
        200:
          description: Success
          schema: LogFileRawResponseSchema
        400:
          description: Invalid request data provided
          schema: HttpErrorSchema
    """
    pass
