# class Point:
#     def __init__(self,x,y):
#         self.x=x
#         self.y=y
#     def __eq__(self, other):
#         return self.x == other.x and self.y == other.y

# p1 = Point(1,2)
# p2 = Point(1,2)
# print(id(p1))
# print(id(p2))
# print(p1.__eq__(p2))

# beter way to deal with classes having only data ->

from collections import namedtuple

Point = namedtuple("Point",["x","y"])  # first arg is the name of the new type and 2nd arg is an array of attribute names
print(Point)
p1 = Point(1,2)
p2 = Point(1,2)

print(p1 == p2)
print(p1.x) 

# these named tuples are immutable 
# p1.x = 20  X
p1 = Point(20,30)