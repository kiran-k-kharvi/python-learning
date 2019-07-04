values = []
for x in range(5):
    values.append(x*2)
print(values)

# same using comprehension
#  [expression for item in items]
value = [x*2 for x in range(5)]  # comprehension on list
print(value)

value = {x*2 for x in range(5)}  # comprehension on sets
print(value)

value = {x: x*2 for x in range(5)}  # comprehension on dictionary
print(value)
