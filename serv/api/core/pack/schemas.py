from marshmallow import fields, Schema


class PackLastModifiedFilterSchema(Schema):
    modified_after = fields.Integer(
        required=False,
        description='Only returns last_modified for packs modified after this timestamp'  # noqa
    )


class PackLastModifiedResponseSchema(Schema):
    data = fields.Dict(
        keys=fields.UUID(description='Pack UUID'),
        values=fields.Integer(description='Last modified of the pack'),
        description='Dictionary where keys are pack UUIDs and values are last_modified integers.'
    )


class PacksFilterSchema(Schema):
    pack_uuids = fields.List(
        fields.UUID(),
        description='List of pack uuids'
    )
    datatable_query = fields.Boolean()
    requested_data_items = fields.List(
        fields.String(),
        description='Return these attributes only.'
    )


class PackSchema(Schema):
    # EXISTING
    uuid = fields.UUID(
        required=True,
        description='Generic identifier of a pack resource'
    )
    name = fields.String(required=True, description='Name of the pack')
    clips = fields.List(
        fields.Dict(),
        required=True,
        description='List of clips present in the pack'
    )
    date_from = fields.Date(
        allow_none=True, description='Date since the pack is valid'
    )
    date_to = fields.Date(
        allow_none=True, description='Final date for the pack to be valid'
    )
    time_from = fields.Time(
        allow_none=True, description='Time since the pack is valid'
    )
    time_to = fields.Time(
        allow_none=True, description='Final time for the pack to be valid'
    )
    issuer = fields.String(required=True, description='Pack issuer')
    priority = fields.Integer(allow_none=True, description='Pack priority')
    screen_identifiers = fields.List(
        fields.String(description='Main identifier of a screen'),
        allow_none=True,
        description='List of screen identifiers'
    )
    external_show_attribute_maps = fields.List(
        fields.Dict(), allow_none=True, description='List of show attributes'
    )
    placeholder_uuid = fields.UUID(
        allow_none=True,
        description='Main identifier of a placeholder resource'
    )
    placeholder_name = fields.String(
        allow_none=True, description='Name of a placeholder resource'
    )
    title_name = fields.String(
        allow_none=True, description='Name of the title'
    )
    title_map_uuid = fields.UUID(
        allow_none=True, description='Main identifier of a title map'
    )
    title_uuid = fields.UUID(
        allow_none=True, description='Main identifier of a title'
    )

    # Currently gotten with extra request with
    # request_data_items=['last_modified', 'title_external_ids']
    title_external_ids = fields.List(
        fields.Dict(),
        allow_none=True,
        description='List of external IDs the title is matched to'
    )
    last_modified = fields.Float(
        allow_none=True,
        description='Last time the pack got modified, only used when syncing packs from site, not on send'  # noqa
    )


class PacksResponseSchema(Schema):
    data = fields.Dict(
        keys=fields.UUID(description='Primary identifier of a Pack.'),
        values=fields.Nested(PackSchema),
        description='Dictionary where keys are pack UUIDs and values are pack details.'  # noqa
    )
