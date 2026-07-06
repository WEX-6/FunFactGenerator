# Tasks P0.2, P4.4, P5.3

from flask import render_template, jsonify, request
from database import get_fact

from rest.helpers.rest_helpers import wants_json, fact_to_json

def get_route():
    # TODO (TaskP5.3):  Get category from query parameters if provided, or set to None if not provided
    retrievedCategory = None

    # TODO (Task P0.2): Call database function to get a random fact
    fact = None

    if wants_json():
        return fact_to_json(fact) # Return the fact as JSON if requested
    # Render the HTML template and pass the fact data to it
    return render_template(
        "generate.html",
        None,  # TODO (P0.2): Replace 'None' with the fact variable to pass data to template
        None  # TODO (P4.4): Pass the category to the template
    )
    # TODO (P4.4): Determine what other data should be passed to the template
