# Most Important Python Built-in Functions

This notebook covers the most commonly used and important Python built-in functions to help you understand their purpose and usage.

## Object-Oriented Programming

### `super()`
**Purpose**: Allows you to call methods from a parent class in your child class.  
**Usage**: Primarily used in inheritance to access parent class methods and attributes.

```python
class Parent:
    def __init__(self, name):
        self.name = name
        
class Child(Parent):
    def __init__(self, name, age):
        super().__init__(name)  # Calls Parent's __init__
        self.age = age
        
# Example
child = Child("Alice", 10)
print(f"Name: {child.name}, Age: {child.age}")
```

## Type Conversion

### `int()`, `float()`, `str()`, `bool()`
**Purpose**: Convert values between basic data types.

```python
# Examples of type conversion
print(int("42"))         # 42
print(float("3.14"))     # 3.14
print(str(42))           # "42"
print(bool(0))           # False
print(bool(1))           # True
print(bool(""))          # False
print(bool("hello"))     # True
```

## Collections and Sequences

### `len()`
**Purpose**: Returns the number of items in a container (list, tuple, string, etc.)

```python
# Examples of len()
print(len([1, 2, 3]))    # 3
print(len("hello"))      # 5
print(len({"a": 1, "b": 2}))  # 2
```

### `range()`
**Purpose**: Creates a sequence of numbers, commonly used in loops.

```python
# Examples of range()
for i in range(5):  # 0, 1, 2, 3, 4
    print(i, end=" ")
    
print("\n---")

# start, stop
for i in range(2, 6):  # 2, 3, 4, 5
    print(i, end=" ")
    
print("\n---")

# start, stop, step
for i in range(1, 10, 2):  # 1, 3, 5, 7, 9
    print(i, end=" ")
```

### `list()`, `tuple()`, `set()`, `dict()`
**Purpose**: Create new collections or convert between collection types.

```python
# Examples of collection constructors
print(list("abc"))              # ['a', 'b', 'c']
print(tuple([1, 2, 3]))         # (1, 2, 3)
print(set([1, 2, 2, 3]))        # {1, 2, 3}
print(dict([(1, 'a'), (2, 'b')]))  # {1: 'a', 2: 'b'}

# Creating empty collections
empty_list = list()
empty_tuple = tuple()
empty_set = set()  # Note: {} creates an empty dict, not set
empty_dict = dict()
```

## List Operations

### `sorted()`
**Purpose**: Returns a new sorted list from an iterable.

```python
# Examples of sorted()
print(sorted([3, 1, 2]))        # [1, 2, 3]
print(sorted("cab"))            # ['a', 'b', 'c']
print(sorted({"b": 1, "a": 2})) # ['a', 'b'] (sorts the keys)

# Custom sort with key function
print(sorted(["apple", "banana", "cherry"], key=len))  # Sorts by length
```

### `map()`
**Purpose**: Applies a function to each item in an iterable.

```python
# Examples of map()
numbers = [1, 2, 3, 4]
squared = map(lambda x: x**2, numbers)
print(list(squared))  # [1, 4, 9, 16]

# With multiple iterables
a = [1, 2, 3]
b = [10, 20, 30]
added = map(lambda x, y: x + y, a, b)
print(list(added))  # [11, 22, 33]
```

### `filter()`
**Purpose**: Filters elements from an iterable based on a function.

```python
# Examples of filter()
numbers = [1, 2, 3, 4, 5, 6]
even = filter(lambda x: x % 2 == 0, numbers)
print(list(even))  # [2, 4, 6]

names = ["Alice", "Bob", "Charlie", "Dave"]
long_names = filter(lambda name: len(name) > 4, names)
print(list(long_names))  # ['Alice', 'Charlie']
```

## Input/Output

### `print()`
**Purpose**: Outputs data to the console.

```python
# Examples of print()
print("Hello", "world")  # Hello world
print("Hello", "world", sep=", ")  # Hello, world
print("Hello", end=" ")
print("world")  # Hello world

# Formatting
name = "Alice"
age = 30
print(f"{name} is {age} years old")  # Alice is 30 years old
```

### `input()`
**Purpose**: Reads a line from the console.

```python
# Example of input()
# Uncomment to run interactively
# name = input("Enter your name: ")
# print(f"Hello, {name}!")
```

### `open()`
**Purpose**: Opens a file and returns a file object.

```python
# Examples of open()
# Write to a file
with open("example.txt", "w") as f:
    f.write("Hello, world!")

# Read from a file
with open("example.txt", "r") as f:
    content = f.read()
    print(content)  # Hello, world!
```

## Inspection and Reflection

### `type()`
**Purpose**: Returns the type of an object.

```python
# Examples of type()
print(type(42))        # <class 'int'>
print(type("hello"))   # <class 'str'>
print(type([1, 2, 3]))  # <class 'list'>

# Check if two types are the same
print(type(42) == int)  # True
```

### `isinstance()`
**Purpose**: Checks if an object is an instance of a class.

```python
# Examples of isinstance()
print(isinstance(42, int))     # True
print(isinstance("hello", str))  # True
print(isinstance("hello", int))  # False

# Check multiple types
print(isinstance(42, (int, float)))  # True
print(isinstance(3.14, (int, float)))  # True
```

### `dir()`
**Purpose**: Lists attributes and methods of an object.

```python
# Examples of dir()
print(dir(str))  # Shows all string methods

s = "hello"
methods = [method for method in dir(s) if not method.startswith('__')]
print(methods[:5])  # First 5 string methods
```

### `help()`
**Purpose**: Shows help documentation for an object.

```python
# Examples of help()
# Uncomment to see full help
# help(str.split)  # Shows documentation for the split method

# Instead of full help, here's a demonstration of what help provides
print("help() would show that str.split splits a string by whitespace or a delimiter")
```

## Mathematical Functions

### `min()`, `max()`
**Purpose**: Returns the smallest/largest item from an iterable or arguments.

```python
# Examples of min() and max()
print(min(1, 2, 3))     # 1
print(max([1, 2, 3]))   # 3

# With a key function
words = ["apple", "banana", "cherry"]
print(min(words, key=len))  # "apple" (shortest)
print(max(words, key=len))  # "banana" (longest)
```

### `sum()`
**Purpose**: Sums the items of an iterable.

```python
# Examples of sum()
print(sum([1, 2, 3]))   # 6
print(sum([0.1, 0.2, 0.3]))  # 0.6000000000000001 (floating point precision)
print(sum([[1], [2], [3]], []))  # [1, 2, 3] (with start value [])
```

### `abs()`
**Purpose**: Returns the absolute value of a number.

```python
# Examples of abs()
print(abs(-5))          # 5
print(abs(3.14))        # 3.14
print(abs(-3.14))       # 3.14
```

### `round()`
**Purpose**: Rounds a number to a specified precision.

```python
# Examples of round()
print(round(3.14159))        # 3 (rounds to nearest integer)
print(round(3.14159, 2))     # 3.14 (rounds to 2 decimal places)
print(round(3.5))            # 4 (rounds to even value when tie)
print(round(4.5))            # 4 (rounds to even value when tie)
```

## Memory Management

### `id()`
**Purpose**: Returns the memory address of an object.

```python
# Examples of id()
x = [1, 2, 3]
y = x      # Same object
z = [1, 2, 3]  # Different object with same value

print(id(x))
print(id(y))  # Same as id(x)
print(id(z))  # Different from id(x)
print(x is y)  # True (same object)
print(x is z)  # False (different objects)
```

## Class and Object Construction

### `getattr()`, `setattr()`, `hasattr()`
**Purpose**: Get, set, or check for attributes on objects.

```python
# Examples of attribute functions
class Person:
    def __init__(self, name):
        self.name = name

p = Person("Alice")

print(hasattr(p, 'name'))    # True
print(getattr(p, 'name'))    # Alice

setattr(p, 'age', 30)
print(hasattr(p, 'age'))     # True
print(getattr(p, 'age'))     # 30

# Default value if attribute doesn't exist
print(getattr(p, 'height', 170))  # 170
```

### `property()`
**Purpose**: Creates managed attributes (getters, setters).

```python
# Example of property()
class Person:
    def __init__(self):
        self._age = 0
        
    def get_age(self):
        return self._age
        
    def set_age(self, value):
        if value < 0:
            raise ValueError("Age cannot be negative")
        self._age = value
        
    age = property(get_age, set_age)

p = Person()
p.age = 25  # Uses set_age
print(p.age)  # Uses get_age

try:
    p.age = -10  # Raises ValueError
except ValueError as e:
    print(f"Error: {e}")

# Alternative decorator syntax
class Person2:
    def __init__(self):
        self._age = 0
        
    @property
    def age(self):
        return self._age
        
    @age.setter
    def age(self, value):
        if value < 0:
            raise ValueError("Age cannot be negative")
        self._age = value
```

## Execution and Environment

### `eval()`, `exec()`
**Purpose**: Execute Python expressions or statements from strings (use with caution).

```python
# Examples of eval() and exec()
result = eval("1 + 2")
print(result)  # 3

math_expr = "10 * 3 + 5"
print(eval(math_expr))  # 35

# exec() for statements
exec("x = 1 + 2")
print(x)  # 3

code = """
y = 10
for i in range(3):
    y += i
"""
exec(code)
print(y)  # 13 (10+0+1+2)
```

### `globals()`, `locals()`
**Purpose**: Return dictionaries of the global and local symbol tables.

```python
# Examples of globals() and locals()
x = 10

def test_func():
    y = 20
    print("Locals:", locals())
    print("y from locals:", locals()['y'])
    print("x from globals:", globals()['x'])

test_func()
print("Globals has x:", 'x' in globals())
```

## Practice Exercises

```python
# Exercise 1: Create a function that uses super()
class Animal:
    def __init__(self, name):
        self.name = name
    
    def speak(self):
        return "Some sound"

class Dog(Animal):
    def __init__(self, name, breed):
        # TODO: Use super() to call the parent's __init__
        # Your code here
        
    def speak(self):
        # TODO: Return "Woof!" instead
        # Your code here

# Exercise 2: Use map and filter together
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# TODO: Use filter to keep only even numbers and map to square them
# Your code here

# Exercise 3: Create a class with a property
# TODO: Create a Temperature class with a celsius property 
# that converts to fahrenheit when accessed with .fahrenheit
# Your code here
```

## Solutions to Exercises

```python
# Solution 1
class Animal:
    def __init__(self, name):
        self.name = name
    
    def speak(self):
        return "Some sound"

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed
        
    def speak(self):
        return "Woof!"

dog = Dog("Rex", "German Shepherd")
print(f"{dog.name} is a {dog.breed} and says {dog.speak()}")

# Solution 2
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = list(map(lambda x: x**2, filter(lambda x: x % 2 == 0, numbers)))
print(result)  # [4, 16, 36, 64, 100]

# Solution 3
class Temperature:
    def __init__(self, celsius=0):
        self._celsius = celsius
        
    @property
    def celsius(self):
        return self._celsius
        
    @celsius.setter
    def celsius(self, value):
        self._celsius = value
        
    @property
    def fahrenheit(self):
        return (self.celsius * 9/5) + 32
        
    @fahrenheit.setter
    def fahrenheit(self, value):
        self.celsius = (value - 32) * 5/9

temp = Temperature(25)
print(f"{temp.celsius}°C is {temp.fahrenheit}°F")
temp.fahrenheit = 68
print(f"{temp.celsius}°C is {temp.fahrenheit}°F")
```

These functions form the foundation of Python programming, and understanding them well will significantly improve your Python skills. As you progress, you'll naturally learn how and when to apply each one effectively.