# This file contains helper functions for converting database rows to Fact objects and fetching fact data from a database cursor. 
# It is not a task and can be ignored for the purpose of the tasks.

from fact import Fact

def row_to_fact(row, columns=None):
    """Converts a database row to a Fact object.

    Supports both mapping-style rows (e.g. sqlite3.Row) and tuple/list rows.
    Missing optional fields default to values that keep earlier worksheet tasks working.
    """
    def _empty_fact():
        return Fact(id=None, fact="", category=None, likes=0, dislikes=0)

    def _from_mapping(data):
        return Fact(
            id=data.get("id"),
            fact=data.get("fact", ""),
            category=data.get("category"),
            likes=(data.get("likes", 0) or 0),
            dislikes=(data.get("dislikes", 0) or 0),
        )

    if row is None:
        return _empty_fact()

    if hasattr(row, "keys"):
        return _from_mapping({key: row[key] for key in row.keys()})

    if columns and isinstance(row, (tuple, list)):
        return _from_mapping({name: value for name, value in zip(columns, row)})

    if isinstance(row, (tuple, list)):
        if len(row) == 5:
            return Fact(id=row[0], fact=row[1], category=row[2], likes=row[3] or 0, dislikes=row[4] or 0)
        if len(row) == 4:
            return Fact(id=row[0], fact=row[1], category=None, likes=row[2] or 0, dislikes=row[3] or 0)
        if len(row) >= 2:
            return Fact(id=row[0], fact=row[1], category=None, likes=0, dislikes=0)

    return _empty_fact()


def fetch_fact_data(cursor):
    """Fetches one row from a cursor and converts it into a Fact-shaped object.

    This hides row/column mapping details from student task files.
    """
    row = cursor.fetchone()
    if row is None:
        return None

    columns = [desc[0] for desc in cursor.description] if cursor.description else None
    return row_to_fact(row, columns)
