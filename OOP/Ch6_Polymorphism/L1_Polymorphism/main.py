""" "
While inheritance is the most unique trait of object-oriented languages, polymorphism is probably the most powerful.
 It also is not particularly unique to class-based languages. Polymorphism is the ability of a variable,
function or object to take on multiple forms.

!    poly" = "many"
!   "morph" = "form"

For example, classes in the same hierarchical tree may have methods with the same name and signature but different implementations.
 Here's a simple example:"""


class Creature:
    def move(self):
        print("the creature moves")


class Dragon(Creature):
    def move(self):
        print("the dragon flies")


class Kraken(Creature):
    def move(self):
        print("the kraken swims")


for creature in [Creature(), Dragon(), Kraken()]:  # !!!!!!! LOOK here
    creature.move()  # <----- this is working because of polymorphism
# prints:
# the creature moves
# the dragon flies
# the kraken swims

# ? Because all three classes have a .move() method, we can shove the objects into a single list, and call the same method on each of them, even though the implementation (method body) is different.


class Rectangle:
    def __init__(self, x1, y1, x2, y2):
        self.x1, self.y1, self.x2, self.y2 = x1, y1, x2, y2
