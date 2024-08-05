import tkinter as tk
from tkinter import messagebox
import random

# Path to the file containing sentences
file_path = "sentence.txt"

# Reading sentences
with open(file_path, "r", encoding="utf-8") as file:
    sentences = [line.strip() for line in file]

# Shuffle the order (optional)
random.shuffle(sentences)

# Function to create the sentence mode frame
def create_sentence_mode_frame(frame):
    global current_index, current_sentence, label_sentence, entry_sentence
    current_index = 0
    current_sentence = sentences[current_index]

    # Functions
    def check_answer(event=None):
        global current_index, current_sentence
        user_answer = entry_sentence.get().strip()
        correct_answer = current_sentence.strip()

        if user_answer == correct_answer:
            label_sentence.config(bg="green")
            messagebox.showinfo("Correct", "Correct answer!")
        else:
            label_sentence.config(bg="red")
            messagebox.showerror("Incorrect", f"Incorrect answer. Correct answer: {current_sentence}")

        # Move to the next sentence
        current_index += 1
        if current_index < len(sentences):
            current_sentence = sentences[current_index]
            label_sentence.config(text=current_sentence, bg="white")
            entry_sentence.delete(0, tk.END)
        else:
            messagebox.showinfo("Congratulations", "Quiz completed!")
            entry_sentence.config(state="disabled")

    # Create widgets
    label_sentence = tk.Label(frame, text=current_sentence, font=("Helvetica", 24), bg="#1E1E1E", fg="#D4D4D4", padx=20, pady=20, relief=tk.RAISED)
    label_sentence.pack(pady=20)

    entry_sentence = tk.Entry(frame, font=("Helvetica", 18), bg="#3C3C3C", fg="#D4D4D4", insertbackground="white")
    entry_sentence.pack(pady=30, padx=20, ipadx=10, ipady=5)  # Adjusted padding and internal padding
    entry_sentence.bind('<Return>', check_answer)  # Bind Enter key to check_answer function

    button_check = tk.Button(frame, text="Check Answer", command=check_answer, font=("Helvetica", 16), bg="#007ACC", fg="#FFFFFF")
    button_check.pack(pady=20)