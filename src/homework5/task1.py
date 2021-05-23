# The function "runner" calls functions from homework 2 according to the specified conditions.
import previous_tasks


def runner(*args):
    list_of_attr = dir(previous_tasks)
    for func in list_of_attr:
        attr = getattr(previous_tasks, func)
        if not args:
            if hasattr(attr, '__call__'):
                attr()
        else:
            if hasattr(attr, '__call__') and func in args:
                attr()


runner()
runner("return_longest_word")
runner("return_longest_word", "calculate_total_price", "calculate_letters")
