from api.odm.event import EventDocument
from bson import ObjectId, json_util


class EventModel:
    def __init__(self):
        pass

    @staticmethod
    def create_event(data: dict):
        data = json_util.loads(json_util.dumps(data))
        event = EventDocument(data.copy())
        event.insert()
        return event

    @staticmethod
    def update_event(event: EventDocument,
                       data: dict):
        data = json_util.loads(json_util.dumps(data))
        for key, value in data.items():
            event.__setattr__(key, value)

        event.update()
        return event

    @staticmethod
    def get_event_by_id(event_id: str):
        return EventDocument.by_id(ObjectId(event_id))

    @staticmethod
    def delete_event(event: EventDocument):
        return event.delete()

    @staticmethod
    def search(query: dict):
        query = json_util.loads(json_util.dumps(query))
        return EventDocument.many(query)
