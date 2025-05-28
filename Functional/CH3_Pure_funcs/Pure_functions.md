# Pure functions

If you take nothing else away from this course, please take this: Pure functions are fantastic. They have two properties:

They always return the same value given the same arguments.
Running them causes no side effects
In short: pure functions don't do anything with anything that exists outside of their scope.


Example of a Pure Function
```
def find_max(nums):
    max_val = float("-inf")
    for num in nums:
        if max_val < num:
            max_val = num
    return max_val
```
Example of an Impure Function
```
# instead of returning a value
# this function modifies a global variable
global_max = float("-inf")

def find_max(nums):
    global global_max
    for num in nums:
        if global_max < num:
            global_max = num
```
Assignment
There's a bug in the convert_file_format function! Right now, it relies on data outside its own scope. These global values can be changed by other parts of the code, so they are not guaranteed to be the same every time convert_file_format is called.

Fix the bug by making convert_file_format a pure function. It should only depend on data that is scoped inside of the function.