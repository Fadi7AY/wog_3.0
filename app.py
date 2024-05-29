import time
import guess_game
import memory_game
import currency_roulette_game
from utils import screen_cleaner
from score import add_score

def welcome():
    name = input("Enter your username please\n")
    print(f"Hi {name}, and welcome to the World of Games: The Epic Journey\n")

def check_condition(number, top_number):
    while True:
        if number.isdigit():
            number = int(number)
            if 1 <= number <= top_number:
                return number
        number = input(f"Invalid number, please enter a valid option 1 - {top_number}.\n")

def is_float(string):
    try:
        float(string)
        return True
    except ValueError:
        return False

def start_play():
    print("""Please choose a game to play:
    1. Memory Game - a sequence of numbers will appear for 1 second and you have to 
    guess it back.
    2. Guess Game - guess a number and see if you chose like the computer.
    3. Currency Roulette - try and guess the value of a random amount of USD in ILS """)

    selection = input("\nplease enter your selection : 1-3\n")
    selection = check_condition(selection, 3)

    difficulty = input("\nplease enter a difficulty level : 1 - 5\n")
    difficulty = check_condition(difficulty, 5)

    # Ensure that we always return the tuple
    return selection, difficulty

def main():
    welcome()

    while True:
        selection, difficulty = start_play()

        if selection == 1:
            result = memory_game.play(difficulty)
        elif selection == 2:
            result = guess_game.play(difficulty)
        elif selection == 3:
            result = currency_roulette_game.play(difficulty)
        else:
            print("Invalid game selection.")
            continue  # Go back to the start of the loop to ask for game selection again

        if result:
            add_score(difficulty)
            print("Congratulations! Your score has been updated.")
        else:
            print("Better luck next time!")

        play_again = input("Do you want to play again? (yes/no): \n").replace(" ", "").lower()
        if play_again.strip() != "yes":
            print("\nThanks for playing! Goodbye.")
            break
        screen_cleaner()

if __name__ == "__main__":
    main()
