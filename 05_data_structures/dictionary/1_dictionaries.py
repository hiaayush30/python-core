# dictionary is a data structure in python which is basically a collection of key value pairs
# in python we can only use immutable types for the keys

point = {"x":1,"y":2}
# or

point1 = dict(x=1,y=2)  # passing key-word arguments here
point1["z"] = 20

print(point1)
print(point1["z"])



# print(point1["e"])  # will throw error
# solution
if "e" in point1:
    print(point1["e"]) 
#or
print(point1.get("e",0))

del point1["x"]

for key in point1:  
    print(f"the key is {key} and the value is {point1[key]}")

#or
print(point1.items())
for x in point1.items():   # the key here is a tuple containing key and value
    key,value = x
    print(f"the key is {key} and the value is {value}")
