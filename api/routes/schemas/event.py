from api.routes.schemas._abstract import AbstractSchema


class EventSchema(AbstractSchema):
    schema = {
        "$schema": "http://json-schema.org/draft-07/schema#",
        "properties": {
            "name": {
                "minLength": 3,
                "maxLength": 255,
                "type": "string",
            },
            "place": {
                "type": "object",
                "properties": {
                    "lng": {
                        "type": "number",
                        "minimum": -180,
                        "maximum": 180,
                    },
                    "lat": {
                        "type": "number",
                        "minimum": -90,
                        "maximum": 90,
                    },
                },
                "required": [
                    "lng",
                    "lat",
                ],
            },
            "sessions": {
                "type": "array",
                "items": {
                    "type": "string",
                    "format": "date-time",
                },
                "minItems": 1,
            },
            "tags": {
                "type": "array",
                "items": {
                    "type": "string",
                },
            },
        },
        "required": [
            "name",
            "place",
            "sessions",
            "tags",
        ],
        "type": "object",
    }


class EventSchemaUpdate(EventSchema):

    def get_schema(self):
        schema = self.schema
        if 'required' in schema:
            schema.pop('required')

        return schema
