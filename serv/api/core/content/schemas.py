from marshmallow import fields, Schema


class ContentLastModifiedFilterSchema(Schema):
    modified_after = fields.Integer(
        required=False,
        description='Only returns last_modified for content "modified" after this timestamp'  # noqa
    )
    content_ids = fields.List(
        fields.UUID(),
        description='List of content uuids'
    )


class ContentLastModifiedResponseSchema(Schema):
    data = fields.Dict(
        keys=fields.UUID(description='Content UUID'),
        values=fields.Integer(description='Last modified of the content'),
        description='Dictionary where keys are Content UUIDS and values are last_modified integers.'  # noqa
    )


class ContentValidationLastModifiedFilterSchema(Schema):
    modified_after = fields.Integer(
        required=False,
        description='Only returns last_modified for content validation "modified" after this timestamp'  # noqa
    )
    content_ids = fields.List(
        fields.UUID(),
        description='List of content uuids'
    )


class CPLXMLFilterSchema(Schema):
    content_ids = fields.List(
        fields.UUID(),
        description='List of content uuids'
    )


class CPLXMLResponseSchema(Schema):
    data = fields.Dict(
        keys=fields.String(description='Content UUID'),
        values=fields.String(description='CPL XML data'),
        description='Dictionary where keys are content UUIDs and values are content XMLs.'  # noqa
    )


class ContentValidationFilterSchema(Schema):
    content_ids = fields.List(
        fields.UUID(),
        description='List of content uuids'
    )


class ContentValidationResponseSchema(Schema):
    data = fields.Dict(
        keys=fields.UUID(description='Content UUID'),
        values=fields.Dict(
            keys=fields.UUID(description='Device UUID'),
            values=fields.Dict(description='Validation status and other info'),
            description='Dictionary where keys are device UUIDs and values are validation details.'  # noqa
        ),
        description='Dictionary where keys are Content UUIDs and values are dictionaries.'  # noqa
    )


class ContentValidationLastModifiedResponseSchema(Schema):
    data = fields.Dict(
        keys=fields.UUID(description='Content UUID'),
        values=fields.Dict(
            keys=fields.UUID(description='Device UUID'),
            values=fields.Integer(description='Validation last_modified'),
            description='Dictionary where keys are device UUIDs and values are validation last_modified integers.'  # noqa
        ),
        description='Dictionary where keys are Content UUIDs and values are dictionaries.'  # noqa
    )
