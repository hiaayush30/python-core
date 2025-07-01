items = [
    ("Product3",99),
    ("Product2",102),
    ("Product1",78),
    ("Product5",35),
    ("Product4",98)
]

# itemValues = []
# for item in items:
#     itemValues.append(item[1])

# map fn
itemValues = map(lambda item:item[1],items) #returns an iterable
for value in itemValues:
    print(value)

print(".....................")
# filter fn
itemValues1= filter(lambda item : item[1]>90,items)
for item in itemValues1:
    print(item)