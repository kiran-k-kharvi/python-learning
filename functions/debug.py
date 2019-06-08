def mult(*num):
    total = 1
    for number in num:
        total *= number
    return total


print("start")
print(mult(1, 2, 3, 4))
