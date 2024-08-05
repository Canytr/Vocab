import tkinter as tk
from tkinter import ttk
import typing_test
import voc_test

# Function to switch frames
def show_frame(frame):
    frame.tkraise()

# Initialize the main window
root = tk.Tk()
root.title("Learning Tool")
root.geometry("800x600")
root.configure(bg="#1E1E1E")

# Create a frame container
container = tk.Frame(root, bg="#252526")
container.pack(side="right", fill="both", expand=True)

# Configure the grid layout
container.grid_rowconfigure(0, weight=1)
container.grid_columnconfigure(0, weight=1)

# Frames for each page
typing_test_frame = tk.Frame(container, bg="#1E1E1E")
voc_test_frame = tk.Frame(container, bg="#1E1E1E")

for frame in (typing_test_frame, voc_test_frame):
    frame.grid(row=0, column=0, sticky="nsew")

# Initialize frames
typing_test.create_typing_test_frame(typing_test_frame)
voc_test.create_voc_test_frame(voc_test_frame)

# Sidebar menu
sidebar = tk.Frame(root, bg="#333333", width=200)
sidebar.pack(side="left", fill="y")

style = ttk.Style()
style.configure("TButton", background="#2D2D30", foreground="#FFFFFF", font=("Segoe UI", 10))
style.map("TButton",
          background=[("active", "#007ACC"), ("disabled", "#3A3A3A")],
          foreground=[("active", "#FFFFFF"), ("disabled", "#6D6D6D")])

button_typing_test = ttk.Button(sidebar, text="Typing Test", command=lambda: show_frame(typing_test_frame))
button_typing_test.pack(pady=20, padx=10, fill='x')

button_voc_test = ttk.Button(sidebar, text="Voc Test", command=lambda: show_frame(voc_test_frame))
button_voc_test.pack(pady=20, padx=10, fill='x')

# Show the initial frame
show_frame(typing_test_frame)

# Start the main loop
root.mainloop()
