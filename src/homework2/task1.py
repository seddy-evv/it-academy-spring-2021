def calculate_total_price(m, n, s):
    total_price = (m + n/100) * s
    return total_price


total = calculate_total_price(1, 80, 10)
print(total)
