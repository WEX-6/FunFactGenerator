# Task P3.1

from fact import Fact
from .provider import SQLiteConnectionProvider
from .helpers.database_helpers import fetch_fact_data

def vote_fact(fact_id: int, vote_type: str) -> Fact:
    provider = SQLiteConnectionProvider()
    with provider.cursor() as cur:
        if vote_type == "like":
            cur.execute() # TODO: Write the SQL query to update the likes count for the given fact_id
        elif vote_type == "dislike":
            cur.execute() # TODO: Write the SQL query to update the dislikes count for the given fact_id
        else:
            raise ValueError("Invalid vote type")

        cur.execute() # TODO: Write the SQL query to retrieve the updated fact details for the given fact_id

        fact_data = fetch_fact_data(cur)
        provider.commit()
        if fact_data:
            return Fact(
                id=fact_data.id,
                fact=None,   # TODO: Create and return a Fact object using the retrieved data
                category=None,
                likes=0,     # TODO: Include the updated likes count
                dislikes=0   # TODO: Include the updated dislikes count
            )

        # TODO: Raise an error if the fact result does not exist in the database
        return
            