"""
!Welcome to Object-Oriented Programming
Object-Oriented Programming, or "OOP", is a pattern for (allegedly) writing clean and maintainable code.

*Admittedly, not everyone agrees that object-oriented programming is the best way to write code,
* but, to be a good engineer, you should at least understand it.

Throughout this course, we'll be coding small bits of a real-time strategy game called "Age of Dragons".
Players control armies of humans, elves, orcs, and dragons in top-down battles.
It's similar to Age of Empires or StarCraft.

?Assignment
One of the greatest sins when trying to write "clean code" is using misleading variable and function names. Take a look at the destroy_wall function. It takes a list of numbers as input (each representing the health of a wall) and returns a new list with each entry of 0 or less removed.

Based on its name, you might assume that destroy_wall destroys a single wall, but if you look closely, you'll see that it handles multiple walls.

The test suite expects a different function name. Take a look at the main_test.py file to see what it's looking for, and rename the function accordingly.
Bonus: rename the variables inside the function to be more descriptive.
After passing the tests, take a look at the solution to see how we named everythin

def destroy_walls(wall_health):
health = []
for w_health in wall_health:
    if w_health > 0:
        new_health.append(w_health)
return new_health
"""


def destroy_walls(wall_healths):
    new_wall_healths = []
    for wall_health in wall_healths:
        if wall_health > 0:
            new_wall_healths.append(wall_health)
    return new_wall_healths
