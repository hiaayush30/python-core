age = int(input("Enter your age\n"))

day = int(input("Enter day number\n"))

price = 12 if age >= 18 else 8

if day == 3:
    price -= 2 

print("Your ticket price is $",price) 
exit()
