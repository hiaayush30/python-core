def increment(number,by):
   return number + by

print(increment(5,by=10))

def decrement(number,by=0):
   return number - by

print(decrement(5,2))


def multiply(x,*y):  #y is a tuple here
   print(x,y)
   product=x
   for number in y:
      product*=number
   return product

print(multiply(2,4,5,6,7))

def saveUser(**user):  # this user here is a dictionary
   print(user)
   
saveUser(id=1,name="Aayush",marks=100)