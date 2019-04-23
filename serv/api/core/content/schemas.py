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
        values=fields.Integer(description='Last modified of the content')
    )


class CPLXMLFilterSchema(Schema):
    content_ids = fields.List(
        fields.UUID(),
        description='List of content uuids'
    )


class CPLXMLResponseSchema(Schema):
    data = fields.Dict(
        keys=fields.UUID(description='Content UUID'),
        values=fields.String(description='CPL XML data')
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
            values=fields.Dict(description='Validation status and other info')
        )
    )
