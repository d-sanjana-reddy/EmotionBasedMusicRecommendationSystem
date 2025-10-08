import cv2
import numpy as np
from fer import FER
import pandas as pd
import pygame
import random
import requests
from io import StringIO
import tkinter as tk
from tkinter import messagebox
import os  # Import os to check file existence

# Initialize pygame for music playback
pygame.mixer.init()

# Load pre-trained emotion detector
detector = FER(mtcnn=True)

# Emotion-to-song mapping
emotion_to_song = {
    'happy': 'happy.mp3',
    'sad': 'sad.mp3',
    'angry': 'angry.mp3',
    'neutral': 'neutral.mp3',
    'fear': 'fear_song.mp3',
    'surprise': 'surprise.mp3',
    'disgust': 'disgust.mp3'
}

# Folder containing the songs
songs_folder = r"C:\Users\sanja\OneDrive\Desktop\College\IPD\IPD-4\ipd4\songs"

# Function to get song dataset from GitHub
def get_song_dataset():
    url = "https://raw.githubusercontent.com/DEAP-STEIM/DEAP-Dataset-Music/main/songs_emotion.csv"
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an error for HTTP issues
        data = StringIO(response.text)
        df = pd.read_csv(data)
        if 'emotion' not in df.columns:
            raise KeyError("The dataset is missing the 'emotion' column.")
        return df
    except requests.exceptions.RequestException as e:
        print(f"Network error while fetching dataset: {e}")
    except KeyError as e:
        print(f"Dataset error: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")
    return None  # Return None if dataset loading fails

def main():
    # Load song dataset
    songs_df = get_song_dataset()
    if songs_df is None:
        print("Using fallback sample data...")
        songs_df = pd.DataFrame({
            'song_name': ['Happy', 'Sad Song', 'Energetic', 'Calm'],
            'artist': ['Artist1', 'Artist2', 'Artist3', 'Artist4'],
            'emotion': ['positive', 'negative', 'positive', 'neutral']
        })

    # Initialize webcam
    cap = cv2.VideoCapture(0)
    dominant_emotion = None
    recommendations = None
    current_song_path = None
    is_playing = False

    def recommend_songs():
        nonlocal recommendations
        if dominant_emotion:
            # Display the song mapped to the detected emotion
            song_file = emotion_to_song.get(dominant_emotion, "No song available")
            playlist_listbox.delete(0, tk.END)  # Clear previous playlist
            playlist_listbox.insert(tk.END, f"1. {song_file}")
        else:
            messagebox.showwarning("Warning", "No emotion detected yet!")

    def play_song():
        nonlocal current_song_path, is_playing
        if not dominant_emotion:
            messagebox.showwarning("Warning", "No emotion detected yet!")
            return

        # Get the song file for the detected emotion
        song_file = emotion_to_song.get(dominant_emotion)
        if not song_file:
            messagebox.showerror("Error", f"No song mapped for emotion: {dominant_emotion}")
            return

        # Construct the full path to the song file
        current_song_path = os.path.join(songs_folder, song_file)
        if not os.path.exists(current_song_path):
            messagebox.showerror("Error", f"Could not play the song: File '{current_song_path}' not found.")
            return

        try:
            pygame.mixer.music.load(current_song_path)
            pygame.mixer.music.play()
            is_playing = True
            messagebox.showinfo("Playing Song", f"Playing: {song_file} for emotion: {dominant_emotion}")
        except Exception as e:
            messagebox.showerror("Error", f"Could not play the song: {e}")

    def pause_or_resume_song():
        nonlocal is_playing
        if is_playing:
            pygame.mixer.music.pause()
            is_playing = False
            pause_button.config(text="Resume")
        else:
            pygame.mixer.music.unpause()
            is_playing = True
            pause_button.config(text="Pause")

    # Create a GUI window
    root = tk.Tk()
    root.title("Emotion-Based Music Recommender")
    root.geometry("400x500")

    # Add a button to recommend songs
    recommend_button = tk.Button(root, text="Recommend Songs", command=recommend_songs)
    recommend_button.pack(pady=10)

    # Add a listbox to display the playlist
    playlist_listbox = tk.Listbox(root, width=50, height=10)
    playlist_listbox.pack(pady=10)

    # Add a button to play the selected song
    play_button = tk.Button(root, text="Play Selected Song", command=play_song)
    play_button.pack(pady=10)

    # Add a button to pause or resume the song
    pause_button = tk.Button(root, text="Pause", command=pause_or_resume_song)
    pause_button.pack(pady=10)

    def close_app():
        cap.release()
        cv2.destroyAllWindows()
        pygame.mixer.music.stop()
        root.destroy()

    root.protocol("WM_DELETE_WINDOW", close_app)

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        # Detect emotions
        result = detector.detect_emotions(frame)
        
        if result:
            emotions = result[0]['emotions']
            dominant_emotion = max(emotions.items(), key=lambda x: x[1])[0]
            
            # Draw emotion text on frame
            cv2.putText(frame, f"Emotion: {dominant_emotion}", 
                       (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 
                       1, (0, 255, 0), 2)

        # Display the frame
        cv2.imshow('Emotion Detection', frame)

        # Check for key press
        key = cv2.waitKey(1) & 0xFF
        if key == ord('q'):
            break

        # Update the GUI
        root.update()

    # Cleanup
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()