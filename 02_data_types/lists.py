li = [1,2,3,4,5]

for i in li:
    print(i,end='\t')

print(li[-1])
print(len(li))

li[2:3]=["Lemon"]

if 4 in li:
    print("i have 4 in the list")

li.append("hello")
print(li)
li.remove("hello")

li.insert(0,"amzing")
print(li)

li2 = li.copy()


print(range(20))

#list comprehension
squared_nums = [x**2 for x in range(10)]
print(squared_nums)