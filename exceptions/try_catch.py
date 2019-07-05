try:
    age = int(input("Age: "))
except ValueError:
    print("enter valid age")
else:
    print("no exception")
print("Execution conioneous")
