# main_score.py

from flask import Flask, jsonify
import os
from utils import SCORES_FILE_NAME, BAD_RETURN_CODE

app = Flask(__name__)

@app.route('/score', methods=['GET'])
def score_server():
    try:
        if os.path.exists(SCORES_FILE_NAME):
            with open(SCORES_FILE_NAME, 'r') as file:
                score = file.read()
            return f"<html><body><h1>The current score is: {score}</h1></body></html>"
        else:
            return f"<html><body><h1>Error: Scores file not found.</h1></body></html>", 404
    except Exception as e:
        return f"<html><body><h1>Error: {e}</h1></body></html>", 500

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
