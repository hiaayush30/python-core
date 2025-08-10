import random

# print(random.random())

# r = random.randrange(-5,11) # excludes 11
# r = random.randint(1,10)  # includes 10
   

print("This is a number guessing game")

top_of_range = input("Type a number: ")

if top_of_range.isdigit():
    top_of_range = int(top_of_range)
    if top_of_range <= 0:
        print("Type a number greater than zero")
        exit()
    else:
        random_number = random.randint(0,top_of_range)
        num_guesses = 0
        while True:
            guess = input("guess the  number: ")

            if not guess.isdigit():
                print("Enter a valid number")
                continue

            num_guesses += 1
            guess = int(guess)

            if guess == random_number:
                print("You guessed the right number in ",num_guesses," attempts")
                break
            elif guess > random_number:
                print("The number is lower than that!")
            else:
                print("The number is higher than that!")
else: 
    print("Enter a valid number")
    exit()