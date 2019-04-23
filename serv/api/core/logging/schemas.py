from marshmallow import fields, Schema


class LogFileGroupsSchema(Schema):
    starting_date = fields.Date(
        required=False,
        description='Only return log files from this starting date'
    )
    modified_after = fields.Integer(
        required=False,
        description='Only return log files modified after this timestamp'
    )


class LogFileDetails(Schema):
    last_modified = fields.Integer(
        description='Timestamp of when log was last modified'
    )
    screen_identifier = fields.String(
        description='Screen identifier'
    )
    dnqualifier = fields.String(
        description='Dnqualifier of the screen server the log file comes from'
    )


class LogFileGroupsResponseSchema(Schema):
    data = fields.Dict(
        keys=fields.Date(),
        values=fields.Dict(
            keys=fields.UUID(),
            values=fields.Nested(LogFileDetails)
        )
    )


class LogFileRawSchema(Schema):
    log_file_uuids = fields.List(
        fields.UUID(),
        description='Filter logs by uuid.'
    )
    dates = fields.List(
        fields.Date(),
        description='Filter logs by date.'
    )
    screen_identifiers = fields.List(
        fields.String(),
        description='Filter logs by screen_identifier.'
    )
    dnqualifiers = fields.List(
        fields.String(),
        description='Filter logs by dnqualifiers.'
    )
    modified_after = fields.Integer(
        required=False,
        description='Only return log files modified after this timestamp'
    )


class LogFileRawDetails(Schema):
    uuid = fields.UUID(description='Primary identifier of a log file.')
    created = fields.Integer()
    dnqualifier = fields.String(
        description="Dnqualifier of the screen server."
    )
    error_message = fields.String(
        description="Error occured in collection or parsing phase."
    )
    signed = fields.Boolean()
    screen_identifier = fields.String(description='Screen identifier e.g. S01')
    absolute_file_path = fields.String(description='Absolute file path')
    unencrypted = fields.Boolean()
    device_ip_address = fields.String(description='Screen server IP address.')
    last_modified = fields.Integer()
    repull_marked = fields.Boolean()
    date = fields.String(description='Log file date.')
    serial = fields.String(description='Screen server serial number.')
    parse_attempted = fields.Boolean()
    pulled = fields.Boolean()
    parsed = fields.Boolean()
    pull_attempted = fields.Boolean()
    no_playouts = fields.Boolean()
    xml = fields.String(description='Full .xml file as retrieved from server.')


class LogFileRawResponseSchema(Schema):
    data = fields.Dict(
        keys=fields.UUID(description='Primary Identifier of the log file.'),
        values=fields.Nested(LogFileRawDetails)
    )
