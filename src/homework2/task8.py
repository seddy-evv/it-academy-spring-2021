# Tasks from codewars.com
""" First task
Your function takes two arguments:

1. current father's age (years)
2. current age of his son (years)
Сalculate how many years ago the father was twice as old as his son
(or in how many years he will be twice as old)."""


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

If no number was deleted from the array and no difference with it,
your function should return the int 0.

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

Given a string, turn each character into its ASCII character code
and join them together to create a number - let's call this number total1:

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

Create a function that takes a Roman numeral as its argument and returns its value
as a numeric decimal integer.
You don't need to validate the form of the Roman numeral.

Modern Roman numerals are written by expressing each decimal digit of the number
to be encoded separately, starting with the leftmost digit and skipping any 0s.
So 1990 is rendered "MCMXC" (1000 = M, 900 = CM, 90 = XC) and
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

The function parts_sums (or its variants in other languages) will take
as parameter a list ls and return a list of the sums of its parts as defined above.

Other Examples:
ls = [1, 2, 3, 4, 5, 6]
parts_sums(ls) -> [21, 20, 18, 15, 11, 6, 0]

ls = [744125, 935, 407, 454, 430, 90, 144, 6710213, 889, 810, 2579358]
parts_sums(ls) -> [10037855, 9293730, 9292795, 9292388, 9291934, 9291504,
                   9291414, 9291270, 2581057, 2580168, 2579358,0]
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
    return list_ + [0]


print(parts_sums([1, 2, 3, 4, 5, 6]))


"""A friend of mine takes the sequence of all numbers from 1 to n (where n > 0).
Within that sequence, he chooses two numbers, a and b.
He says that the product of a and b should be equal to the sum of all numbers in the sequence,
excluding a and b.
Given a number n, could you tell me the numbers he excluded from the sequence?
The function takes the parameter: n (n is always strictly greater than 0)
and returns an array or a string (depending on the language) of the form:

[(a, b), ...] or [[a, b], ...] or {{a, b}, ...} or or [{a, b}, ...]
with all (a, b) which are the possible removed numbers in the sequence 1 to n.

[(a, b), ...] or [[a, b], ...] or {{a, b}, ...} or ... will be sorted in increasing order
of the "a".

It happens that there are several possible (a, b). The function returns an empty array
(or an empty string) if
no possible numbers are found which will prove that my friend has not told the truth!
(Go: in this case return nil).

Examples:
removNb(26) should return [(15, 21), (21, 15)]
or
removNb(26) should return { {15, 21}, {21, 15} }
or
removeNb(26) should return [[15, 21], [21, 15]]
or
removNb(26) should return [ {15, 21}, {21, 15} ]
or
removNb(26) should return "15 21, 21 15"
or

in C:
removNb(26) should return  {{15, 21}{21, 15}} tested by way of strings.
Function removNb should return a pointer to an allocated array of Pair pointers,
each one also allocated."""


def remov_nb(n):
    total = 0
    list_high = []
    list_low = []
    for i in range(n + 1):
        total += i
    for i in range(n, 0, - 1):
        z = (total - i) // i
        if i * z == (total - i - z):
            list_low.append((z, i))
            list_high.append((i, z))
    list_high.reverse()
    return list_low + list_high


print(remov_nb(26))


"""Given two strings s1 and s2, we want to visualize how different the two strings are.
We will only take into account the lowercase letters (a to z).
First let us count the frequency of each lowercase letters in s1 and s2.
s1 = "A aaaa bb c"
s2 = "& aaa bbb c d"
s1 has 4 'a', 2 'b', 1 'c'
s2 has 3 'a', 3 'b', 1 'c', 1 'd'

So the maximum for 'a' in s1 and s2 is 4 from s1; the maximum for 'b' is 3 from s2.
In the following we will not consider letters when the maximum of their occurrences
is less than or equal to 1.

We can resume the differences between s1 and s2 in the following string: "1:aaaa/2:bbb"
where 1 in 1:aaaa stands for string s1 and aaaa because the maximum for a is 4.
In the same manner 2:bbb stands for string s2 and bbb because the maximum for b is 3.

The task is to produce a string in which each lowercase letters of s1 or s2 appears
as many times as its maximum if this maximum is strictly greater than 1;
these letters will be prefixed by the number of the string where they appear
with their maximum value and :. If the maximum is in s1 as well as in s2 the prefix is =:.

In the result, substrings (a substring is for example 2:nnnnn or 1:hhh;
it contains the prefix) will be in decreasing order of their length and when they have
the same length sorted in ascending lexicographic order (letters and digits - more precisely
sorted by codepoint); the different groups will be separated by '/'.
See examples and "Example Tests".

Hopefully other examples can make this clearer.

s1 = "my&friend&Paul has heavy hats! &"
s2 = "my friend John has many many friends &"
mix(s1, s2) --> "2:nnnnn/1:aaaa/1:hhh/2:mmm/2:yyy/2:dd/2:ff/2:ii/2:rr/=:ee/=:ss"

s1 = "mmmmm m nnnnn y&friend&Paul has heavy hats! &"
s2 = "my frie n d Joh n has ma n y ma n y frie n ds n&"
mix(s1, s2) --> "1:mmmmmm/=:nnnnnn/1:aaaa/1:hhh/2:yyy/2:dd/2:ff/2:ii/2:rr/=:ee/=:ss"

s1="Are the kids at home? aaaaa fffff"
s2="Yes they are here! aaaaa fffff"
mix(s1, s2) --> "=:aaaaaa/2:eeeee/=:fffff/1:tt/2:rr/=:hh"""""


def mix(s1, s2):
    letters = "abcdefghijklmnopqrstuvwxyz"
    dict_s1 = {}
    dict_s2 = {}
    max_len = 0
    for el in s1:
        if el in letters:
            dict_s1[el] = dict_s1.get(el, 0) + 1
            max_len = dict_s1[el] if dict_s1[el] > max_len else max_len
    for el in s2:
        if el in letters:
            dict_s2[el] = dict_s2.get(el, 0) + 1
            max_len = dict_s2[el] if dict_s2[el] > max_len else max_len
    list_letters = ["" for _ in range(max_len + 1)]
    for el in letters:
        sum_string1 = dict_s1.get(el, 0)
        sum_string2 = dict_s2.get(el, 0)
        if sum_string1 > sum_string2 and sum_string1 > 1:
            list_letters[sum_string1] = list_letters[sum_string1] + "1:" + el * sum_string1 + "/"
    for el in letters:
        sum_string1 = dict_s1.get(el, 0)
        sum_string2 = dict_s2.get(el, 0)
        if sum_string1 < sum_string2 and sum_string2 > 1:
            list_letters[sum_string2] = list_letters[sum_string2] + "2:" + el * sum_string2 + "/"
    for el in letters:
        sum_string1 = dict_s1.get(el, 0)
        sum_string2 = dict_s2.get(el, 0)
        if sum_string1 == sum_string2 and sum_string1 > 1:
            list_letters[sum_string1] = list_letters[sum_string1] + "=:" + el * sum_string1 + "/"
    list_letters.reverse()
    return("".join(list_letters)).strip("/")


print(mix("Sadus:cpms>orqn3zecwGvnznSgacs", "MynwdKizfd$lvse+gnbaGydxyXzayp"))
