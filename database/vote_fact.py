# Task P3.1

from fact import Fact
from .provider import SQLiteConnectionProvider

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

        result = cur.fetchone()
        provider.commit()
        if result:
            return Fact() # TODO: Create and return a Fact object using the retrieved data
        else:
            return 
            # TODO: Raise an error if the fact result does not exist in the database
            