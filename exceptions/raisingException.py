def cal_xfact(age):
    if age <= 0:
        raise ValueError("age cannot be 0")
    return 10 / age


try:
    cal_xfact(-1)
except ValueError as error:
    print(error)
