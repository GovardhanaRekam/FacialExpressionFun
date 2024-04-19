import cv2
import random
import threading
from moviepy.editor import VideoFileClip
from deepface import DeepFace
from time import time, sleep
import csv

# Load the pre-trained facial expression detection model
model = DeepFace.build_model('Emotion')

# Global variables
game_started = False
cap = None
video_files = [
    "your video file paths"
]
expressions = ['angry', 'disgust', 'fear', 'happy', 'sad', 'surprise', 'neutral']
video_thread = None  # Placeholder for video thread
paused = False  # Flag to indicate if the game is paused

# Function to detect facial expressions
def detect_expression(frame):
    try:
        predictions = DeepFace.analyze(frame, actions=['emotion'])
        if isinstance(predictions, list) and predictions:
            dominant_emotion = predictions[0]['dominant_emotion']
            dominant_percentage = predictions[0]['emotion'][dominant_emotion]
            return dominant_emotion, dominant_percentage
        else:
            return None, None
    except ValueError:
        return None, None

# Function to write game data to CSV file
def write_to_csv(player_name, expressions_shown, expressions_matched, score):
    with open('game_data.csv', mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([player_name, expressions_shown, expressions_matched, score])

# Function to play random video
def play_random_video():
    while video_thread.is_alive():  # Ensure the thread runs while it's alive
        # Choose a random video from the list
        video_path = random.choice(video_files)
        video_clip = VideoFileClip(video_path)

        # Play the video along with its sound
        video_clip.preview()

        # Remove the played video from the list
        video_files.remove(video_path)

        # Check if all videos have been played
        if not video_files:
            # Reset the list to the original
            video_files.extend([
                "your video file paths"
            ])

# Function to start the game
def start_game():
    global game_started
    global cap
    global video_thread
    global paused

    cap = cv2.VideoCapture(0)
    expressions = ['angry', 'disgust', 'fear', 'happy', 'sad', 'surprise', 'neutral']
    game_started = False
    game_start_time = 0
    game_duration = 10  # Duration of the game in seconds
    score = 0
    expressions_matched = 0
    expressions_shown = []  # List to store expressions shown by the player
    player_name = input("Enter player name (type 'quit' to exit): ")

    if player_name.lower() == 'quit':
        return

    # Start the video thread if not already running
    if not video_thread or not video_thread.is_alive():
        video_thread = threading.Thread(target=play_random_video)
        video_thread.start()

    # Start the game loop
    while True:
        ret, frame = cap.read()

        if not ret:
            break

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        expression, percentage = detect_expression(frame)

        if expression is not None and not game_started:
            game_started = True
            game_start_time = time()
            if expressions:
                random_expression = random.choice(expressions)
            else:
                write_to_csv(player_name, expressions_shown, expressions_matched, score)
                print("No expressions left. Game Over!")
                break

        if game_started and time() - game_start_time < game_duration:
            if not paused:
                if expressions:
                    cv2.putText(frame, f"Expression: {random_expression} ", (34,39), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
                    cv2.putText(frame, f"Kept Expression:{expression} time :{-1*game_start_time + time()}", (39, 86), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
                else:
                    write_to_csv(player_name, expressions_shown, expressions_matched, score)
                    print("No expressions left. Game Over!")
                    break

                if expression == random_expression:
                    score += 10
                    expressions_matched += 1
                    expressions_shown.append(expression)
                    expressions.remove(random_expression)
                    if expressions:
                        random_expression = random.choice(expressions)
                    else:
                        write_to_csv(player_name, expressions_shown, expressions_matched, score)
                        print("No expressions left. Game Over!")
                        break
                    game_start_time = time()

                cv2.putText(frame, f"Score: {score}", (50, 100), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

        elif game_started and time() - game_start_time >= game_duration:
            if not paused:
                if expressions:
                    cv2.putText(frame, f"{random_expression} deleted", (22, 160), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
                    expressions.remove(random_expression)
                    if expressions:
                        random_expression = random.choice(expressions)
                    else:
                        write_to_csv(player_name, expressions_shown, expressions_matched, score)
                        print("No expressions left. Game Over!")
                        break
                    game_start_time = time()
                else:
                    print("Game Over! Final Score:", score)
                    write_to_csv(player_name, expressions_shown, expressions_matched, score)
                    break

        # Display the video frame
        cv2.imshow('Video', frame)

        key = cv2.waitKey(1)
        if key == ord('q'):
            break
        elif key == ord(' '):  # Toggle pause state on spacebar press
            paused = not paused
            if paused:
                print("Game Paused")
            else:
                print("Game Resumed")

    # Release the video capture object
    cap.release()

# Function to start the game and play video
def start_game_and_video():
    while True:
        # Start the game
        start_game()

        # Stop the video thread if running
        if video_thread and video_thread.is_alive():
            video_thread.join()

if __name__ == '__main__':
    start_game_and_video()




