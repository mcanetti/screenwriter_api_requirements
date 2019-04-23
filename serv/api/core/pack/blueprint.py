from flask import Blueprint

from serv.api.core.pack import schemas  # noqa

pack = Blueprint(
    'pack', __name__, url_prefix='/core/pack'
)


@pack.route("/last_modified")
def get_last_modified():
    """
    Get last_modified for all available packs. Filter by modified_after

    ---
    get:
      tags:
        - core
        - pack
      parameters:
        - in: query
          schema: PackLastModifiedFilterSchema
          required: false
      description: Get last_modified for all available packs. Filter by
        modified_after
      responses:
        200:
          description: Success
          schema: PackLastModifiedResponseSchema
        400:
          description: Invalid request data provided
          schema: HttpErrorSchema
    """
    pass


@pack.route("/packs")
def get_packs():
    """
    Get packs details. Filter by pack_uuids. Current behaviour requires
    querying the info twice to get last_modified and title_external_ids of the
    pack. We would like to have them returned in any case.

    ---
    get:
      tags:
        - core
        - pack
      parameters:
        - in: query
          schema: PacksFilterSchema
          required: false
      description: Get packs details. Filter by pack_uuids. Current behaviour
        requires querying the info twice to get last_modified and
        title_external_ids of the pack. We would like to have them returned
        in any case.
      responses:
        200:
          description: Success
          schema: PacksResponseSchema
        400:
          description: Invalid request data provided
          schema: HttpErrorSchema
    """
    pass
