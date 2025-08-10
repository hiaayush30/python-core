import random
 

user_wins = 0
computer_wins = 0

options = ["rock","paper","scissors"]

while True:
    user_input = (input("Rock/Paper/Scissors/Quit: ")).lower()
    if user_input == "q":
        print("Computer wins:",computer_wins)
        print("Your wins:",user_wins)
        break

    elif user_input in options:
        random_num = random.randint(0,2)
        computer_input = options[random_num]
        print(f"The computer chose "+computer_input+".")
        
        if computer_input == "rock" and user_input == "scissors":
            print("Computer won!")
            computer_wins +=1
        elif computer_input == "scissors" and user_input == "paper":
            print("Computer won!")
            computer_wins +=1
        elif computer_input == "paper" and user_input == "rock":
            print("Computer won!")
            computer_wins +=1
        elif computer_input == user_input:
            print("It was a tie")
        else:
            print("You won!")
            user_wins+=1
    else:
        print("Enter a valid option")

print("Good game!")