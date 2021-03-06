import pymongo
from mongoframes import *
from config._abstract import AbstractConfig


class Place(SubFrame):
    _fields = {
        'lng',
        'lat'
    }


class EventDocument(Frame):
    _db = AbstractConfig.get_config_class().MONGO_DB

    _collection = 'events'

    _fields = {
        '_id',
        'name',
        'sessions',
        'place',
        'tags',
        'created',
        'modified',
        'interested'
    }

    _default_projection = {
        'place': {'$sub': Place}
    }

    _indexes = [
        IndexModel([('name', pymongo.TEXT)]),
        IndexModel([('place', pymongo.GEO2D)]),
        IndexModel([('sessions', 1)]),
        IndexModel([('tags', 1)]),
        IndexModel([('created', pymongo.ASCENDING)]),
        IndexModel([('modified', pymongo.ASCENDING)])
    ]

    @property
    def interested(self):
        from api.odm.interest import InterestDocument
        return InterestDocument.count({'event': self._id})


EventDocument.listen('insert', EventDocument.timestamp_insert)
EventDocument.listen('update', EventDocument.timestamp_update)
