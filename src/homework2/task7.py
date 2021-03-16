def calculate_area_triangle(a, b, c):
    if a + b > c and a + c > b and b + c > a:
        p = (a + b + c) / 2
        s = (p * (p - a) * (p - b) * (p - c))**0.5
        return "Area is:{}".format(s)
    else:
        return "Incorrect value"


print(calculate_area_triangle(1, 3, 3))
print(calculate_area_triangle(1, 2, 3))
