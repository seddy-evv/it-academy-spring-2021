""" First task
Your function takes two arguments:

1. current father's age (years)
2. current age of his son (years)
Сalculate how many years ago the father was twice as old as his son (or in how many years he will be twice as old)."""


def twice_as_old(dad_years_old, son_years_old):
    twice_age = (dad_years_old - son_years_old) * 2
    if dad_years_old > twice_age:
        return dad_years_old - twice_age
    elif dad_years_old < twice_age:
        return twice_age - dad_years_old
    else:
        return 0


print(twice_as_old(60, 35))

""" Second task
An ordered sequence of numbers from 1 to N is given. One number might have deleted from it, 
    then the remaining numbers were mixed. Find the number that was deleted.

Example:

The starting array sequence is [1,2,3,4,5,6,7,8,9]

The mixed array with one deleted number is [3,2,4,6,7,8,1,9]

Your function should return the int 5.

If no number was deleted from the array and no difference with it, your function should return the int 0.

Note: N may be 1 or less (in the latter case, the first array will be [])."""


def find_deleted_number(arr, mixed_arr):
    for element in arr:
        if not mixed_arr.count(element):
            return element
    return 0


arr_test = [1, 2, 3, 4, 5, 6, 7, 8, 9]
mixed_arr_test = [3, 2, 4, 6, 7, 8, 1, 9]
print(find_deleted_number(arr_test, mixed_arr_test))


""" Third task

Given a string, turn each character into its ASCII character code and join them together to create a number - 
let's call this number total1:

'ABC' --> 'A' = 65, 'B' = 66, 'C' = 67 --> 656667
Then replace any incidence of the number 7 with the number 1, and call this number 'total2':

total1 = 656667
              ^
total2 = 656661
              ^
Then return the difference between the sum of the digits in total1 and total2:

  (6 + 5 + 6 + 6 + 6 + 7)
- (6 + 5 + 6 + 6 + 6 + 1)
-------------------------
                       6
"""


def calc(x):
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
    return n


print(calc("ABC"))


""" Third task

Create a function that takes a Roman numeral as its argument and returns its value as a numeric decimal integer.
You don't need to validate the form of the Roman numeral.

Modern Roman numerals are written by expressing each decimal digit of the number to be encoded separately, 
starting with the leftmost digit and skipping any 0s. So 1990 is rendered "MCMXC" (1000 = M, 900 = CM, 90 = XC) and 
2008 is rendered "MMVIII" (2000 = MM, 8 = VIII). The Roman numeral for 1666, "MDCLXVI", 
uses each letter in descending order.

Example:

solution('XXI') # should return 21
Help:

Symbol    Value
I          1
V          5
X          10
L          50
C          100
D          500
M          1,000 """


def solution(roman):
    roman_letters = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    sum_ = 0
    previous_ = 0
    for element in roman:
        if roman_letters[element] > previous_:
            sum_ = sum_ - previous_ + roman_letters[element] - previous_
        else:
            sum_ += roman_letters[element]
        previous_ = roman_letters[element]
    return sum_


print(solution("MCMXC"))


"""Fifth task
Let us consider this example (array written in general format):

ls = [0, 1, 3, 6, 10]

Its following parts:

ls = [0, 1, 3, 6, 10]
ls = [1, 3, 6, 10]
ls = [3, 6, 10]
ls = [6, 10]
ls = [10]
ls = []
The corresponding sums are (put together in a list): [20, 20, 19, 16, 10, 0]

The function parts_sums (or its variants in other languages) will take as parameter a list ls and return a list of the 
sums of its parts as defined above.

Other Examples:
ls = [1, 2, 3, 4, 5, 6] 
parts_sums(ls) -> [21, 20, 18, 15, 11, 6, 0]

ls = [744125, 935, 407, 454, 430, 90, 144, 6710213, 889, 810, 2579358]
parts_sums(ls) -> [10037855, 9293730, 9292795, 9292388, 9291934, 9291504, 9291414, 9291270, 2581057, 2580168, 2579358,0]
Notes
Take a look at performance: some lists have thousands of elements.
Please ask before translating.
"""


def parts_sums(list_):

    n = len(list_)
    sum_ = 0
    for bypass in range(0, n):
        sum_ += list_[bypass]
    previous = 0
    for bypass in range(0, n):
        previous1 = list_[bypass]
        list_[bypass] = sum_ - previous
        previous += previous1
    return list_+[0]


print(parts_sums([1, 2, 3, 4, 5, 6]))
