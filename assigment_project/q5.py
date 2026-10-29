# 5. Number Guessing Game
# Beginner
# Concepts: while, if-else, functions
# Requirements
#     • Generate a random number from 1 to 100.
#     • Ask the player to guess the number.
#     • Display “Too high” or “Too low.”
#     • Limit the player to seven attempts.
#     • Display the final result.
# Bonus: Add easy, medium, and hard difficulty levels with different attempt limits.


import random

def number_guess():

    number = random.randint(1,100)
    count = 0

    while count<6:
        print("------Guess the Number---------")
        user_number = int(input("Enter your Guess : "))
        if user_number == number:
            count+=1
            print(f"your Guess is Right : {number} guesses take : {count}")
            break

        elif user_number>number:
            print(f"your Guess is Too High")
            count+=1

        elif user_number<number:
            print(f"your Guess is Too Low")
            count+=1
    else:
        print("Maximun attempt Reached")

number_guess()