# The initial data is a list of integers. The function moves all nonzero elements
# to the left side of the list without changing their order, and all zeros to
# the right side and prints the resulting list. The order of nonzero elements is not changed,
# the additional list is not used, the movement is performed in one pass through the list.


list_of_numbers = [0, 1, 4, 0, 5, 0, 3, 0, 9, 7, 0]
amount_of_elements = len(list_of_numbers)
index = 0
for n in range(amount_of_elements):
    if list_of_numbers[n]:
        list_of_numbers[index], list_of_numbers[n] = list_of_numbers[n], list_of_numbers[index]
        index += 1

print(list_of_numbers)
