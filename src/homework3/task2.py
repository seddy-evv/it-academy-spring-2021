# Task3 - List practice


import copy

lst1 = [element + element1 for element in 'ab' for element1 in 'bcd']
print(lst1)

lst2 = lst1[0:6:2]
print(lst2)

lst3 = [element + "a" for element in "1234"]
print(lst3)

element_2a = lst3.pop(1)
print(element_2a)
print(lst3)

lst4 = copy.deepcopy(lst3)
lst4.append(element_2a)
print(lst3)
print(lst4)
