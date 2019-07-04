number = [1, 2, 3]
print(*number)  # * is unpacking operator

values = list(range(20))
print(values)

value = [*range(12, 22, 2), *"hello"]  # does same function as above
print(value)


first = {"x": 11}
second = {"x": 10, "y": 20, "z": 30}
combined = {**first, **second}
print(combined)
