# Tasks P1.1, P3.1, P4.3

from fact import Fact
from .provider import SQLiteConnectionProvider

# TODO: (Task P1.1) Add fact_text parameter
# TODO: (Task P4.3) Add category parameter
def create_fact() -> Fact:
    provider = SQLiteConnectionProvider()
    with provider.cursor() as cur:
        # TODO: (Task P1.1) Write SQL query to add new fact to the database
        # TODO: (Task P3.1) Add likes and dislikes counts to SQL query
        # TODO: (Task P4.3) Add category to SQL query
        cur.execute()
        result = cur.fetchone()
        provider.commit()
        # TODO: (Task P1.1) Create and return a Fact object using the data from the database result
        # TODO: (Task P3.1) Add likes and dislikes counts to the Fact object
        # TODO: (Task P4.3) Add category to returned fact
        return Fact()