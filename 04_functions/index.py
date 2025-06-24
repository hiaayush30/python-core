def myFunction():
    print("hello there from myFunction")
    
myFunction()
print(myFunction())  # all fns return None by default until you return a value
# None is an object that represents the absence of a value
print(myFunction)

def greet(fname,lname):
    return f"hello there {fname} {lname}"

message = greet("Advay","Jha")
print(message)