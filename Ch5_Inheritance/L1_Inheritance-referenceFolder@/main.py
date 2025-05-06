"""
? Non-OOP languages like Go and Rust support encapsulation and abstraction... almost every language does.
!Inheritance, on the other hand, is typically unique to class-based languages like Python, Java, and Ruby.

Inheritance allows a "child" class, to inherit properties and methods from "parent" class.
 It's a way to share code between classes.


"""


class Human:
    def __init__(self, name):
        self.__name = name

    def get_name(self):
        return self.__name


## don't touch above this line


class Archer(Human):
    # This is a child class of Human
    # It inherits the properties and methods of the Human class
    def __init__(self, name, num_arrows):
        super().__init__(
            name
        )  # Call the constructor of the parent class (Human)   https://docs.python.org/3/library/functions.html#super
        self.__num_arrows = num_arrows
        # self.__name = name # This is not needed, because the parent class (Human) already has a __name property

    def get_num_arrows(self):
        return self.__num_arrows


# You can add functions to test your code here
def main():
    # Your own tests
    human = Human("Test Human")
    archer = Archer("Test Archer", 10)
    print(f"Human name: {human.get_name()}")
    print(f"Archer name: {archer.get_name()}")
    print(f"Archer arrows: {archer.get_num_arrows()}")


# if __name__ == "__main__":
#    main()
# I dont really need this, because I am not running this file directly
# I am running the test file, which will import this file and run the tests
# I will just leave it here for now, in case I need to run this file directly in the future
