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

## Acknowledgements

- ExpressMimic is inspired by the DeepFace library and various facial expression recognition projects.
- Special thanks to contributors for their valuable feedback and suggestions.

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License

[MIT](LICENSE)
