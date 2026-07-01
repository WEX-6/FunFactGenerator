# Task P3.2

from flask import request
from rest.helpers.rest_helpers import json_response

def vote_route():
    data = request.json
    # TODO: Extract fact_id from the JSON data
    # TODO: Extract vote_type from the JSON data

    try:
        # TODO: Call the vote_fact function to get the updated fact details after voting

        # TODO: Determine the new count based on the vote type

        # TODO: Create the response JSON with fact_id, new_count, likes, and dislikes
        response = {}
        return json_response(response, 200)  # Return the JSON response with status code 200 for successful vote
    except ValueError as err: # Catch the ValueError raised by vote_fact for invalid vote types
        return json_response(str(err), 400)  # Return the error message with status code 400 for invalid vote type