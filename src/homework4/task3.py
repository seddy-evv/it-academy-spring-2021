# The function takes two lists of numbers and counts how many distinct numbers
# are in the first and second lists at the same time.


def count_numbers(list1, list2):
    set1 = set(list1)
    set2 = set(list2)
    count_of_numbers = len(set1 & set2)
    print(count_of_numbers)


count_numbers([1, 3, 4, 1, 5, 7], [7, 8, 3, 22, 1, 18])
