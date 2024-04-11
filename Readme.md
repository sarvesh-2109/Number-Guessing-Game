
# Number Guessing Game

This Flask web application allows users to play a number guessing game. The user needs to guess a number between 0 to 9, and the application will provide feedback on whether the guess is too high, too low, or correct.

## Output


## How to Play

1. Navigate to the home page ("/").
2. The user will see a message prompting them to guess a number between 0 to 9 along with an accompanying GIF image.
3. Enter a number as part of the URL to make a guess. For example, entering "/3" in the URL will make a guess that the random number is 3.
4. The application will provide feedback based on the guess:
    - If the guess is too high, a message with a GIF indicating "Too high, try again!" will be displayed.
    - If the guess is too low, a message with a GIF indicating "Too low, try again!" will be displayed.
    - If the guess is correct, a message with a GIF indicating "You found me!" will be displayed.

## Running the Application

To run the application, execute the Python script (`app.py`). Ensure you have Flask installed. You can install Flask using pip:

pip install Flask


After installing Flask, run the following command in the terminal:

```bash
python server.py
```

The application will start running on your local server. Open a web browser and navigate to `http://127.0.0.1:5000/` to access the home page and start playing the game.

## Dependencies

- Flask
- Random 
