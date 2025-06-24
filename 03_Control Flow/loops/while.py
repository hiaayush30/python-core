number = 5
while number>0:
    print(number)
    number -= 1
    
# while True:
#     print("yo")

# command = ""
# while command.lower()!="quit":
#     command = input(">")
#     print(command)
    
while True:
    command = input(">")
    print(command)
    if command.lower()=="quit":
        break
