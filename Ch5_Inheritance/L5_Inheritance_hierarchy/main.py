"""
There is no (technical) limit to how deeply we can nest an inheritance tree. For example:
*Tiger inherits from Feline inherits from Animal inherits from LivingThing.

A good child class is a strict subset of its parent class.

"""


class Human:
    def __init__(self, name):
        self.__name = name

    def get_name(self):
        return self.__name


## don't touch above this line


class Archer(Human):
    def __init__(self, name, num_arrows):
        super().__init__(name)
        self._num_arrows = num_arrows

    def get_num_arrows(self):
        return self._num_arrows

    def use_arrows(self, num):
        if num > self._num_arrows:
            raise Exception("not enough arrows")
        self._num_arrows -= num


class Crossbowman(Archer):
    def __init__(self, name, num_arrows):
        super().__init__(name, num_arrows)

    def triple_shot(self, target):
        if self._num_arrows < 3:
            raise Exception("not enough arrows")
        self._num_arrows -= 3
        return f"{target.get_name()} was shot by 3 crossbow bolts"
