try:
    file = open("app.py")
    age = int(input("Age: "))
    # file.close() # will not be executed if above line fails
# or
    with open("app.py") as file1: # with this syntax file.close() will automatically be called
        print("")
except:
    print("File not found")
finally:
    file.close()

# if an object has __enter__ and __exit__ methods, then it supports context mgmt protocol 
# and can be used with "with" syntax like we used for file object above

try:
    with open("app.py") as file1,open("app2.py") as file2:
      print("Transfer data between the 2 files")
except:
    print("file not found")