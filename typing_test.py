import tkinter as tk
from tkinter import messagebox
import random
import time

# Sample words for the typing test
words_list = ["these", "year", "add", "that", "big", "soon", "later", "give", "this", "came", "see", "put", "another", "number", "it's", "no", "few", "talk", "also", "at", "are", "world", "stop", "by"]

# Shuffle the words
random.shuffle(words_list)

# Timer variables
time_limit = 60  # in seconds

# Function to update the timer
def update_timer(label_timer, start_time, entry_word):
    elapsed_time = time.time() - start_time
    remaining_time = time_limit - int(elapsed_time)
    if remaining_time > 0:
        label_timer.config(text=f"0:{remaining_time:02d}")
        label_timer.after(1000, update_timer, label_timer, start_time, entry_word)
    else:
        messagebox.showinfo("Time's up", "The time is over!")
        entry_word.config(state="disabled")

# Function to check the word
def check_word(event=None):
    global current_word_index
    user_input = entry_word.get().strip()
    if user_input == words_list[current_word_index]:
        words_labels[current_word_index].config(fg="green")
    else:
        words_labels[current_word_index].config(fg="red")

    current_word_index += 1
    if current_word_index < len(words_list):
        entry_word.delete(0, tk.END)
    else:
        messagebox.showinfo("Completed", "You have typed all the words!")
        entry_word.config(state="disabled")

# Function to create the typing test frame
def create_typing_test_frame(frame):
    global entry_word, words_labels, current_word_index
    current_word_index = 0

    # Create a frame for words
    frame_words = tk.Frame(frame, bg="#1E1E1E")
    frame_words.pack(pady=20)

    # Display the words
    words_labels = []
    for word in words_list:
        label = tk.Label(frame_words, text=word, font=("Helvetica", 14), padx=5, pady=5, bg="#1E1E1E", fg="#D4D4D4")
        label.pack(side="left")
        words_labels.append(label)

    # Entry widget for user input
    entry_word = tk.Entry(frame, font=("Helvetica", 18), bg="#3C3C3C", fg="#D4D4D4", insertbackground="white")
    entry_word.pack(pady=20)
    entry_word.bind('<Return>', check_word)

    # Timer label
    label_timer = tk.Label(frame, text=f"1:00", font=("Helvetica", 18), bg="#1E1E1E", fg="#D4D4D4")
    label_timer.pack(pady=10)

    # Start the timer
    start_time = time.time()
    update_timer(label_timer, start_time, entry_word)
