import random
import sys

#When the level number is less than or equal to zero.
while True:
    try:
        level = int(input("Enter a level (positive integer): "))
        if level > 0:
            break
        else:
            print("Level cannot be zero or negative.")
            
#When the user enters string.
    except ValueError:
        print("Please enter a valid integer.")
        
#Assign the computer to pick any random number between 1 and the level entered
number = random.randint(1, level)

#The user must have 5 attempts to guess the number right and not allow guess number to be less than zero
for attempt in range(1, 6): 
    try:
        guess_number = int(input(f"Guess {attempt}: "))
        if guess_number < 0:
            sys.exit("Invalid number.")     
        if guess_number < number:          
            print("Too small!")
        elif guess_number > number:
            print("Too large!")
        else:
            print("Just right!")
            break                         
    except ValueError:
        print("Please enter a valid integer.")
        continue 
else:
    print(f"Sorry, you didn't guess the number. It was {number}.")
