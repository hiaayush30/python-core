name = input("Type your name: ")
print("Welcome", name, "to this adventure")

answer = input("you are on a dirt road, it has come to an end and you can go left or right: ").lower()

if answer == "left":
    answer = input("You came across a river. You can go around it or swim across it.(swim/walk): ").lower()
    if answer == "swim":
        print("You drowned!")
    elif answer == "walk":
        print("You were shot!")
    else:
      print("Not a valid option. YOu loose")

elif answer == "right":
   answer = input("You came across a bridge, it looks wobbly, Do you want to cross it or back out.(cross/back): ").lower()
   if answer == "back":
       print("you loose!")
   elif answer == "cross":
       print("you win!")
   else:
       print("Invalid option. You loose!")
else:
    print("Not a valid option. you loose")

