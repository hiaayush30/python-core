age = input("Enter your age\n")
print(type(age)) 
age = int(age);
print("Your age is ",age)
print(type(age))

if age < 13:
    print("Child")

elif age < 18:
    print("Teen")

else:
    print("Adult")