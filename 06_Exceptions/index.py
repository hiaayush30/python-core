try:
    numbers = [1,2]
    print(numbers[3])
except:
    print("Index not found")

try:
    age = int(input("Age: "))
except ValueError as ex:
    print(ex)
    print(type(ex))
    print("You did't enter a valid age")
else:
    print("No exceptions were thrown")

print("Execution continues")
