# rebuild_indexes.py

import argparse

# Import Frame classes
from api.odm.event import EventDocument
from api.odm.interest import InterestDocument

from config._abstract import AbstractConfig
AbstractConfig.set_up_db()

# Build a table of Frame classes
frame_cls_table = {
    EventDocument._collection: EventDocument,
    InterestDocument._collection: InterestDocument
}


def rebuild_indexes(collection_names):
    """(Re)build database indexes"""

    # If the only collection specified is all then rebuild all indexes
    if len(collection_names) == 1 and collection_names[0] == 'all':
        collection_names = frame_cls_table.keys()

    for name in collection_names:

        # Find the class for the collection
        frame_cls = frame_cls_table.get(name)
        assert frame_cls, 'Class not defined for collection: ' + name

        # Drop all indexes for the collection then recreate them
        frame_cls.get_collection().drop_indexes()
        frame_cls.get_collection().create_indexes(frame_cls._indexes)


if __name__ == "__main__":

    parser = argparse.ArgumentParser(description='(Re)build database indexes')
    parser.add_argument('collections', type=str, nargs='+')
    args = parser.parse_args()

    rebuild_indexes(args.collections)
