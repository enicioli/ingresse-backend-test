from api.odm.event import EventDocument
from bson.objectid import ObjectId


class EventModel:
    def __init__(self):
        pass

    @staticmethod
    def create_event(data: dict):
        event = EventDocument(data)
        event.insert()
        return event

    @staticmethod
    def update_event(event: EventDocument,
                       data: dict):
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
    def search(filters: dict):
        return EventDocument.many(filters)
