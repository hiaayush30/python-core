

def multiply(*nums):
    total=1
    for num in nums:
        total*=num
        return num
    
print("start")
print(multiply(2,3,4,5,6))