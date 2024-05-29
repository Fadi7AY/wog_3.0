# from app import start_play, welcome
# import guess_game
# import memory_game
# import currency_roulette_game
# from utils import screen_cleaner
#
# def main():
#     welcome()
#
#     while True:
#         selection, difficulty = start_play()
#
#         if selection == 1:
#             result = memory_game.play(difficulty)
#         elif selection == 2:
#             result = guess_game.play(difficulty)
#         elif selection == 3:
#             result = currency_roulette_game.play(difficulty)
#         else:
#             print("Invalid game selection.")
#
#         play_again = input("Do you want to play again? (yes/no): \n")
#         play_again = play_again.replace(" ", "").lower()
#
#         if play_again.strip() != "yes":
#             print("\nThanks for playing! Goodbye.")
#             break
#         screen_cleaner()
#
# if __name__ == "__main__":
#     main()
from app import main

if __name__ == "__main__":
    main()
