import json
import pytest
import unittest
from bson import ObjectId

from tests import setup
from api.models.event import EventModel
from api.odm.event import EventDocument

app = setup.create_flask_app()


class EventModelTest(unittest.TestCase):

    @pytest.mark.usefixtures('fixture_event_post_body')
    def test_1_create_event(self):
        data = json.loads(self.event_post_body)
        event = EventModel.create_event(data)

        self.assertIsInstance(event, EventDocument)
        self.assertIsNotNone(event._id)

    @pytest.mark.usefixtures('fixture_event_document')
    def test_2_get_event_by_id(self):
        event = EventModel.get_event_by_id(str(self.event._id))
        event_not_exists = EventModel.get_event_by_id(str(ObjectId()))

        self.assertEqual(event, self.event)
        self.assertIsNone(event_not_exists)

    @pytest.mark.usefixtures('fixture_event_document', 'fixture_event_update_body')
    def test_3_update_event(self):
        update_event = json.loads(self.event_update_body)
        event = EventModel.update_event(self.event, update_event)

        for key in update_event:
            self.assertEqual(event.get(key), update_event[key])

    @pytest.mark.usefixtures('fixture_event_document')
    def test_4_delete_event(self):
        EventModel.delete_event(self.event)
        self.assertIsNone(EventModel.get_event_by_id(str(self.event._id)))

    @pytest.fixture(scope="function")
    def fixture_event_post_body(request):
        request.event_post_body = setup.read_fixture_file('event_post_body.json')

    @pytest.fixture(scope="function")
    def fixture_event_update_body(request):
        request.event_update_body = setup.read_fixture_file('event_update_body.json')

    @pytest.fixture(scope="function")
    def fixture_event_document(request):
        request.event = EventModel.create_event(json.loads(setup.read_fixture_file('event_post_body.json')))


if __name__ == '__main__':
    unittest.main()
