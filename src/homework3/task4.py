def count_pairs(str_of_numbers):
    clean_str = str_of_numbers.replace(" ", "")
    number_of_pairs = 0
    line_length = len(clean_str)
    for i in range(line_length):
        for numb in range(i + 1, line_length):
            if int(clean_str[i]) == int(clean_str[numb]):
                number_of_pairs += 1
    return number_of_pairs


print(count_pairs("1 1 1"))
print(count_pairs("1 1 1 1"))
print(count_pairs("2 1 1 1 1 2"))
