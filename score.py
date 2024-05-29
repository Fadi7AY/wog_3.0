
import os
from utils import SCORES_FILE_NAME, BAD_RETURN_CODE

def add_score(difficulty):
    try:
        # Read the current score from the scores file
        if os.path.exists(SCORES_FILE_NAME):
            with open(SCORES_FILE_NAME, 'r') as file:
                current_score = int(file.read())
        else:
            current_score = 0

        # Calculate the points for winning
        POINTS_OF_WINNING = (difficulty * 3) + 5
        new_score = current_score + POINTS_OF_WINNING

        # Write the new score to the scores file
        with open(SCORES_FILE_NAME, 'w') as file:
            file.write(str(new_score))

    except Exception as e:
        print(f"An error occurred while updating the score: {e}")
        return BAD_RETURN_CODE

    return new_score


