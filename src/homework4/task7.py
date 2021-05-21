# Implementation of the Euclidean algorithm without using functions and recursion.


first_number = 459
second_number = 4071
if second_number > first_number:
    first_number, second_number = second_number, first_number
elif first_number == second_number:
    print("numbers are equal")

while first_number > second_number:
    first_number = first_number % second_number
    if first_number:
        first_number, second_number = second_number, first_number
    else:
        print(second_number)
        break
