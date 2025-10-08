# 🎵 Emotion-Based Music Recommender

An **AI-powered emotion detection and music recommendation system** that uses your **facial expressions** (captured through your webcam) to suggest and play songs that match your current mood.

It combines **computer vision**, **deep learning**, and **audio playback** for a fun and personalized experience.

---

## 🚀 Features

- 🎭 **Real-Time Emotion Detection** using webcam and the FER model  
- 🎶 **Automatic Song Recommendation** based on detected emotions  
- ▶️ **Play / Pause / Resume Controls**  
- 🪟 **Simple GUI Interface** built with Tkinter  
- 💾 **Fallback Dataset** when the online dataset is unavailable  

---

## 🧰 Tech Stack

| Component | Technology |
|------------|-------------|
| **Language** | Python |
| **Libraries** | OpenCV, NumPy, FER, Pandas, Pygame, Tkinter, Requests |
| **Emotion Detection** | [FER (Facial Emotion Recognition)](https://github.com/justinshenk/fer) |
| **Music Playback** | Pygame Mixer |
| **GUI** | Tkinter |
| **Dataset** | GitHub-hosted CSV (`songs_emotion.csv`) |

---

## 🖥️ How It Works

1. Your webcam captures your live video feed.  
2. The FER model detects your **dominant emotion** in real time.  
3. The app recommends a song based on that emotion.  
4. You can play, pause, or resume the song directly from the GUI.  

---

## 🗂️ Project Structure

Emotion-Music-Recommender/
│── main.py # Main Python script
│── songs/ # Folder containing MP3 songs
|  │── happy.mp3
|  │── sad.mp3
|  │── angry.mp3
|  │── neutral.mp3
|  │── fear_song.mp3
|  │── surprise.mp3
|  └── disgust.mp3
└── README.md # Documentation file

### Description

- `main.py`: Runs the emotion detection and music recommendation system.  
- `songs/`: Contains the MP3 files mapped to different emotions.  
- `README.md`: Provides details about the project, setup, and usage.

---

## ⚙️ Installation & Setup

### 1. Clone the Repository
```bash
git clone https://github.com/<your-username>/emotion-music-recommender.git
cd emotion-music-recommender
```

### 2. Install Dependencies
Make sure you have **Python 3.8+** installed, then run:
```bash
pip install opencv-python numpy fer pandas pygame requests
```

### 3. Add Songs
Create a folder named songs in your project directory and add the following MP3 files:
```bash
happy.mp3
sad.mp3
angry.mp3
neutral.mp3
fear_song.mp3
surprise.mp3
disgust.mp3
```

### 4. Run the Application
To start the program, run:
```bash
python main.py
```

---

## 🧠 Supported Emotions

| Emotion | Example Song |
|----------|---------------|
| 😄 Happy | `happy.mp3` |
| 😢 Sad | `sad.mp3` |
| 😡 Angry | `angry.mp3` |
| 😐 Neutral | `neutral.mp3` |
| 😨 Fear | `fear_song.mp3` |
| 😲 Surprise | `surprise.mp3` |
| 🤢 Disgust | `disgust.mp3` |

Each detected emotion automatically triggers the song mapped to it.

---

## 🪄 GUI Overview

| Button | Action |
|---------|---------|
| **Recommend Songs** | Suggests songs based on the detected emotion |
| **Play Selected Song** | Plays the recommended song for your current emotion |
| **Pause / Resume** | Pauses or resumes the currently playing song |
| **Close Window** | Stops playback, releases webcam, and closes the app safely |

---

## 🧾 Example Output

When your detected emotion is **happy**, the app displays:
```bash
Emotion: happy
Playing: happy.mp3 for emotion: happy
```
This message appears both on-screen and in the webcam window.

---

## ⚠️ Notes

- Ensure your **webcam** is properly connected and accessible.  
- The **FER** model may take a few seconds to initialize on the first run.  
- The app automatically falls back to a **local sample dataset** if the online CSV file isn’t available.  
- If your song files are in a different folder, update the `songs_folder` path in the script accordingly.  

---

## 💡 Future Improvements

- 🎧 Integrate **Spotify** or **YouTube APIs** for real-time music recommendations  
- 🧠 Add **emotion history tracking** for personalized playlists  
- 🪟 Redesign GUI with **PyQt5** or **customtkinter** for a modern look  
- 🤖 Support **mixed or blended emotions** for more accurate recommendations  

---

## 👩‍💻 Author

**Danda Sanjana Reddy (DSR)**  

---
