"""
!Abstraction
*Abstraction helps us handle complexity by hiding unnecessary details.

... which sounds just like encapsulation, right? To be honest, the ideas are so similar that it's almost not worth worrying about the difference...almost.

Abstraction vs. Encapsulation
Abstraction is about creating a simple interface for complex behavior. It focuses on what's exposed (public).
Encapsulation is about hiding internal state. It focuses on tucking away the implementation details (private).
Abstraction is more about reducing complexity, encapsulation is more about maintaining the integrity of system internals.

In my personal opinion, it's a bit of a distinction without a difference... but "abstraction" is a more broadly used term, and in my view at least, it's also a more general term for "making something easier to use by adding a layer on top".

Are We Encapsulating or Abstracting?
Both. We are almost always doing both. Here's an example of using the random library to generate a random number:

import random

attack_damage = random.randrange(5)

Generating random numbers is a really hard problem. The operating system uses the physical hardware of the computer to create a seed for the randomness. However, the developers of the random library have abstracted that complexity away and encapsulated it within the simple randrange function. We just say "I want a random number from 0 to 4" and the library does it.

When writing libraries for other developers to use, getting the abstractions right is critical because changing them later can be disastrous. Imagine if the maintainers of the random module changed the input parameters to the randrange function! It would break code used by thousands of applications around the world.

?Assignment
We don't want our coworkers at Age of Dragons Studios™ to have to worry about how Humans move. We'll abstract that away from them by encapsulating the private __pos_x, __pos_y, and __speed variables behind some simple methods.

Complete the following methods in the Human class:

move_right(): Adds the human's speed to its x position.
move_left(): Subtracts the human's speed from its x position.
move_up(): Adds the human's speed to its y position.
move_down(): Subtracts the human's speed from its y position.
get_position(): Returns the x position and y position as a tuple."""


class Human:
    def __init__(self, pos_x, pos_y, speed):
        self.__pos_x = pos_x
        self.__pos_y = pos_y
        self.__speed = speed

    def move_right(self):
        self.__pos_x += self.__speed

    def move_left(self):
        self.__pos_x -= self.__speed

    def move_up(self):
        self.__pos_y += self.__speed

    def move_down(self):
        self.__pos_y -= self.__speed

    def get_position(self):
        return self.__pos_x, self.__pos_y


"""The terms "abstraction" and "encapsulation" mostly just emphasize different aspects of the same concept:

Abstraction focuses on exposing essential features while hiding complexity
Encapsulation focuses on bundling data with methods and restricting direct access to implementation details
they're the same

Creating good abstractions is particularly crucial when you're developing libraries for other developers to use. For example, the built-in pow function in Python is an abstraction that hides the complexity of calculating exponents.

pow isn't magic. Somewhere, code that does something like this exists and is called when you use pow:
"""


def pow(base, exponent):
    result = 1
    for _ in range(exponent):
        result *= base
    return result


"""
!How OOP Developers Think
Classes in object-oriented programming are all  about grouping data and behavior together in one place: an object. Object-oriented programmers tend to think about programming as a modeling problem. They think:

"How can I write a Human class that holds the data and simulates the behavior of a real human?"

To provide some contrast, when functional programmers aren't busy writing white papers, they tend to think of their code as inputs and outputs, and how those inputs and outputs transition the world from one state to the next:

"My game has 7 humans in it. When one takes a step, what's the next state of the game?"

oop vs fp

Both Paradigms Are Useful
OOP isn't the only pattern for organizing code, but it's one of the more popular ones. If you understand multiple ways of thinking about code, you'll be a much better developer overall.
    """
