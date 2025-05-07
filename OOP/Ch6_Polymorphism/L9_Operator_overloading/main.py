"""

* As we discussed in the last assignment, operator overloading is the practice of defining custom behavior for standard Python operators.
* Here's a list of how the operators translate into method names.

?Operation	Operator	Method
Addition	+	__add__
Subtraction	-	__sub__
Multiplication	*	__mul__
Power	**	__pow__
Division	/	__truediv__
Floor Division	//	__floordiv__
Remainder (modulo)	%	__mod__
Bitwise Left Shift	<<	__lshift__
Bitwise Right Shift	>>	__rshift__
Bitwise AND	&	__and__
Bitwise OR	|	__or__
Bitwise XOR	^	__xor__
Bitwise NOT	~	__invert__

    > The last ones are just like in assembly brother...

"""


class Sword:
    def __init__(self, sword_type):
        self.sword_type = sword_type

    def __add__(self, other):
        # return self.sword_type + other.sword_type
        if self.sword_type == "bronze" and other.sword_type == "bronze":
            return Sword("iron")
        if self.sword_type == "iron" and other.sword_type == "iron":
            return Sword("steel")
        raise Exception("cannot craft")
