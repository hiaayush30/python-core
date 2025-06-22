from chai_fn import chai

print("Hello again")
print("*" * 10)

chai("python function") 

arr1 = [1,2,3]
arr2 = [1,2,3]
arr3 = arr1

print(arr1 is arr2)
print(arr3 == arr2)
print(arr3 is arr1)

# Python's == operator is generally used for value comparison and implicitly considers the
# types for meaningful comparison, similar to JavaScript's ===.
# Python's is operator checks for object identity (whether two variables point to the same
# object in memory), which is a distinct concept.

repr('chai')
print('chai')
str('chai')