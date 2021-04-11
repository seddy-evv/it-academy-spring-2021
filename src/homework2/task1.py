# The function calculates the total price of the product.
# Initial data:
# m - amount of rubles
# n - the number of penny
# s - quantity of goods


def calculate_total_price(m, n, s):
    total_price = (m + n / 100) * s
    return total_price


total = calculate_total_price(1, 80, 10)
print("Total price {}".format(total))
