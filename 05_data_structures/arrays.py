# used when you have large sequence of numbers
# this datatype takes a little less memory and performs a bit faster wrt tuple

from array import array # module and class name is same

numbers = array("i",[1,2,3,4,5])  # i is typecode for signed integer

print(numbers)

numbers.append(100)
numbers.insert(1,55)
print(numbers)
print(numbers[0])

# unlike lists the objects in the array are of a single defined type
