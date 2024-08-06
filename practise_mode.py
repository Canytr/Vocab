import tkinter as tk
import threading
from gtts import gTTS
import os
import pygame

# Initialize pygame mixer
pygame.mixer.init()

# Path to the file containing words
file_path = "words.txt"
mp3_folder = "mp3_files"

# Ensure the mp3_files directory exists
os.makedirs(mp3_folder, exist_ok=True)

# Reading words
with open(file_path, "r", encoding="utf-8") as file:
    words = [line.strip().split(",") for line in file]

def create_mp3_files():
    for word, meaning in words:
        mp3_path = os.path.join(mp3_folder, f"{word}.mp3")
        if not os.path.exists(mp3_path):
            tts = gTTS(word, lang='en')
            tts.save(mp3_path)

def play_pronunciation(word):
    mp3_path = os.path.join(mp3_folder, f"{word}.mp3")
    if os.path.exists(mp3_path):
        pygame.mixer.music.load(mp3_path)
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():  # Wait for the music to finish playing
            pygame.time.Clock().tick(10)  # Sleep for a short time to avoid busy-waiting

# Function to create the practise mode frame
def create_practise_mode_frame(frame):
    global current_index, label_word, label_meaning, practise_started

    current_index = 0
    practise_started = False

    label_word = tk.Label(frame, text="", font=("Helvetica", 24), bg="#1E1E1E", fg="#D4D4D4", padx=20, pady=20, relief=tk.RAISED)
    label_word.pack(pady=20)

    label_meaning = tk.Label(frame, text="", font=("Helvetica", 18), bg="#1E1E1E", fg="#D4D4D4", padx=20, pady=20)
    label_meaning.pack(pady=20)

    def next_word():
        global current_index
        current_index += 1
        if current_index < len(words):
            current_word = words[current_index][0]
            current_meaning = words[current_index][1]
            label_word.config(text=current_word)
            label_meaning.config(text=current_meaning)
            threading.Thread(target=play_pronunciation, args=(current_word,)).start()
            frame.after(3000, next_word)  # Move to the next word after 3 seconds
        else:
            label_word.config(text="Practical completed!", fg="blue")
            label_meaning.config(text="")

    def start_practice():
        global practise_started
        if not practise_started:
            practise_started = True
            create_mp3_files()  # Create mp3 files if they don't exist
            next_word()

    # Button to start practice
    start_button = tk.Button(frame, text="Start Practice", command=start_practice, font=("Helvetica", 16), bg="#007ACC", fg="#FFFFFF")
    start_button.pack(pady=20)
