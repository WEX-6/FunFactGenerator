# Task P4.4

class Fact:
    def __init__(self, id: int, fact: str, category: str = None, likes: int = 0, dislikes: int = 0):
        self.id = id
        self.fact = fact
        self.likes = likes
        self.dislikes = dislikes
        # TODO: Store category information as an instance variable

    def __repr__(self):
        return f"<Fact id={self.id} fact='{self.fact}' likes={self.likes}, dislikes={self.dislikes}" # TODO: Add category information to the string representation
