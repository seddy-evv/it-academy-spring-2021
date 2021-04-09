# The initial data is a list. The function prints those elements of it
# that appear in the list only once, in the order in which they appear in the list.


list_ = ["a", "b", "c", "d", "d", "f", "e", "e"]
for element in list_:
    if list_.count(element) == 1:
        print(element)
