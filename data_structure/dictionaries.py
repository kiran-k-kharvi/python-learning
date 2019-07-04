point = {"x": 1, "y": 2}
point = dict(x=1, y=2)  # same as above
print(point["x"])
point["z"] = 20
print(point)

if " a" in point:
    print(point["a"])
print(point.get("a", 0))
print(point)

del point["x"]
print(point)


for key in point:
    print(key, point[key])
