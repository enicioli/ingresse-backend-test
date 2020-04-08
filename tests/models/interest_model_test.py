import json
import pytest
import unittest
from bson import ObjectId

from tests import setup
from api.models.interest import InterestModel
from api.odm.interest import InterestDocument
from api.odm.event import EventDocument

app = setup.create_flask_app()


class InterestModelTest(unittest.TestCase):

    @pytest.mark.usefixtures('fixture_interest_post_body', 'fixture_event_document')
    def test_1_create_interest(self):
        data = json.loads(self.interest_post_body)
        interest = InterestModel.create_interest(data, event=self.event)

        self.assertIsInstance(interest, InterestDocument)
        self.assertIsNotNone(interest._id)

    @pytest.mark.usefixtures('fixture_interest_document')
    def test_2_get_interest_by_id(self):
        interest = InterestModel.get_interest_by_id(str(self.interest._id))
        interest_not_exists = InterestModel.get_interest_by_id(str(ObjectId()))

        self.assertEqual(interest, self.interest)
        self.assertIsNone(interest_not_exists)

    @pytest.mark.usefixtures('fixture_interest_document')
    def test_3_get_interests_by_email(self):
        interests = InterestModel.get_interests_by_email(self.interest.email)
        for interest in interests:
            self.assertEqual(interest.email, self.interest.email)

        interests_empty_list = InterestModel.get_interests_by_email('notfound@email.com')
        self.assertListEqual(interests_empty_list, [])

    @pytest.mark.usefixtures('fixture_interest_document')
    def test_4_delete_interest(self):
        InterestModel.delete_interest(self.interest)
        self.assertIsNone(InterestModel.get_interest_by_id(str(self.interest._id)))

    @pytest.fixture(scope="function")
    def fixture_interest_post_body(request):
        request.interest_post_body = setup.read_fixture_file('interest_post_body.json')

    @pytest.fixture(scope="function")
    def fixture_event_document(request):
        event = EventDocument(**json.loads(setup.read_fixture_file('event_post_body.json')))
        event._id = ObjectId()
        request.event = event

    @pytest.fixture(scope="function")
    def fixture_interest_document(request):
        event = EventDocument(**json.loads(setup.read_fixture_file('event_post_body.json')))
        event._id = ObjectId()

        interest_data = json.loads(setup.read_fixture_file('interest_post_body.json'))

        request.interest = InterestModel.create_interest(interest_data, event=event)


if __name__ == '__main__':
    unittest.main()
