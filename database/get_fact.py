# Tasks P0.1, P3.1, P4.2, P5.1, P5.2

from typing import List, Optional
from fact import Fact
from .provider import SQLiteConnectionProvider
from .helpers.database_helpers import fetch_fact_data

# TODO: (Task P5.1) Add optional category parameter to function definition
def get_fact() -> Fact:
    provider = SQLiteConnectionProvider()
    with provider.cursor() as cur:
        # TODO: (Task P5.1) Use the category parameter to optionally filter the random fact query
        # TODO: (Task P0.1) Write SQL query to select a random fact from the database
        cur.execute("") # SQL query goes here
        # TODO: (Task P3.1) Add the likes and dislikes counts to the SQL query
        # TODO: (Task P4.2) Add the category column to the SQL query
        fact_data = fetch_fact_data(cur)
        if not fact_data:
            return Fact(id=None, fact="", category=None, likes=0, dislikes=0) # TODO: (Task P0.1) Create and return an empty Fact object if no result is found

        # TODO: (Task P0.1) Create and return a Fact object using the data from the database result
        # TODO: (Task P3.1) Add the likes and dislikes counts to the Fact object
        # TODO: (Task P4.2) Add the category information
        return Fact(
            id=fact_data.id,
            fact=None,     # TODO: (Task P0.1) Add parsed fact text
            likes=0,       # TODO: (Task P3.1) Add parsed likes count
            dislikes=0,    # TODO: (Task P3.1) Add parsed dislikes count
            category=None  # TODO: (Task P4.2) Add parsed category
        )

def get_facts_by_category() -> List[str]:
    provider = SQLiteConnectionProvider()
    with provider.cursor() as cur:
        cur.execute("") # TODO: (Task P5.2) Write SQL query to get distinct facts by category from the database
        rows = cur.fetchall()
        return [row[0] for row in rows]
