import os
import app
from sys import platform

SCORES_FILE_NAME = "Scores.txt"
BAD_RETURN_CODE= 404


def clear_screen():
    if platform.startswith('win32'):
        os.system('cls')
    else:
        os.system('clear')



