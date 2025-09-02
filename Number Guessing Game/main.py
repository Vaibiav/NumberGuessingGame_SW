def display_title():
    print("=====================================")
    print("  VNIT Nagpur - Software Lab III")
    print("  CSP300 - Project: Number Guessing Game")
    print("  Programming Specifications:")
    print("  - Python project with functions")
    print("  - Track tasks in Jira")
    print("  - Random number guessing game")
    print("=====================================\n")

import random

def play_game():
    number_to_guess = random.randint(1, 10)
    guess = 0
    while guess != number_to_guess:
        guess = int(input("Enter your guess (1-10): "))
        if guess < number_to_guess:
            print("Too low")
        elif guess > number_to_guess:
            print("Too high")
        else:
            print("You guessed it!")
    print("Game over!\n")

def main():
    display_title()
    play_again = "yes"
    while play_again.lower() == "yes":
        play_game()
        play_again = input("Do you want to play the game again? (yes/no): ")
    print("Thank you for playing!")

if __name__ == "__main__":
    main()
