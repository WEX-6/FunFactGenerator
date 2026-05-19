# TASK P4.6

from flask import jsonify
from database import get_categories

def get_categories_route():
    categories = None # TODO: Get the categories from the database
    return jsonify({"categories": categories})
