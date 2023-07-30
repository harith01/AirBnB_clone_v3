#!/usr/bin/python3
"""Create app"""

from api.v1.views import app_views
from flask import Flask, Blueprint, make_response, jsonify
import os
from models import storage


app = Flask(__name__)
app.register_blueprint(app_views)

@app.teardown_appcontext
def teardown_appcontext(code):
    """Teardown Appcontext"""
    storage.close()

@app.errorhandler(404)
def not_found(error):
    """Error handler"""
    return make_response(jsonify({'error': 'Not found'}), 404)

if __name__ == "__main__":
    app.run(host=os.getenv('HBNB_API_HOST', '0.0.0.0'),
            port=int(os.getenv('HBNB_API_PORT', '5000')))
