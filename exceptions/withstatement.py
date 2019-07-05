try:
    with open("file.txt") as file:  # no need of finally:
        print("file opened.")
        file.__enter__
    age = int(input("Age: "))
    xfact = 10 / age
except (ValueError, ZeroDivisionError):
    print("enter valid age")
else:
    print("no exception")
