# Numbers in python have the same precision as Double in C

import random
import math
from decimal import Decimal
from fractions import Fraction

math.floor(-2.8)  
# -3

math.trunc(-2.8)
# -2 as trunc goes towards 0

x = 1 + 2j  # complex numbers

print(random.randint(10,100))
print(random.choice([2,4,6,8,10]))

l1 = [1,2,3,4,5]
random.shuffle(l1)
print(l1)


print((0.1+0.1+0.1)-0.3)
print(Decimal('0.1')+Decimal('0.1')+Decimal('0.1')-Decimal('0.3'))

myFra = Fraction(2,7)
print(myFra)

setone = {1,2,3,4}
print(setone & {2,4,6,7,8}) #intersection
print(setone | {1,6,7,9})  #union
print(setone - {1,2,3,4}) # it will not shpw {} as that is a dictionary
print(type({}))
print(type(True))
print(False is 0)

print (10/3)
print(10//3)
print(10**3)


# type conversion
x = input("x: ");
print(type(x))
x = int(x);
print(x+1)