items = [
    ("product1", 10),
    ("product2", 9),
    ("product3", 12),
    ("product4", 1),
]

prices = list(map(lambda item: item[1], items))
print(prices)
