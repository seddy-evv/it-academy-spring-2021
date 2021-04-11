# The function prints the n-th Fibonacci number.


def fibonacci(n):
    fibonacci_number = 1
    first_number = 0
    for i in range(3, n + 1):
        fibonacci_number, first_number = fibonacci_number + first_number, fibonacci_number
    fibonacci_number = 1 if n == 2 else fibonacci_number
    print(fibonacci_number)


fibonacci(3)
