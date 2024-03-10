#!/usr/bin/python3
"""
Web server
"""
from api.v1.views import app_views
from flask import Flask, jsonify, make_response

app = Flask(__name__)
app.register_blueprint(app_views)


@app.errorhandler(404)
def not_found(error):
    """ json 404 page """
    return make_response(jsonify({"error": "Not found"}), 404)

# Custom route handler to check if the endpoint exists
@app.route('/api/v1/status', methods=['GET'], strict_slashes=False)
def get_status():
    """ Get status endpoint """
    # Check if the endpoint exists
    endpoint_exists = True  # Placeholder for your condition to check if the endpoint exists

    if endpoint_exists:
        return jsonify({"status": "OK"})
    else:
        return not_found(None)


if __name__ == "__main__":
    # python -m api.v1.app
    app.run(host="0.0.0.0", port=5000)
