"""
Built in methods

__str__, __repr__ for printing or object type stuff.

? The __repr__ method works similarly: the difference is that it's intended for use in debugging by developers, rather than in printing strings to end users.


"""


class Dragon:
    def __init__(self, name, color):
        self.name = name
        self.color = color

    def __str__(self):
        return f"I am {self.name}, the {self.color} dragon"
