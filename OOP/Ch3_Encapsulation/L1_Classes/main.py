"""
#! Encapsulation
# * Encapsulation is the practice of hiding complexity inside a "black box"
# * so that it's easier to focus on the problem at hand.

The simplest example of encapsulation is a function. The caller of a function doesn't need to worry too much about what happens inside, they just need to understand the inputs and outputs.

# who even knows how this function works???
# I sure don't, I just call it and assume
# it calculates the acceleration correctly
acceleration = calc_acceleration(initial_speed, final_speed, time)

To use the calc_acceleration function, we don't need to think about each line of code inside the function definition. We just need to know that if we give it the inputs:

initial_speed
final_speed
time
It will produce the correct acceleration as an output.

Public and Private
By default, all properties and methods in a class are public. That means that you can access them with the . operator:

wall.height = 10
print(wall.height)
# 10

Private data members are a way to encapsulate logic and data within a class definition. To make a property or method private just prefix it with two underscores:

class Wall:
    def __init__(self, armor, magic_resistance):
        self.__armor = armor
        self.__magic_resistance = magic_resistance

    def get_defense(self):
        return self.__armor + self.__magic_resistance

front_wall = Wall(10, 20)

# This results in an error
print(front_wall.__armor)

# This works
print(front_wall.get_defense())
# 30

We do this to make it easier to use our class. Now when another developer (or even ourselves) use the Wall class, they don't need to think about how armor and magic_resistance affect the defense of a Wall. In fact, we don't even allow them to access armor and magic_resistance directly by making them private with __.

They simply call the public get_defense() method and know that the correct value will be returned.

?Assignment
Complete the Wizard class's constructor.

Set 2 private properties (be sure to include the private __ prefix):
stamina
intelligence
Set 3 public properties:
name: Use the value passed into the constructor
health: 100x the value of "stamina"
mana: 10x the value of "intelligence"
"""


class Wizard:
    def __init__(self, name, stamina, intelligence):
        self.name = name
        self.health = stamina * 100
        self.mana = intelligence * 10
        # __ means private
        self.__stamina = stamina
        self.__intelligence = intelligence


"""Not Security
Encapsulation is all about making code easy to work with by "hiding" complicated code within a "black box". It makes it so that we don't have to worry about details of how a function or method works... we just use it.

It's kinda like how the inner workings of your car's power steering are hidden from you. You don't need to be an expert on hydraulic systems to turn the wheel from side to side.

Let me say this next part loud and clear:

Encapsulation and the concepts of private and public members have NOTHING to do with security. This really confused me as a new developer. 
Just as the casing on your computer hides its inner workings but doesn't stop you from opening the case and looking inside,
encapsulation doesn't stop anyone from knowing how your code works, it just puts it all in one easy to find place.

Encapsulation is about organization, not security.

Encapsulation is like storing folders in an unlocked filing cabinet. The cabinet doesn't stop anyone from peeking inside, but it does keep everything tidy and easy to find.


Encapsulation in Python
Python is a very dynamic language, which makes it difficult for the interpreter to enforce some of the safeguards that languages like Go do. That's why encapsulation in Python is achieved mostly by convention rather than by force.

Prefixing methods and properties with a double underscore is a strong suggestion to the users of your class that they shouldn't be touching that stuff. If a developer wants to break convention, there are ways to get around the double underscore rule.
"""


class Wall:
    def __init__(self, height):
        # the double underscore make this a private property
        # but it's not strictly enforced, there are hacks to get around it
        self.__height = height

    def get_height(self):
        return self.__height
