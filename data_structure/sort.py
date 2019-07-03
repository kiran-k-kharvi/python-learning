numbers = [3, 41, 65, 87, 12, 50]
numbers.sort(reverse=True)  # """  this will modify the list """
print(numbers)

print(sorted(numbers))  # """   this will no modify the list """
numbers.sort(reverse=True)  # """  this will modify the list """
print(numbers)
print(sorted(numbers, reverse=True))
print(numbers)
