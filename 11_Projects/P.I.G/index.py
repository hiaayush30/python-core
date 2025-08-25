import random

def rollDice():
    return  random.randint(1,6)

print("let's roll")
rolls = 0
score = 0
while(1):
  choice = int(input("1.Roll Dice\t 2.View Score\t 3.Exit\t:"))
  if not choice.is_integer:
     print("Enter a valid input next time!")
     continue
  if choice == 3:
     break
  elif choice == 2:
     print(f"Your current score is {score} in {rolls} attempts")
  else:
     recieved = rollDice()
     print(f"you rolled {recieved}!")
     rolls +=1
     score += recieved
     if recieved == 1:
       print(f"You got a total of {score} points in {rolls} attempts!")
       break
     elif score>= 30:
       print(f"You won as you scored {score} points in {score} attempts!")
       break

print("Thank you for playing this game")