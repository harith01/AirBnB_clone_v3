#!/usr/bin/python3
"""view for States that handle all default
RESTFul API actions"""

import storage
from api.v1.views import app_views
from flask import jsonify, abort, request

@app_views.route('/states', method=['GET'])
def get_states():
    """Retrieves the list of allState Objects"""
    states = []
    for state in storage.all("State").values():
        states.append(state.to_dict())
        return jsonify(states)

@app_views.route('/states/<string:state_id>', method=['GET'],
   strict_slashes=False)
def get_state():
    """Retrieves a State object with the corresponding state_id"""
    for state in storage.all("State").values():
        if state.id == state_id:
            return jsonify(state.to_dict())
    abort(404)

@app_views.route('/states/<string:state_id>', method=['DELETE'],
   strict_slashes=False)
def delete_state():
    """Delete State with object having state_id"""
    state = storage.get("State", state_id)
    if state is None:
        abort(400)
    state.delete()
    storage.save()
    return (jsonify({}))

@app_views.route('/states', method=['POST'], strict_slashes=False)
def post_state():
    """Post State object"""
    if not request.get_json():
        return make_response(jsonify({'error': 'Not a JSON'}), 400)
    if 'name' not in request.get_json():
        return make_response(jsonify({'error': 'Missing name'}), 400)
    state = State(**request.get_json())
    state.save()
    return make_response(jsonify(state.to_dict()), 201)

@app_views.route('/states/<string:state_id>', strict_slashes=False,
   method=['PUT'])
def update_state():
    """Update a State object"""
    state = storage.get("State", state_id)
    if state is None:
        abort(404)
    if not request.get_json():
        return make_response(jsonify({'error': 'Not a JSON'}), 400)
    for attr, value in request.get_json().items():
        if attr not in ['id', 'created_at', 'updated_at']:
            setattr(state, attr, value)
    state.save()
    return jsonify(state.to_dict())
