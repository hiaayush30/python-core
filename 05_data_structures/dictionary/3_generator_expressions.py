# generator object is used when you have very large amount (infinite) data which does not need to be stored in the memory
# generator objects are iterables like lists but unlike them they do not store all values in memory,
# they generatespit out new value on each iteration

from sys import getsizeof

values = (x*2 for x in range(5000))  # this is a generator expression (does't return a tuple but a generator expression)
print("generator object:",getsizeof(values),"bytes") # size remains consistent on changing range above

list_values = [x*2 for x in range(5000)]
print("list:",getsizeof(list_values),"bytes")

# when you are using generator object, you will not be able to get the total number of values you are working with

print(values)

# [print(val) for val in values]