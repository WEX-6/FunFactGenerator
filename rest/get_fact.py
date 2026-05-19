# Tasks P0.2, P4.5

from flask import render_template, jsonify, request
from database import get_fact

def get_route():
    retrievedCategory = None # TODO: (Task P4.5) Get category from query parameters if provided, or set to None if not provided

    # TODO: (Task P0.2) Call database function to get a random fact
    # TODO: (Task P4.5) Pass in category argument
    fact = None

    # Check if the client wants JSON response based on query parameters
    wants_json = request.args.get("json") in ("1", "true", "True")

    if wants_json:
        return jsonify({
            "id": getattr(fact, "id", None),
            "fact": fact.fact,
            # TODO: (Task P4.5) Add category
            "likes": getattr(fact, "likes", 0),
            "dislikes": getattr(fact, "dislikes", 0) 
        })
    # Render the HTML template and pass the fact data to it
    # TODO: (Task P4.5) Add category data
    return render_template(
        "generate.html",
        None, # TODO: (Task P0.2) Update here (where None) to pass the fact data to the template
        None, 
        None,
        None
    )
