import json
import pytest
import unittest
from bson import ObjectId

from tests import setup
from api.models.event import EventModel
from api.models.interest import InterestModel

app = setup.create_flask_app()


class InterestRoutesTest(unittest.TestCase):

    @pytest.mark.usefixtures('fixture_event_document', 'fixture_interest_post_body')
    def test_1_route_create_interest(self):
        with app.test_client() as c:
            body = json.loads(self.interest_post_body)
            response = c.post('/interest/event/{}'.format(self.event._id), json=body)
            response_bad_request_due_to_invalid_id = c.post('/interest/event/{}'.format('0'), json={})
            response_not_found = c.post('/interest/event/{}'.format(str(ObjectId())), json=body)
            response_bad_request_due_to_invalid_body = c.post('/interest/event/{}'.format(self.event._id),
                                                              json={'email': 1})

        self.assertEqual(response.status_code, 201)
        self.assertEqual(response_bad_request_due_to_invalid_id.status_code, 400)
        self.assertEqual(response_not_found.status_code, 404)
        self.assertEqual(response_bad_request_due_to_invalid_body.status_code, 400)

    @pytest.mark.usefixtures('fixture_interest_document')
    def test_2_route_get_interest(self):
        with app.test_client() as c:
            response = c.get('/interest/{}'.format(self.interest._id))
            response_bad_request_due_to_invalid_id = c.get('/interest/{}'.format('0'))
            response_not_found = c.get('/interest/{}'.format(str(ObjectId())))

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response_bad_request_due_to_invalid_id.status_code, 400)
        self.assertEqual(response_not_found.status_code, 404)

    @pytest.mark.usefixtures('fixture_interest_document')
    def test_3_route_get_customer_interests(self):
        with app.test_client() as c:
            response = c.get('/interest/email/{}'.format(self.interest.email))
            response_not_found = c.get('/interest/email/{}'.format('notfound@email.com'))

        self.assertEqual(response.status_code, 200)
        for result in json.loads(response.data):
            self.assertEqual(result['email'], self.interest.email)
        self.assertEqual(response_not_found.status_code, 200)
        self.assertEqual(json.loads(response_not_found.data), [])

    @pytest.mark.usefixtures('fixture_interest_document')
    def test_4_route_delete_interest(self):
        with app.test_client() as c:
            response = c.delete('/interest/{}'.format(self.interest._id))
            response_bad_request_due_to_invalid_id = c.delete('/interest/{}'.format('0'))
            response_not_found = c.delete('/interest/{}'.format(str(ObjectId())), json={})

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response_bad_request_due_to_invalid_id.status_code, 400)
        self.assertEqual(response_not_found.status_code, 404)

    @pytest.fixture(scope="function")
    def fixture_interest_post_body(request):
        request.interest_post_body = setup.read_fixture_file('interest_post_body.json')

    @pytest.fixture(scope="function")
    def fixture_event_document(request):
        request.event = EventModel.create_event(json.loads(setup.read_fixture_file('event_post_body.json')))

    @pytest.fixture(scope="function")
    def fixture_interest_document(request):
        event = EventModel.create_event(json.loads(setup.read_fixture_file('event_post_body.json')))
        request.interest = InterestModel.create_interest(json.loads(setup.read_fixture_file('interest_post_body.json')),
                                                        event)


if __name__ == '__main__':
    unittest.main()
