# Tuple unlike list is immutable
tuple = ("yo","ho","so")

print(tuple[0])
print(tuple[-1])

# tuple[2]="hey" can't do it

tuple2 =  ("go","bro")

tuples= tuple + tuple2
print(tuples)

if "ho" in tuples:
    print("ho ho ho")

print(tuples.count("go"))

(yo,ho,so) = tuple
print(yo)

print(type(yo))
print(type(tuple))