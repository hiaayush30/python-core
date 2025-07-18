# essentially a read only list

point = (1,2)
# or 
point1 = 10,

print(type(point1))

concatenated_tuple = (1,2) + (3,4)
print(concatenated_tuple)

t1 = (1,2)*3
print(t1)

list_to_tuple = tuple([10,20,30])
print(list_to_tuple)
list_to_tuple_1 = tuple("Hello World")
print(list_to_tuple_1)


print(list_to_tuple_1[0:8])

x,y = point
print(f"{x},{y}")

if 1 in point:
    print("1 exists in point")


a = 10
b = 20
a,b = b,a  # on the right side a tuple is getting defined ie b,a => (20,10) and unpacking it on the left side
print(b)