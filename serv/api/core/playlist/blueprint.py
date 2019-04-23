from flask import Blueprint

from serv.api.core.playlist import schemas  # noqa

playlist = Blueprint(
    'playlist', __name__, url_prefix='/core/playlist'
)


@playlist.route("/playlist")
def get_playlist():
    """
    List of all available playlists. Wrapped under device_uuid
    layer. If the change of structure breaks too many things in Screenwriter
    UI go with new endpoint. Filter by modified_after. Make sure to always
    return a reliable last_modified. If screen playlist, return an `has_spl`
    flag to make us know is it possible to request the spl (see
    /playlist/screen_playlist).

    ---
    get:
      tags:
        - core
        - playlist
      parameters:
        - in: query
          schema: PlaylistsFilterSchema
          required: false
      description: List of all available playlists. Wrapped under device_uuid
        layer. If the change of structure breaks too many things in
        Screenwriter UI go with new endpoint. Filter by modified_after.
        Make sure to always return a reliable last_modified. If screen
        playlist, return an `has_spl` flag to make us know is it possible to
        request the spl (see /playlist/screen_playlist).
      responses:
        200:
          description: Success
          schema: PlaylistsResponseSchema
        400:
          description: Invalid request data provided
          schema: HttpErrorSchema
    """
    pass


@playlist.route("/screen_playlist")
def get_screen_playlist():
    """
    List SPLs. These are not currently stored on the LMS so it is up to you
    guys to decide how to do it, but we need a way to request playlist in the
    original format provided by the screen servers. A flag on playlist/playlist
    endpoint can let us know if the spl is available and we can use this
    endpoint to collect it. Returning it together with other playlist info (so
    from playlist/playlist) may be dispendious but again implementation is up
    to you. Depending on the implementation an extra /screen_playlist/fetch may
    be required to schedule fetching from screen servers.

    ---
    get:
      tags:
        - core
        - playlist
        - new
      parameters:
        - in: query
          schema: SPLFilterSchema
          required: false
      description: List SPLs. These are not currently stored on the LMS so it
        is up to you guys to decide how to do it, but we need a way to request
        playlist in the original format provided by the screen servers. A flag
        on playlist/playlist endpoint can let us know if the spl is available
        and we can use this endpoint to collect it. Returning it together with
        other playlist info (so from /playlist/playlist) may be expensive, but
        again implementation is up to you. Depending on the implementation an
        extra POST `/playlist/screen_playlist/fetch` may be required to
        schedule fetching from screen servers.
      responses:
        200:
          description: Success
          schema: SPLResponseSchema
        400:
          description: Invalid request data provided
          schema: HttpErrorSchema
    """
    pass
