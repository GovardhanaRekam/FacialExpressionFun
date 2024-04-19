# ExpressMimic 🎭

ExpressMimic is a fun game where you mimic facial expressions detected by your webcam! 🚀

## How it Works

1. **Start the Game**: Run the script and enter your name to begin.
2. **Mimic Expressions**: Watch the video prompts and mimic the displayed facial expressions in real-time.
3. **Score Points**: Earn points for accurate mimicry within the time limit.
4. **Game Over**: The game ends after a certain duration or when all expressions are shown.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/GovardhanaRekam/FacialExpressionFun
   cd FacialExpressionFun
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the game:
   ```bash
   python expressmimic.py
   ```

## Libraries Used

- [OpenCV](https://github.com/opencv/opencv): For capturing webcam frames and video processing.
- [MoviePy](https://github.com/Zulko/moviepy): For playing video clips.
- [DeepFace](https://github.com/serengil/deepface): For detecting facial expressions.
- [Threading](https://docs.python.org/3/library/threading.html): For parallel execution of game and video threads.
- [CSV](https://docs.python.org/3/library/csv.html): For handling game data storage.
### Game Mechanics:

1. **Starting the Game**:
    - Upon running the script, the player is prompted to enter their name to start the game.
    - Once the player enters their name, the game begins.

2. **Game Loop**:
    - The game loop consists of displaying video prompts of facial expressions captured from video files.
    - Each prompt lasts for a specific duration, during which the player needs to mimic the displayed expression.

3. **Expression Mimicry**:
    - The player watches the video prompt and mimics the facial expression shown in real-time.
    - The expression recognition system detects the player's facial expression and matches it with the prompt.

4. **Scoring**:
    - If the player accurately mimics the expression within the time limit, they earn points.
    - Points are awarded for each correctly matched expression.

5. **Game End**:
    - The game continues until either a certain duration elapses or all expressions have been shown.
    - If the player successfully mimics all expressions, they complete the game with a final score.
    - If the time limit expires or all expressions are exhausted, the game ends, and the final score is displayed.


## Acknowledgements

- ExpressMimic is inspired by the DeepFace library and various facial expression recognition projects.
- Special thanks to contributors for their valuable feedback and suggestions.

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License

[MIT](LICENSE)
