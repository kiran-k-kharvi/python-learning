number = [1, 2, 2, 3, 4]
first = set(number)
print(first)
second = {2, 7, 8, 9}
print(second)
second.add(5)
print(second)
second.remove(7)
print(" second length", len(second))
print(second)

print(first | second)  # union
print(first & second)  # intersection
print(first - second)
print(first ^ second)  # eiher in first or second not in both

if 1 in first:
    print("yes")
