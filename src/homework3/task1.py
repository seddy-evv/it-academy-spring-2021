def fizz_buzz():
    for n in range(1, 101):
        if not n % 3 and not n % 5:
            print("FizzBuzz")
        elif not n % 3:
            print("Fizz")
        elif not n % 5:
            print("Buzz")
        else:
            print(n)


fizz_buzz()
