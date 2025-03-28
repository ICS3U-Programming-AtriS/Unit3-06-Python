#!/usr/bin/env python3
# Created By: Atri Sarker
# Date: March 27, 2025
# Random Number Guessing Game With Error handling

import random


def main():
    # Generate a random number between 0 and 9 [INCLUSIVE]
    correct_num = random.randint(0, 9)

    # Get the user's guess as a string
    user_input = input("Enter a number (0-9): ")

    try:
        # Convert the user's guess to an integer
        user_num = int(user_input)

        # Check if the user's guess is the same as the correct number
        if user_num == correct_num:
            # Tell the user that they guessed correctly
            print("You guessed correctly!")
        # If it isn't, tell the user that they guessed wrong
        else:
            # Tell the user that they guessed wrong
            # Also tell them the correct answer
            print(f"Wrong! The correct answer was {correct_num}.")
    except ValueError:
        # Tell the user that their input wasn't an integer
        print(f"{user_input} is not an integer.")


if __name__ == "__main__":
    main()
