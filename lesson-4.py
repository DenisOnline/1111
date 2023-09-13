def black_hole(*args):
    print(type(args))
    for i in args:
        print(i)


def black_hole_named(**kwargs):
    print(type(kwargs))
    for i in kwargs:
        print(i)


def black_hole_mixed(var_1, var_2=3, *args, **kwargs):
    print("var_1 = ", var_1)
    print("var_2 = ", var_2)
    for arg in args:
        print("arg = ", arg)
    for key, value in kwargs.items():
        print("key = ", key, ", value = ", value)


def way(v, t):
    print(v * t)


list = [89, 13]
dict = {"v": 110, "t": 13}
way(**dict)

import random

i = 0
while i < 10:
    print(random.randint(1, 10))
    i += 1
# black_hole(1 ,34, 3, "Cat", 3)
# black_hole_named(name="Denis", age=21)
# black_hole_mixed(3, 4, "Cat", 34, name="Denis", age=21)
