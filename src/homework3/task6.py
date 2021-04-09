# The initial data is a list of integers. The function moves all nonzero elements
# to the left side of the list without changing their order, and all zeros to
# the right side and prints the resulting list. The order of nonzero elements is not changed,
# the additional list is not used, the movement is performed in one pass through the list.


lst_ = [0, 1, 4, 0, 5, 0, 3, 0, 9, 7, 0]
n = len(lst_)
b = 0
for k in range(n):
    if lst_[k]:
        lst_[b], lst_[k] = lst_[k], lst_[b]
        b += 1

print(lst_)
