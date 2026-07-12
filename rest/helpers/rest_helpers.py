# This file contains helper functions for the REST API routes. It is not a task and can be ignored for the purpose of the tasks.
from flask import request, jsonify


def wants_json():
    """Returns True if the client requested a JSON response via query parameter."""
    return request.args.get("json") in ("1", "true", "True")

def fact_to_json(fact):
    """Converts a Fact object to a JSON-serializable dictionary."""
    return {
        "id": getattr(fact, "id", None),
        "fact": getattr(fact, "fact", None),
        "category": getattr(fact, "category", None),
        "likes": getattr(fact, "likes", 0),
        "dislikes": getattr(fact, "dislikes", 0)
    }

def json_response(message, status_code=200):
    """Returns a JSON response with the given message and status code."""
    if isinstance(message, dict):
        return jsonify(message), status_code
    return jsonify({"message": message}), status_code
