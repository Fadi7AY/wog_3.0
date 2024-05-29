import random
import app

def generate_number(difficulty):

    secret_number = random.randint(1, difficulty)
    return secret_number


def get_guess_from_user(difficulty):

    user_guess = input(f"Enter a guess between 1 and {difficulty}\n")
    user_guess=app.check_condition(user_guess, difficulty)
    return user_guess


def compare_results(difficulty):

    if generate_number(difficulty)==get_guess_from_user(difficulty):
        print("There is a match!")
        return True
    else :
        print("No Match")
        return False


def play(difficulty):

    # generate_number()
    # get_guess_from_user()
    guess_result = compare_results(difficulty)
    if guess_result :
        return True

    return False
