list1= [1,2,3]
list2=[10,20,30]

# [(1,10),(2,20),(3,30)]

# newList = list(zip(list1,list2))
newList = list(zip("abcd",list1,list2))
print(newList)