#!/usr/bin/python3
"""
AirBnB App
"""

from flask import Flask, jsonify
from api.v1.views import app_views
from models import storage
from os import getenv

app = Flask(__name__)
app.register_blueprint(app_views)


@app.errorhandler(404)
def error_404(error):
    """
    handle error
    """
    return(jsonify(error="Not found"), 404)


@app.teardown_appcontext
def remove_session(x=None):
    """
    remove the current session
    """
    storage.close()


if __name__ == '__main__':
    host = getenv("HBNB_API_HOST", "0.0.0.0")
    port = int(getenv("HBNB_API_PORT", 5000))
    app.run(host=host, port=port, threaded=True)
