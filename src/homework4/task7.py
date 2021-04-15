# Implementation of the Euclidean algorithm without using functions and recursion.


a = 459
b = 1071
if b > a:
    a, b = b, a
c = a
while c > b:
    while c > b:
        c = a % b
    if c:
        a, b, c = b, c, a
    else:
        print(b)
        break
else:
    print("numbers are equal")
