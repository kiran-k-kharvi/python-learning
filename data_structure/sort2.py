items = [
    ("product1", 10),
    ("product2", 9),
    ("product3", 12),
    ("product4", 1),
]


def sort_item(item):
    return item[1]


items.sort(key=sort_item)
print(items)
