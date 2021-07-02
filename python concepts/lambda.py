# THIS IS ANONYMOUS FUNCTION WHERE WE USE THIS WHEN WE TRY TO HAVE FUNCTION WITH NO NAME
# ALSO WE CAN USE THIS WHEN WE WANT TO GIVE ARG TO ARG FUNC

lambda x: x     # THIS RETURNS THE X VALUE WHICH IS GIVEN AS ARGUMENT

(lambda x: x + 1)(2)
# X VALUE IS TAKEN AS 2 AND GIVES US 3


# add_one = lambda x: x + 1
def add_one(x): return x + 1


def outer_func(x):
    y = 4
    return lambda z: x + y + z


for i in range(3):
    closure = outer_func(i)
    print(f"closure({i+5}) = {closure(i+5)}")
