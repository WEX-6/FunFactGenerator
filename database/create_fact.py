# Tasks P1.1, P3.1, P4.3

from fact import Fact
from .provider import SQLiteConnectionProvider
from .helpers.database_helpers import fetch_fact_data

# TODO: (Task P1.1) Add fact_text parameter
# TODO: (Task P4.3) Add category parameter
def create_fact() -> Fact:
    provider = SQLiteConnectionProvider()
    with provider.cursor() as cur:
        # TODO: (Task P1.1) Write SQL query to add new fact to the database
        # TODO: (Task P3.1) Add likes and dislikes counts to SQL query
        # TODO: (Task P4.3) Add category to SQL query
        cur.execute("") # SQL query goes here
        fact_data = fetch_fact_data(cur)
        provider.commit()
        if not fact_data:
            return Fact(id=None, fact="", category=None, likes=0, dislikes=0) # TODO: (Task P1.1) Create and return an empty Fact object if no result is found
        
        return Fact(
            id=fact_data.id,
            fact= None,   # TODO: (Task P1.1) Create and return a Fact object using the data from the database result
            likes=0,      # TODO: (Task P3.1) Add likes and dislikes counts to the Fact object
            dislikes=0,   
            category=None # TODO: (Task P4.3) Add category to returned fact
        )