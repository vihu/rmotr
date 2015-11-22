"""
Write a function that receives a list and prints all its
items using a list comprehension.

Example:
        print_members(["Hello", 3, True, (1, 2)])

"""


def printer(i):
    print i


def print_members(a_list):
    return [printer(i) for i in a_list]


print_members(["Hello", 3, True, (1, 2)])
