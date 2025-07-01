# [expression for item in items]

items = [
    ("Product3",99),
    ("Product2",102),
    ("Product1",78),
    ("Product5",35),
    ("Product4",98)
]

# prices = list(map(lambda item : item[1],items))
# or
# prices = [item[1] for item in items]

# prices = list(filter(lambda item : item[1]>90,items))
# or
prices = [item[1] for item in items if item[1]>90]


print(prices)