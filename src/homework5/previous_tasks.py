# Homework 2.
import re

N = 7


def calculate_total_price(m=1, n=80, s=10):
    total_price = (m + n / 100) * s
    print("Total price {}".format(total_price))


def return_longest_word():
    text = ("Walking, running, cycling and "
            "playing football are some kinds "
            "of sports that you do every day.")
    clean_text = re.sub(r"[^\w\s]", "", text)
    strings = clean_text.split()
    longest_word = ""
    for current_str in strings:
        if len(current_str) > len(longest_word):
            longest_word = current_str
    print(longest_word)


def replace_duplicate():
    text = "abc cde def"
    clean_text = text.replace(" ", "")
    new_str = ""
    for element in clean_text:
        if new_str.find(element) == -1:
            new_str += element
    print(new_str)


def calculate_letters():
    text = ("Walking, running, cycling and "
            "playing football are some kinds "
            "of sports that you do every day.")
    uppercase_alphabet = ("ABCDEFGHIJKLMNO"
                          "PQRSTUVWXYZ")
    lower_case_alphabet = uppercase_alphabet.lower()
    upper = 0
    lower = 0
    for element in text:
        if element in uppercase_alphabet:
            upper += 1
        elif element in lower_case_alphabet:
            lower += 1
    template = "in string {} cursive letters and {} lowercase letters"
    print(template.format(upper, lower))


def fibonacci(n=6):
    fibonacci_number = 1
    first_number = 0
    for i in range(3, n + 1):
        fibonacci_number, first_number = fibonacci_number + first_number, fibonacci_number
    fibonacci_number = 1 if n == 2 else fibonacci_number
    print(fibonacci_number)


def palindrome(origin_number=187781):
    total_number = 0
    num = origin_number
    while num > 0:
        dig = num % 10
        total_number = total_number * 10 + dig
        num = num // 10
    if origin_number == total_number:
        print(True)
    else:
        print(False)


def calculate_area_triangle(a=1, b=3, c=3):
    if a + b > c and a + c > b and b + c > a:
        p = (a + b + c) / 2
        s = (p * (p - a) * (p - b) * (p - c))**0.5
        print("Area is:{}".format(s))
    else:
        print("Incorrect value")


def twice_as_old(dad_years_old=60, son_years_old=35):
    twice_age = (dad_years_old - son_years_old) * 2
    if dad_years_old > twice_age:
        print(dad_years_old - twice_age)
    elif dad_years_old < twice_age:
        print(twice_age - dad_years_old)
    else:
        print(0)


def find_deleted_number():
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    mixed_arr = [3, 2, 4, 6, 7, 8, 1, 9]
    req_el = 0
    for element in arr:
        if not mixed_arr.count(element):
            req_el = element
    print(req_el)


def calc(x="ABC"):
    total1 = ""
    for element in x:
        total1 += str(ord(element))
    total2 = total1.replace("7", "1")
    sum1 = 0
    for element in total1:
        sum1 += int(element)
    sum2 = 0
    for element in total2:
        sum2 += int(element)
    n = sum1 - sum2
    print(n)


def solution(roman="MCMXC"):
    roman_letters = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    sum_ = 0
    previous_ = 0
    for element in roman:
        if roman_letters[element] > previous_:
            sum_ = sum_ - previous_ + roman_letters[element] - previous_
        else:
            sum_ += roman_letters[element]
        previous_ = roman_letters[element]
    print(sum_)


def parts_sums():
    list_ = [1, 2, 3, 4, 5, 6]
    n = len(list_)
    sum_ = 0
    for bypass in range(0, n):
        sum_ += list_[bypass]
    previous = 0
    for bypass in range(0, n):
        previous1 = list_[bypass]
        list_[bypass] = sum_ - previous
        previous += previous1
    print(list_ + [0])
