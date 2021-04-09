# Task1 - 1 line


BOARD_SIZE = 8


class BailOut(Exception):
    pass


def validate(list_queens):
    left = right = col = list_queens[-1]
    for r in reversed(list_queens[:-1]):
        left, right = left - 1, right + 1
        if r in (left, col, right):
            raise BailOut


def add_queen(list_queens):
    for i in range(BOARD_SIZE):
        test_queens = list_queens + [i]
        try:
            validate(test_queens)
            if len(test_queens) == BOARD_SIZE:
                return test_queens
            else:
                return add_queen(test_queens)
        except BailOut:
            pass
    raise BailOut


queens = add_queen([])
print(queens)
print("\n".join(". " * q + "Q " + ". " * (BOARD_SIZE - q - 1) for q in queens))
