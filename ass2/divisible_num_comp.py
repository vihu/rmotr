"""
Write a function that receives a list of numbers
and a term 'n' and returns only the elements that are divisible
by that term 'n'. You must use List comprehensions to solve it.

Example:
        divisible_numbers([9, 8, 7, 6, 5, 4, 3, 2, 1], 3)  # [9, 6, 3]
        """

def divisible_numbers(a_list, term):
    # return a list of numbers only divisble by term in a_list
    return [i for i in a_list if i%3==0]
