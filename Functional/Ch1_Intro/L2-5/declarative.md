Why Python?
Frankly, Python is not the best language for functional programming. Reasons include:

No static typing.
(Almost) everything is mutable.
No tail call optimization.
Side effects are common.
Imperative and OOP styles abound in popular libraries.
Purity is not enforced (and sometimes not even encouraged).
Sum Types are hard to define.
Pattern matching is weak at best.

So seriously, why are we using Python? One reason trumps all others: you already know Python. Python is a great choice for learning coding basics,
OOP, Algorithms, and Data Structures, and the tradeoff of learning a new language at this point in the curriculum isn't worth it.

We can still cover the most important concepts of functional programming in Python, even if we have to jump through a hoop or two to do it.
!Functional programming is a paradigm of useful techniques for writing better code, and they apply to all languages, not just purely functional ones.


?Immutability
In FP, we strive to make data immutable. Once a value is created, it cannot be changed. Mutable data, on the other hand, can be changed after it's created.

Who Cares?
Immutable data is easier to think about and work with. When 10 different functions have access to the same variable, and you're debugging a problem with that variable, you have to consider the possibility that any of those functions could have changed the value.

When a variable is immutable, you can be sure that it hasn't changed since it was created. It's a helluva lot easier to work with.

Generally speaking, immutability means fewer bugs and more maintainable code.

Tuples vs. Lists
Tuples and lists are both ordered collections of values, but tuples are immutable and lists are mutable.

You can append to a list, but you can not append to a tuple. You can create a new copy of a tuple using values from an existing tuple, but you can't change the existing tuple.

*Declarative Programming

Functional programming aims to be declarative. We prefer to declare what we want the computer to do, rather than muck around with the details of how to do it.

Let's take an extreme example and pretend we wanted to style a webpage with CSS (Obviously a hypothetical because, well, why would anyone want to work on the frontend???)
