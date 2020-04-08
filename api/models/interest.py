from api.odm.interest import InterestDocument
from api.odm.event import EventDocument
from bson.objectid import ObjectId


class InterestModel:
    def __init__(self):
        pass

    @staticmethod
    def create_interest(data: dict,
                        event: EventDocument):
        interest = InterestDocument(data)
        interest.event = event
        interest.insert()
        return interest

    @staticmethod
    def get_interest_by_id(interest_id: str):
        return InterestDocument.by_id(ObjectId(interest_id))

    @staticmethod
    def get_interests_by_email(email: str):
        return InterestDocument.many({'email': email})

    @staticmethod
    def delete_interest(interest: InterestDocument):
        return interest.delete()
