# Small anonymous functions can be created with the lambda keyword
import dis


def make_incrementor(n):
    return lambda x: x + n


f = make_incrementor(42)
f(0)    # make_incrementor(42)(0)
# 42
f(1)
# 43

# THIS IS ANONYMOUS FUNCTION WHERE WE USE THIS WHEN WE TRY TO HAVE FUNCTION WITH NO NAME
# ALSO WE CAN USE THIS WHEN WE WANT TO GIVE ARG TO ARG FUNC

lambda x: x     # THIS RETURNS THE X VALUE WHICH IS GIVEN AS ARGUMENT

(lambda x: x + 1)(2)
# X VALUE IS TAKEN AS 2 AND GIVES US 3


def add_one(x): return x + 1
def add_one(x): return x + 1


def outer_func(x):  # outer_func(i)(z)
    y = 4
    return lambda z: x + y + z


closure = outer_func(1)  # outer_func(1)(1)
# print(outer_func(1)(1, 2, 3))
for i in range(3):
    closure = outer_func(1)  # outer_func(1)(1)
    print(i, closure(i))


def add(x, y): return x + y


type(add)
# <class 'function'>
dis.dis(add)
#   1           0 LOAD_FAST                0 (x)
#   2 LOAD_FAST                1 (y)
#   4 BINARY_ADD
#   6 RETURN_VALUE
print(add)
# <function <lambda> at 0x7f30c6ce9ea0>

finder = (lambda x: (x % 2 and 'odd' or 'even'))
print(finder(2))
# even
print(finder(3))
# odd


# Lamda also has all the types of arg position, keyword, **
# All the below code will produce 6 as output

(lambda x, y, z: x + y + z)(1, 2, 3)

(lambda x, y, z=3: x + y + z)(1, 2)

(lambda x, y, z=3: x + y + z)(1, y=2)

(lambda *args: sum(args))(1, 2, 3)

(lambda **kwargs: sum(kwargs.values()))(one=1, two=2, three=3)

(lambda x, *, y=0, z=0: x + y + z)(1, y=2, z=3)
