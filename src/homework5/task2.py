# A decorator has been created that stores the results of function calls
# (for the entire time of calls, and not just the current run of the program).
import os.path


def dec(func):

    def wrapper(*args, **kwargs):

        if os.path.exists('text.txt'):
            with open('text.txt', 'r') as fh:
                count_call = int(fh.read())
        else:
            count_call = 0
        with open('text.txt', 'w') as fh:
            fh.write(str(count_call + 1))
        print(count_call + 1)

        result = func(*args, **kwargs)
        return result

    return wrapper


@dec
def function():
    pass


function()
