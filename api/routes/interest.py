from flask import Blueprint, request, jsonify
from api.routes._abstract import AbstractRoute
from api.routes.schemas.interest import InterestSchema
from api.models.interest import InterestModel
from api.models.event import EventModel

InterestController = Blueprint('interest', __name__, url_prefix='/interest')


@InterestController.route('/event/<event_id>', methods=['POST'])
def route_create_interest(event_id: str):
    if not AbstractRoute.is_object_id(event_id):
        return AbstractRoute.bad_request()

    json_data = request.get_json(force=True)
    result, message = InterestSchema.validate(json_data)
    if result is False:
        return AbstractRoute.bad_request(message)

    event = EventModel.get_event_by_id(event_id)
    if event is None:
        return AbstractRoute.not_found()

    interest = InterestModel.create_interest(json_data, event)
    return jsonify(interest.to_json_type()), 201


@InterestController.route('/<interest_id>', methods=['GET'])
def route_get_interest(interest_id: str):
    if not AbstractRoute.is_object_id(interest_id):
        return AbstractRoute.bad_request()

    interest = InterestModel.get_interest_by_id(interest_id)
    if interest is None:
        return AbstractRoute.not_found()

    return jsonify(interest.to_json_type())


@InterestController.route('/<interest_id>', methods=['DELETE'])
def route_delete_interest(interest_id: str):
    if not AbstractRoute.is_object_id(interest_id):
        return AbstractRoute.bad_request()

    interest = InterestModel.get_interest_by_id(interest_id)
    if interest is None:
        return AbstractRoute.not_found()

    InterestModel.delete_interest(interest)
    return jsonify({'message': 'OK'})


@InterestController.route('/email/<email>', methods=['GET'])
def route_get_customer_interests(email: str):
    interests = InterestModel.get_interests_by_email(email)
    return jsonify(list(map(lambda interest: interest.to_json_type(), interests)))
