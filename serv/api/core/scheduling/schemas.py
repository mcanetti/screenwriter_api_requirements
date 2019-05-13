from marshmallow import fields, Schema


class ScheduleLastModifiedFilterSchema(Schema):
    # new
    modified_after = fields.Integer(
        required=False,
        description='Only returns schedule modified after this timestamp'
    )
    # old
    delete = fields.Boolean()


class ScheduleLastModifiedResponseSchema(Schema):
    data = fields.Dict(
        keys=fields.UUID(descrption='Primary id of Schedule'),
        values=fields.Float(description='Schedule last_modified field'),
        description='Dictionary where keys are schedule UUIDs and values are last_modified integers.'  # noqa
    )
