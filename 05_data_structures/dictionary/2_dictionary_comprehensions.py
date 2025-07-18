values = []

# list comprehension revision
# [expression for item in items]

for x in range(5):
    values.append(x*2)
#or
values = [ x*2 for x in range(5) ]

print(values) 

# similarly set comprehension
set_values = { x*2 for x in range(5) }
print(set_values)

my_dictionary={ x : x*2 for x in range(5)}
print(my_dictionary) 

tuple_values = (x*2 for x in range(5)) # returns a generator object
print(tuple_values)