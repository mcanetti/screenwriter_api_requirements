from flask import Blueprint

from serv.api.core.content import schemas  # noqa

content = Blueprint(
    'content', __name__, url_prefix='/core/content'
)


@content.route("/last_modified")
def get_last_modified():
    """
    Get last_modified for all available contents.
    Filtering by modified_after should only return content added
    from the specified timestamp.

    ---
    get:
      tags:
        - core
        - content
        - new
      parameters:
        - in: query
          schema: ContentLastModifiedFilterSchema
          required: false
      description: Get last_modified for all available contents.
          Filtering by modified_after should only return content added
          from the specified timestamp.
      responses:
        200:
          description: Success
          schema: ContentLastModifiedResponseSchema
        400:
          description: Invalid request data provided
          schema: HttpErrorSchema
    """
    pass


@content.route("/validation")
def get_validation():
    """
    Get validation status for all available contents. Validation info is
    wrapped under device_uuids layer. Filter by content_ids to restrict the
    response to the only cpl we care about.

    ---
    get:
      tags:
        - core
        - content
        - new
      parameters:
        - in: query
          schema: ContentValidationFilterSchema
          required: false
      description: Get validation status for all available contents. Validation
          info is wrapped under device_uuids layer. Filter by content_ids to
          restrict the response to the only cpl we care about.
      responses:
        200:
          description: Success
          schema: ContentValidationResponseSchema
        400:
          description: Invalid request data provided
          schema: HttpErrorSchema
    """
    pass


@content.route("/cpl_xml")
def get_cpl_xml():
    """
    Return cpl.xml for every known cpl. Filter by content_ids to restrict the
    response to the only cpl we care about.

    ---
    get:
      tags:
        - core
        - content
        - new
      parameters:
        - in: query
          schema: CPLXMLFilterSchema
          required: false
      description: Return cpl.xml for every known cpl. Filter by content_ids to
          restrict the response to the only cpl we care about.
      responses:
        200:
          description: Success
          schema: CPLXMLResponseSchema
        400:
          description: Invalid request data provided
          schema: HttpErrorSchema
    """
    pass
