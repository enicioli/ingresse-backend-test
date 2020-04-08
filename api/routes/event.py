from flask import Blueprint, request, jsonify
from api.routes._abstract import AbstractRoute
from api.routes.schemas.event import EventSchema, EventSchemaUpdate
from api.models.event import EventModel
import json

EventController = Blueprint('event', __name__, url_prefix='/event')


@EventController.route('', methods=['POST'])
def route_create_event():
    json_data = request.get_json(force=True)
    result, message = EventSchema.validate(json_data)
    if result is False:
        return AbstractRoute.bad_request()

    event = EventModel.create_event(json_data)
    return jsonify(event.to_json_type()), 201


@EventController.route('/<event_id>', methods=['PUT', 'PATCH'])
def route_update_event(event_id: str):
    if not AbstractRoute.is_object_id(event_id):
        return AbstractRoute.bad_request()

    event = EventModel.get_event_by_id(event_id)
    if event is None:
        return AbstractRoute.not_found()

    json_data = request.get_json(force=True)

    if request.method == 'PATCH':
        result, message = EventSchemaUpdate.validate(json_data)
    else:
        result, message = EventSchema.validate(json_data)

    if result is False:
        return AbstractRoute.bad_request()

    event = EventModel.update_event(event, json_data)
    return jsonify(event.to_json_type())


@EventController.route('/<event_id>', methods=['GET'])
def route_get_event(event_id: str):
    if not AbstractRoute.is_object_id(event_id):
        return AbstractRoute.bad_request()

    event = EventModel.get_event_by_id(event_id)
    if event is None:
        return AbstractRoute.not_found()

    event.interested = event.interested
    return jsonify(event.to_json_type())


@EventController.route('/<event_id>', methods=['DELETE'])
def route_delete_event(event_id: str):
    if not AbstractRoute.is_object_id(event_id):
        return AbstractRoute.bad_request()

    event = EventModel.get_event_by_id(event_id)
    if event is None:
        return AbstractRoute.not_found()

    EventModel.delete_event(event)
    return jsonify({'message': 'OK'})


@EventController.route('/', methods=['GET'])
def route_search_events():
    filters = json.loads(request.args.get('q'))
    events = EventModel.search(filters)

    return jsonify(list(map(lambda event: event.to_json_type(), events)))
