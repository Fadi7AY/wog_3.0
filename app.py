import time
import guess_game,memory_game,currency_roulette_game

def welcome():
    name=input("Enter your username please\n")
    print(f"Hi {name} , and welcome to the World of Games: The Epic Journey\n")

def check_condition(number,top_number) :  ## func to check if the input is valid
    while True:
        # number = input("\nplease enter your number\n")
        if number.isdigit():
            number = int(number)
            if 1 <= number <= top_number:
                return number

        number=input(f"Invalid number, please enter a valid option 1 -{top_number}.\n")

def is_float(string):
    try:
        float(string)
        return True
    except ValueError:
        return False

def start_play():

    #global difficulty

    print("""Please choose a game to play:
    1. Memory Game - a sequence of numbers will appear for 1 second and you have to 
    guess it back.
    2. Guess Game - guess a number and see if you chose like the computer.
    3. Currency Roulette - try and guess the value of a random amount of USD in ILS """)

    selection = input("\nplease enter your selection : 1-3\n")
    selection= check_condition(selection,3)


    difficulty = input("\nplease enter a difficulty level : 1 - 5\n")
    difficulty= check_condition(difficulty,5)

    return selection, difficulty

    # if selection == 1:
    #     memory_game.play()
    # elif selection == 2:
    #     guess_game.play()
    # elif selection == 3:
    #     currency_roulette_game.play()
    # # else:
    # #     print("Invalid game selection.")













