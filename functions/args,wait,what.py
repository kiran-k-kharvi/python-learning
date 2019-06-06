def multi(*number):
    for num in number:
        print(num)


multi(2, 5, 6, 8)


print("  ")


def multiply(*numb):
    total = 1
    for num in numb:
        total *= num
    return total


print(multiply(2, 4, 3))
 