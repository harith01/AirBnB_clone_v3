#!/usr/bin/python3
"""Index file"""

from api.v1.views import app_views
from flask import jsonify
from models import storage
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User

@app_views.route('/status', strict_slashes=False)
def showStatus():
    """Show status"""
    return jsonify({"status": "OK"})

@app_views.route('/stats', strict_slashes=False)
def stats():
    """Show number of objects by type"""
    obj_count = {}
    obj_count['amenities'] = storage.count(Amenity) 
    obj_count['cities'] = storage.count(City) 
    obj_count['places'] = storage.count(Place) 
    obj_count['reviews'] = storage.count(Review) 
    obj_count['states'] = storage.count(State) 
    obj_count['users'] = storage.count(User)
    return jsonify(obj_count)
