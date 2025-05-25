##First Class and Higher Order Functions
page 1
A programming language "supports first-class functions" when functions are treated like any other variable. That means functions can be passed as arguments to other functions, can be returned by other functions, and can be assigned to variables.

### 1. First-class function:
A function that is treated like any other value

### 2. Higher-order function:
 A function that accepts another function as an argument or returns a function
Python supports first-class and higher-order functions.

First-Class Example```
def square(x):
    return x * x

# Assign function to a variable
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

page 2

Map
"Map", "filter", and "reduce" are three commonly used higher-order functions in functional programming.

In Python, the built-in map function takes a function and an iterable (in this case a list) as inputs. It returns an iterator that applies the function to every item, yielding the results.

map function

With map, we can operate on lists without using loops and nasty stateful variables. For example:

def square(x):
    return x * x

nums = [1, 2, 3, 4, 5]
squared_nums = map(square, nums)
print(list(squared_nums))
# [1, 4, 9, 16, 25]

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