letters = ["a","b","c"]
print([0]*5)

combined = [0]*5 + letters
print(combined)

print([0,1,2,3]*2)

list_from_range= list(range(20))
print(list_from_range)

chars = list("Hello")
print(chars)

print(len(list_from_range))

letters.append("q")
letters.insert(0,'y')
letters.pop()
letters.remove('a')  # will only remove the first occurence
del letters[0:1]
letters.clear()
print(letters)

new_list = [10,20,30,40,50,60,70,80,90,100,20,30,20]
# print(new_list.index(51))
# if the value does not exist,python throws an error unlike c based langs which return -1
# so
if 51 in new_list:
    print(new_list.index(51))
else:
    print("51 not present")

print(new_list.count(20))

