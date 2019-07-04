from sys import getsizeof

value = (x*2 for x in range(5))
print("generator", getsizeof(value))

value = (x*2 for x in range(100000))
print("generator", getsizeof(value))

value = [x*2 for x in range(99)]
print("list", getsizeof(value))

value = {x*2 for x in range(99)}
print("list", getsizeof(value))
