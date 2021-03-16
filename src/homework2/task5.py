def fibonacci(n):
    fibonacci_number = 0
    first_number = 0
    second_number = 1
    for i in range(3, n+1):
        fibonacci_number = first_number + second_number
        first_number = second_number
        second_number = fibonacci_number
    fibonacci_number = 1 if n == 2 else fibonacci_number
    print(fibonacci_number)


fibonacci(7)
