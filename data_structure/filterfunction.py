items = [
    ("product1", 10),
    ("product2", 9),
    ("product3", 12),
    ("product4", 1),
]

filtered = list(filter(lambda item: item[1] >= 10, items))
print(filtered)
