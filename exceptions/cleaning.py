try:
    file = open("file.txt")
    age = int(input("Age: "))
    xfact = 10 / age
except (ValueError, ZeroDivisionError):
    print("enter valid age")
else:
    print("no exception")
finally:
    file.close()
