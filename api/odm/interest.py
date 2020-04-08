import pymongo
from mongoframes import *
from api.odm.event import EventDocument
from config._abstract import AbstractConfig


class InterestDocument(Frame):
    _db = AbstractConfig.get_config_class().MONGO_DB

    _collection = 'interests'

    _fields = {
        'event',
        'email',
        'created'
    }

    _default_projection = {
        'event': {'$ref': EventDocument}
    }

    _indexes = [
        IndexModel([('email', 1)]),
        IndexModel([('created', pymongo.ASCENDING)]),
        IndexModel([('event', 1), ('email', 1)], unique=True)
    ]


InterestDocument.listen('insert', InterestDocument.timestamp_insert)
