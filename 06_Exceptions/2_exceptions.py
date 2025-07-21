try:
    age = int(input("Age: "))
    xfactor = 10/age
except (ValueError,ZeroDivisionError):
    print("Not a valid number")
# except ZeroDivisionError:
#     print("Cannot divide by zero")
else:
    print("execution successfull")