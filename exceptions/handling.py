try:
    age = int(input("Age: "))
    xfact = 10 / age
# except ValueError:
#     print("enter valid age")
# except ZeroDivisionError:
#     print("age cannot be 0")
except (ValueError, ZeroDivisionError):
    print("enter valid age")
else:
    print("no exception")
print("Execution conioneous")
