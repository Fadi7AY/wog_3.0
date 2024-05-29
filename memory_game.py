import random
import time
import app
import os
from sys import platform


def clear_screen():
    if platform.startswith('win32'):
        os.system('cls')
    else:
        os.system('clear')



def generate_sequence(difficulty):
    random_list = []
    print("\n")

    for i in range(difficulty):
        random_list.append(random.randint(1, 101))
        print(random_list[i], end=' ')
    print("\n")
    return random_list


def get_list_from_user(difficulty):
    time.sleep(0.7)
    # print("\n"*10) # this is just for now and for testing !!!
    #
    # os.system('cls')
    clear_screen() ##### addition



    user_list = []
    for i in range(difficulty):
        user_guess = input(f"Enter number {i + 1} :")
        user_list.append(app.check_condition(user_guess, 101))


    return user_list


def is_list_equal(difficulty):

    user_list=[]
    random_list=[]

    random_list = generate_sequence(difficulty)
    user_list=get_list_from_user(difficulty)


    if random_list == user_list:
        print("There is a match\n")
        return True
    print("There is NO match !!!\n")
    return False


def play(difficulty):

    # generate_sequence()
    # get_list_from_user()
    user_guess=is_list_equal(difficulty)
    if user_guess :
        return True
    return False
