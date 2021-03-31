lst_ = [0, 1, 4, 0, 5, 0, 3, 0, 9, 7, 0]
n = len(lst_)
b = 0
for k in range(n):
    if lst_[k]:
        lst_[b], lst_[k] = lst_[k], lst_[b]
        b += 1

print(lst_)
