import tkinter as tk
from tkinter import messagebox
import random

# Path to the file containing words and their meanings
file_path = "voc.txt"

# Reading words and meanings
with open(file_path, "r", encoding="utf-8") as file:
    words = []
    for line in file:
        word, meaning = line.strip().split(":")
        words.append((word.strip(), meaning.strip()))

# Shuffle the order
random.shuffle(words)

# Function to create the vocab test frame
def create_voc_test_frame(frame):
    global current_index, current_word, current_meaning, label_word, label_meaning, entry_translation
    current_index = 0
    current_word, current_meaning = words[current_index]

    # Functions
    def check_answer(event=None):
        global current_index, current_word, current_meaning
        user_answer = entry_translation.get().strip().lower()
        correct_answer = current_word.lower()

        if user_answer == correct_answer:
            label_word.config(bg="green")
            messagebox.showinfo("Correct", "Correct answer!")
        else:
            label_word.config(bg="red")
            messagebox.showerror("Incorrect", f"Incorrect answer. Correct answer: {current_word}")

        # Move to the next word
        current_index += 1
        if current_index < len(words):
            current_word, current_meaning = words[current_index]
            label_word.config(text=current_word, bg="white")
            label_meaning.config(text=current_meaning)
            entry_translation.delete(0, tk.END)
        else:
            messagebox.showinfo("Congratulations", "Quiz completed!")
            entry_translation.config(state="disabled")

    # Create widgets
    label_word = tk.Label(frame, text=current_word, font=("Helvetica", 24), bg="#1E1E1E", fg="#D4D4D4", padx=20, pady=20, relief=tk.RAISED)
    label_word.pack(pady=20)

    label_meaning = tk.Label(frame, text=current_meaning, font=("Helvetica", 18), bg="#1E1E1E", fg="#D4D4D4", padx=20, pady=20)
    label_meaning.pack()

    entry_translation = tk.Entry(frame, font=("Helvetica", 18), bg="#3C3C3C", fg="#D4D4D4", insertbackground="white")
    entry_translation.pack(pady=10)

    button_check = tk.Button(frame, text="Check Answer", command=check_answer, font=("Helvetica", 16), bg="#007ACC", fg="#FFFFFF")
    button_check.pack(pady=20)

    # Check answer when Enter key is pressed
    frame.bind('<Return>', check_answer)
