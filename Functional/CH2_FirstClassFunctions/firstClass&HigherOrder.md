# First Class and Higher Order Functions
---

A programming language "supports first-class functions" when functions are treated like any other variable. That means functions can be passed as arguments to other functions, can be returned by other functions, and can be assigned to variables.

### 1. First-class function:
**A function that is treated like any other value**

### 2. Higher-order function:
 **A function that accepts another function as an argument or returns a function**
**Python supports first-class and higher-order functions.**

```
First-Class Example```
def square(x):
    return x * x

Assign function to a variable
f = square

print(f(5))
# 25

Higher-Order Example
def square(x):
    return x * x

def my_map(func, arg_list):
    result = []
    for i in arg_list:
        result.append(func(i))
    return result

squares = my_map(square, [1, 2, 3, 4, 5])
print(squares)
# [1, 4, 9, 16, 25]

# and using lambda makes it even cooler

def my_map_withLambda( arg_list):
    result = []
    for i in arg_list:
        result.append(lambda i: i * i)
    return result

```



## Map
|
"Map", "filter", and "reduce" are three commonly used higher-order functions in functional programming.

In Python, the built-in map function takes a function and an iterable (in this case a list) as inputs. It returns an iterator that applies the function to every item, yielding the results.

**map** function
: **With map, we can operate on lists without using loops and nasty stateful variables.** For example:
```
def square(x):
    return x * x

nums = [1, 2, 3, 4, 5]
squared_nums = map(square, nums)
print(list(squared_nums))
# [1, 4, 9, 16, 25]
```
The list type constructor, list() converts the map object back into a standard list.

Assignment
Markdown supports two different styles of bullet points, - and *. We prefer *, so, we need a function to convert any - bullet points to * bullet points.

Complete the change_bullet_style function. It takes a document (a string) as input, and returns a single string as output. The returned string should have any lines that start with a - character replaced with a * character.

For example, this:

- This is a bullet
- This is a bullet

Becomes:

* This is a bullet
* This is a bullet

Use the built-in map function to apply the provided convert_line function to each line of the input string. Use .split() and .join() to split the document into a list of lines, and then join the lines back together. This should preserve the original line breaks. Don't use the .replace() string method.

Examples of split and join:

```
# my_document is a string with newlines
lines_list = my_document.split("\n")

rejoined_doc = "\n".join(lines_list)


def change_bullet_style(document):
    lines = document.split("\n")
    processed_lines = map(convert_line, lines)
    return "\n".join(processed_lines)
    
def change_bullet_styleV2(document):
    return "\n".join(map(convert_line, document.split("\n")))       # WOOOO   !!!!!


# Don't edit below this line


def convert_line(line):
    old_bullet = "-"
    new_bullet = "*"
    if len(line) > 0 and line[0] == old_bullet:
        return new_bullet + line[1:]
    return line
```

## Filter

**The built-in filter function takes a function and an iterable (in this case a list) and returns an iterator that only contains elements from the original iterable where the result of the function on that item returned True.**

![Filter function](FfVxD7d.png)

In Python:
```
def is_even(x):
    return x % 2 == 0

numbers = [1, 2, 3, 4, 5, 6]
evens = list(filter(is_even, numbers))
print(evens)
# [2, 4, 6]
```

### Assignment

Complete the remove_invalid_lines function. It accepts a document as input. It should:

Use the built-in filter function and a lambda to return a copy of the input document
Remove any lines that start with a - character.
Keep all other lines and preserve trailing newlines.
For example, this:

* Star Wars episode 1 is underrated
- Star Wars episode 9 is fine
* Star Wars episode 3 is the best


Should become:

* Star Wars episode 1 is underrated
* Star Wars episode 3 is the best


Tips
The splitlines method does not preserve trailing newlines and may cause your output to fail the tests.

The following methods may be useful:

```
.join

"\n".join(["a", "b", "c"])
# a
# b
# c

.startswith

s = "hello"
s.startswith("h")
# True
s.startswith("o")
# False

.split

s = """hello
world"""
lines = s.split("\n")
# ['hello', 'world']
```

## SOLUTION:
'''
   def remove_invalid_lines(document):
        return "\n".join(
            filter(lambda x: not x.startswith("-"), document.split("\n"))
        )

run_cases = [
    (
        "\n* We are the music makers\n- And we are the dreamers of dreams\n* Come with me and you'll be\n",
        "\n* We are the music makers\n* Come with me and you'll be\n",
    ),
    (
        "\n* In a world of pure imagination\n- There is no life I know\n* Living there - you'll be free\n",
        "\n* In a world of pure imagination\n* Living there - you'll be free\n",
    ),
]
'''
---------------------------------
Input document:
"
* We are the music makers
- And we are the dreamers of dreams
* Come with me and you'll be
"
Expected output:
"
* We are the music makers
* Come with me and you'll be
"
Actual output:
"
* We are the music makers
* Come with me and you'll be
"
Pass
---------------------------------
Input document:
"
* In a world of pure imagination
- There is no life I know
* Living there - you'll be free
"
Expected output:
"
* In a world of pure imagination
* Living there - you'll be free
"
Actual output:
"
* In a world of pure imagination
* Living there - you'll be free
"
Pass
============= PASS ==============
2 passed, 0 failed, 1 skipped