"""
Python Web Development Techdegree
Project 1 - Number Guessing Game
--------------------------------

For this first project we will be using Workspaces. 

NOTE: If you strongly prefer to work locally on your own computer, you can totally do that by clicking: File -> Download Workspace in the file menu after you fork the snapshot of this workspace.

"""

import random


def start_game():
    welcome = print("Welcome to the Number Guessing Game")
    random_number = random.randint(1, 15)
    attempts = 1
    high_score = 0
    
    while True:
        try:
            guess_number = int(input("Please pick a number between 1 and 15: "))
            if guess_number < 1 or guess_number > 15:
                raise ValueError("Your choice must be a whole number between 1 and 15.")
            elif guess_number < random_number:
                print("It's higher")
                attempts += 1
                continue
            elif guess_number > random_number:
                print("It's lower")
                attempts += 1
                continue
            elif guess_number == random_number:
                print("You got it! It took you {} tries. The correct number was {}.".format(attempts, random_number))
                if high_score == 0 or attempts < high_score:
                    high_score = attempts
                play_again = input("Would you like to play again? (Yes/No): ")
                if play_again.lower() == 'yes':
                    print("The HIGHSCORE is {}".format(high_score))
                    attempts = 1
                    continue
        except ValueError:
            print("Oh No! That's not a valid value. Please try again...")
        else:
            print("Thank you for playing!")
            break
    
    """Psuedo-code Hints
    
    When the program starts, we want to:
    
    ------------------------------------
    1. Display an intro/welcome message to the player.
    2. Store a random number as the answer/solution.
    3. Continuously prompt the player for a guess.
      a. If the guess greater than the solution, display to the player "It's lower".
      b. If the guess is less than the solution, display to the player "It's higher".
    
    4. Once the guess is correct, stop looping, inform the user they "Got it"
         and show how many attempts it took them to get the correct number.
    5. Let the player know the game is ending, or something that indicates the game is over.
    
    ( You can add more features/enhancements if you'd like to. )
    """
#     write your code inside this function.


if __name__ == '__main__':
    # Kick off the program by calling the start_game function.
    start_game()
