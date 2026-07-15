# TASKS P1.2, P4.5

from flask import render_template, request
from database import create_fact
from fact import Fact
def create_route():
    if request.method == "GET":
        # TODO: (Task P1.2) Render the create.html template
       return render_template("create.html")

    if request.method == "POST":

        # TODO: (Task P1.2) Get the fact_text from the form
        text = request.form.get("fact_text", "").strip()
        
        create_fact(text)

        # TODO: (Task P4.5) Get the category from the form

        # TODO: (Task P1.2) Check that fact text is provided, if not return an error
        if not text:
            return "Invalid Fact.", 400
        print(text)
        # TODO: (Task P1.2) Call the create_fact function from the database folder

        myFact = Fact(
            id=1234,
            fact= text,   # TODO: (Task P1.1) Create and return a Fact object using the data from the database result
            likes=7,      # TODO: (Task P3.1) Add likes and dislikes counts to the Fact object
            dislikes=9999,   
            category=None # TODO: (Task P4.3) Add category to returned fact
        )
        # TODO: (Task P4.5) Pass the category to the create_fact function

        return render_template(
            "create.html",
            random_fact=myFact,
            category=None,) # TODO: (Task P1.2) Pass the HTML template, fact and category (Task P4.5) parameters