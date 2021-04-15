# Implementation of the Euclidean algorithm without using functions and recursion.


a = 1071
b = 459
if b > a:
    a, b = b, a
c = a
while True:
    while c > b:
        c = a % b
    if a == b:
        print("numbers are equal")
        break
    elif c:
        a, b, c = b, c, a
    else:
        print(b)
        break
