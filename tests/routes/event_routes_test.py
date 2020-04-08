import json
import pytest
import unittest
from bson import ObjectId

from tests import setup
from api.models.event import EventModel

app = setup.create_flask_app()


class EventRoutesTest(unittest.TestCase):

    @pytest.mark.usefixtures('fixture_event_post_body')
    def test_1_route_create_event(self):
        with app.test_client() as c:
            response = c.post('/event', json=json.loads(self.event_post_body))
            response_bad_request = c.post('/event', json={})

        self.assertEqual(response.status_code, 201)
        self.assertEqual(response_bad_request.status_code, 400)

    @pytest.mark.usefixtures('fixture_event_document', 'fixture_event_update_body')
    def test_2_route_update_event(self):
        with app.test_client() as c:
            response = c.patch('/event/{}'.format(self.event._id), json=json.loads(self.event_update_body))
            response_bad_request_due_to_invalid_id = c.put('/event/{}'.format('0'), json={})
            response_not_found = c.put('/event/{}'.format(str(ObjectId())), json={})
            response_bad_request_due_to_invalid_body = c.put('/event/{}'.format(self.event._id), json={'name': 1})

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response_bad_request_due_to_invalid_id.status_code, 400)
        self.assertEqual(response_not_found.status_code, 404)
        self.assertEqual(response_bad_request_due_to_invalid_body.status_code, 400)

    @pytest.mark.usefixtures('fixture_event_document')
    def test_3_route_get_event(self):
        with app.test_client() as c:
            response = c.get('/event/{}'.format(self.event._id))
            response_bad_request_due_to_invalid_id = c.get('/event/{}'.format('0'))
            response_not_found = c.get('/event/{}'.format(str(ObjectId())), json={})

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response_bad_request_due_to_invalid_id.status_code, 400)
        self.assertEqual(response_not_found.status_code, 404)

    @pytest.mark.usefixtures('fixture_event_document')
    def test_4_route_delete_event(self):
        with app.test_client() as c:
            response = c.delete('/event/{}'.format(self.event._id))
            response_bad_request_due_to_invalid_id = c.delete('/event/{}'.format('0'))
            response_not_found = c.delete('/event/{}'.format(str(ObjectId())), json={})

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response_bad_request_due_to_invalid_id.status_code, 400)
        self.assertEqual(response_not_found.status_code, 404)

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
