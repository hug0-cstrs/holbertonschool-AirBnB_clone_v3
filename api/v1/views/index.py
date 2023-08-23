#!/usr/bin/python3
""" Index """
from api.v1.views import app_views
from flask import jsonify
from models import storage


@app_views.route('/status', strict_slashes=False)
def status():
    """ Returns JSON """
    return jsonify(status="OK")

@app_views.route('/stats', methods=['GET'], strict_slashes=False)
def number_objects():
    """
    returns class dictionary
    """
    cls_dict = {'amenities': storage.count('Amenity'),
                'cities': storage.count('City'),
                'places': storage.count('Place'),
                'reviews': storage.count('Review'),
                'states': storage.count('State'),
                'users': storage.count('User')}
    return jsonify(cls_dict)
