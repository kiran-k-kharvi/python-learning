items = [
    ("product1", 10),
    ("product2", 9),
    ("product3", 12),
    ("product4", 1),
]
# prices = list(map(lambda item: item[1], items))

prices = [item[1] for item in items]  # same as map function above
print(prices)

# filtered = list(filter(lambda item: item[1] >= 10, items))
# same as filter function above
prices = [item for item in items if item[1] >= 10]
print(prices)
