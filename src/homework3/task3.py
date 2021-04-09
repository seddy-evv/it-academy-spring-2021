# Task3 - Tuple practice


tuple1 = tuple(['a', 'b', 'c'])
print(tuple1, type(tuple1))

lst1 = list(tuple1)
print(lst1, type(lst1))

a, b, c = 'a', 2, "python"
print(a, b, c)

tuple2 = ([1, 2, 3],)
print(len(tuple2))
for list1 in tuple2:
    for i in list1:
        print(i)
print(len(tuple2))
