numbers = [5,10,2,88,9]

# numbers.sort(reverse=True)
sorted_nums = sorted(numbers,reverse=True)
print(sorted_nums)
print(numbers)

items = [
    ("Product3",99),
    ("Product2",102),
    ("Product1",78),
    ("Product5",35),
    ("Product4",98)
]

def sort_item(item):  # returns the item price
    return item[1]
items.sort(key=sort_item)
print(items)