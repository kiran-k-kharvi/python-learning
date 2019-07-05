from timeit import timeit

code1 = """
def cal_xfact(age):
    if age <= 0:
        raise ValueError("age cannot be 0")
    return 10 / age


try:
    cal_xfact(-1)
except ValueError as error:
    pass
"""

code2 = """
def cal_xfact(age):
    if age <= 0:
        return None
    return 10 / age


xfactor = cal_xfact(-1)
if xfactor == None:
    pass
"""

print("first code", timeit(code1, number=10000))
print("second code", timeit(code2, number=10000))
