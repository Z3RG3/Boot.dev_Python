Anonymous Functions
Anonymous functions have no name, and in Python, they're called lambda functions after lambda calculus. Here's a lambda function that takes a single argument x and returns the result of x + 1:

`lambda x: x + 1`

Notice that the expression x + 1 is returned automatically, no need for a return statement. And because functions are just values, we can assign the function to a variable named add_one:

`add_one = lambda x: x + 1`
`print(add_one(2))`
`# 3`

!Lambda functions might look scary, but they're still just functions. Because they simply return the result of an expression, they're often used for small, simple evaluations. Here's an example that uses a lambda to get a value from a dictionary:

```
get_age = lambda name: {
    "lane": 29,
    "hunter": 69,
    "allan": 17
}.get(name, "not found")
print(get_age("lane"))
# 29
```

Assignment
Complete the file_type_getter function. This function accepts a list of tuples, where each tuple contains:

A "file type" (e.g. "code", "document", "image", etc)
A list of associated file extensions (e.g. [".py", ".js"] or [".docx", ".doc"])
First, use loops to create a dictionary that maps each file extension to its corresponding file type, based on the input tuples. For example, the resulting dictionary might be:
```
{
    ".doc": "text",
    ".docx": "document",
    ".py": "code",
    ".jpg": "image"
}
```!
Next, return a lambda function that accepts a string (a file extension) and returns the corresponding file type. If the extension is not found in the dictionary, the lambda function should return "Unknown". I used the .get dictionary method to handle this.
```
def file_type_getter(file_extension_tuples):
    lambda extension: {
        ".doc": "text",
    ".docx": "document",
    ".py": "code",
    ".jpg": "image"
    }.get


my solution:
def file_type_getter(file_extension_tuples):
    file_extensions_dict = {}
    for tup in file_extension_tuples:
        for ext in tup[1]:
            file_extensions_dict[ext] = tup[0]
    return lambda ext: file_extensions_dict.get(ext, "Unknown")



file_extension_tuples = [
    (
        [("document", [".doc", ".docx"]), ("image", [".jpg", ".png"])],
        ".doc",
        "document",
    ),
    (
        [("document", [".doc", ".docx"]), ("image", [".jpg", ".png"])],
        ".png",
        "image",
    ),
    (
        [("document", [".doc", ".docx"]), ("image", [".jpg", ".png"])],
        ".txt",
        "Unknown",
    ),
    (
        [("code", [".py", ".js"]), ("markup", [".html", ".xml"])],
        ".js",
        "code",
    ),
]
```