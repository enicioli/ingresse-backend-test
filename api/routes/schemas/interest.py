from api.routes.schemas._abstract import AbstractSchema


class InterestSchema(AbstractSchema):
    schema = {
        "$schema": "http://json-schema.org/draft-07/schema#",
        "properties": {
            "email": {
                "type": "string",
                "format": "idn-email",
            },
        },
        "required": [
            "email",
        ],
        "type": "object",
    }
