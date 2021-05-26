# The function "runner" calls functions from homework 2 according to the specified conditions.
from inspect import isfunction
import previous_tasks


def runner(*args):
    list_of_attr = dir(previous_tasks)
    for func in list_of_attr:
        attr = getattr(previous_tasks, func)
        if not args:
            if isfunction(attr):
                attr()
        else:
            if isfunction(attr) and func in args:
                attr()


runner()
runner("return_longest_word")
runner("return_longest_word", "calculate_total_price", "calculate_letters")
