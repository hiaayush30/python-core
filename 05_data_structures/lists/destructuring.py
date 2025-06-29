numbers = [1,2,3]
first,second,third = numbers
print(second)

numbers2 = list(range(20))
first_1,*others,last= numbers2
print(others)

def multiply_numbers(*nums):
    total=1
    for num in nums:
        total*=num
    return total

print(multiply_numbers(*others))
print(multiply_numbers(1,2,3,4))

def printList(*nums):
    for num in enumerate(nums):  #returns a tuple with index and value
        print(num)

#or

def printList2(*nums):
    for index,val in enumerate(nums):  #returns a tuple with index and value
        print(index)

printList2(10,20,30)