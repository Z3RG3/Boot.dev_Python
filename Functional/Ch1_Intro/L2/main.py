"""

?What Is Functional Programming, - Declarative? Opposed to OOP, Imperative
Functional programming is a style (or "paradigm" if you're pretentious) of programming where we compose functions instead of mutating state (updating the value of variables).

Functional programming is more about declaring what you want to happen, rather than how you want it to happen.
Imperative (or procedural) programming declares both the what and the how.


best source: https://en.wikipedia.org/wiki/Programming_paradigm

A programming paradigm is a relatively high-level way to conceptualize and structure the implementation of a computer program. A programming language can be classified as supporting one or more paradigms.[1]

Paradigms are separated along and described by different dimensions of programming. Some paradigms are about implications of the execution model, such as allowing side effects, or whether the sequence of operations is defined by the execution model. Other paradigms are about the way code is organized, such as grouping into units that include both state and behavior. Yet others are about syntax and grammar.

Some common programming paradigms include (shown in hierarchical relationship):[2][3][4]

!Imperative – code directly controls execution flow and state change, explicit statements that change a program state
    *procedural – organized as procedures that call each other
    *object-oriented – organized as objects that contain both data structure and associated behavior, uses data structures consisting of data fields and methods together with their interactions (objects) to design programs
        -Class-based – object-oriented programming in which inheritance is achieved by defining classes of objects, versus the objects themselves
        -Prototype-based – object-oriented programming that avoids classes and implements inheritance via cloning of instances

?Declarative – code declares properties of the desired result, but not how to compute it, describes what computation should perform, without specifying detailed state changes
    *functional – a desired result is declared as the value of a series of function evaluations, uses evaluation of mathematical functions and avoids state and mutable data
    *logic – a desired result is declared as the answer to a question about a system of facts and rules, uses explicit mathematical logic for programming
    *reactive – a desired result is declared with data streams and the propagation of change
"""


def stylize_title(document):
    pass


# Don't touch below this line


def center_title(document):
    width = 40
    title = document.split("\n")[0]
    centered_title = title.center(width)
    return document.replace(title, centered_title)


def add_border(document):
    title = document.split("\n")[0]
    border = "*" * len(title)
    return document.replace(title, title + "\n" + border)
