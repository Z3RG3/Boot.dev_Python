# Methods vs. Functions
You know what a function is, and a method is the exact same thing, it's just tied directly to a class and has access to the properties of the object.

## A method automagically receives the object it was called on as its first parameter:

class Soldier:
    health = 100

    def take_damage(self, damage, multiplier):
        # "self" is dalinar in the first example
        #
        damage = damage * multiplier
        self.health -= damage

dalinar = Soldier()
# "damage" and "multiplier" are passed explicitly as arguments
# 20 and 2, respectively
# "dalinar" is passed implicitly as the first argument, "self"
dalinar.take_damage(20, 2)
print(dalinar.health)
# 60

adolin = Soldier()
# Again, "adolin" is passed implicitly as the first argument, "self"
# "damage" and "multiplier" are passed explicitly as arguments
adolin.take_damage(10, 3)
print(adolin.health)
# 70

A method can operate on data that is contained within the class. In other words, you won't always see all the "outputs" in the return statement because the method might just mutate the object's properties directly.

The OOP Debate
Because functions are more explicit, some developers argue that functional programming is better than object-oriented programming. Neither paradigm is "better" (I'm required to say this as an educator). The best developers learn and understand both styles and use them as they see fit.

While methods are more implicit (an object's properties are changed from within), they also make it easier to group a program's data and behavior in one place, which can lead to a more organized codebase. It's tradeoffs all the way down.


# Constructors
I have a confession... I've been teaching you the bad way to define properties on a class... oopsie!

It's rare in the real world to see a class that defines properties like this (as we did):

    class Soldier:
        name = "Legolas"
        armor = 2
        num_weapons = 2

A constructor is (usually) better. It's a specific method on a class called __init__ that is called automatically when you create a new instance of a class.

So, using a constructor, the code from above would look like this:

    class Soldier:
        def __init__(self):
            self.name = "Legolas"
            self.armor = 2
            self.num_weapons = 2

Not only is this safer (we'll talk about why later), but it also allows us to make the starting property values configurable:

    class Soldier:
        def __init__(self, name, armor, num_weapons):
            self.name = name
            self.armor = armor
            self.num_weapons = num_weapons

soldier_one = Soldier("Legolas", 5, 10)
print(soldier_one.name)
# prints "Legolas"
print(soldier_one.armor)
# prints "5"
print(soldier_one.num_weapons)
# prints "10"

soldier_two = Soldier("Gimli", 2, 1)
print(soldier_two.name)
# prints "Gimli"
print(soldier_two.armor)
# prints "2"
print(soldier_two.num_weapons)
# prints "1"