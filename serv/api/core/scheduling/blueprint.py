from flask import Blueprint

from serv.api.core.scheduling import schemas  # noqa

scheduling = Blueprint(
    'scheduling', __name__, url_prefix='/core/scheduling'
)


@scheduling.route("/last_modified")
def get_last_modified():
    """
    List last_modified for all available schedules.
    Add filtering for modified_after to return only schedules with
    last_modified > modified_after.

    ---
    get:
      tags:
        - core
        - schedule
      parameters:
        - in: query
          schema: ScheduleLastModifiedFilterSchema
          required: false
      description: List last_modified for all available schedules.
        Add filtering for modified_after to return only schedules with
        last_modified > modified_after.
      responses:
        200:
          description: Success
          schema: ScheduleLastModifiedResponseSchema
        400:
          description: Invalid request data provided
          schema: HttpErrorSchema
    """
    pass
