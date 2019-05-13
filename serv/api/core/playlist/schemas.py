from marshmallow import fields, Schema


class PlaylistsFilterSchema(Schema):
    modified_after = fields.Integer(
        required=False,
        description='Only returns playlists modified after this timestamp'
    )
    device_ids = fields.List(
        fields.UUID(),
        description='List of device uuids')
    playlist_ids = fields.List(
        fields.UUID(),
        description='List of playlist uuids'
    )
    request_data_items = fields.List(
        fields.String(),
        description='Streamline returned result for wanted details. If [] return everything.'  # noqa
    )
    validate = fields.Boolean()
    flatten = fields.Boolean()


class PlaylistSchema(Schema):
    # Fields specified in request_data_items or EVERYTHING about a playlist
    last_modified = fields.Integer(
        description='Timestamp of when playlst was last modified'
    )
    playlist = fields.Dict()
    uuid = fields.UUID()
    title = fields.String()
    content_ids = fields.List(fields.String())
    is_4k = fields.Boolean()
    is_hfr = fields.Boolean()
    is_template = fields.Boolean()
    is_3d = fields.Boolean()
    clean = fields.Boolean()
    preshow_duration = fields.Integer()
    duration_in_seconds = fields.Integer()


class PlaylistsResponseSchema(Schema):
    data = fields.Dict(
        keys=fields.UUID(description='Device uuid wrap'),
        values=fields.Dict(
            keys=fields.UUID(description='Playlist uuid'),
            values=fields.Nested(PlaylistSchema),
            description='Dictionary where keys are playlist UUIDs and values are playlist details.'  # noqa
        ),
        description='Dictionary where keys are device UUIDs and values are dictionaries.'  # noqa
    )


class SPLFilterSchema(Schema):
    modified_after = fields.Integer(
        required=False,
        description='Only returns playlists modified after this timestamp'
    )
    device_ids = fields.List(
        fields.UUID(),
        description='List of device uuids')
    playlist_ids = fields.List(
        fields.UUID(),
        description='List of playlist uuids'
    )


class SPLSchema(Schema):
    spl_data = fields.String()
    device_uuid = fields.UUID()


class SPLResponseSchema(Schema):
    data = fields.Dict(
        keys=fields.UUID(),
        values=fields.Nested(SPLSchema)
    )
