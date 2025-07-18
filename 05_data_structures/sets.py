numbers = [1,1,2,2,3]

uniques = set(numbers)
print(uniques)

my_set1 = {10,4,8}
my_set1.add(5)
my_set1.remove(8)
print(my_set1)

my_set2 = {1,2,3,4,5}

print(my_set1 | my_set2)  # union of two sets
print(my_set1 & my_set2)  # intersection of two sets
print(my_set1 - my_set2)  # will retun the values present in set1 but not in set2
print(my_set1 ^ my_set2)  # unique values present in either set but not both (symatric difference)

# unlike lists sets are unordered collections ie no indexing

if 1 in my_set1:
    print("1 is present")
else:
    print("not present")