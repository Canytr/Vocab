import tkinter as tk
from tkinter import ttk
import typing_test
import voc_test

# Function to switch frames
def show_frame(frame):
    frame.tkraise()

# Function to quit the application
def quit_app():
    root.destroy()

# Initialize the main window
root = tk.Tk()
root.title("Learning Tool")
root.attributes('-fullscreen', True)  # Make the window fullscreen
root.configure(bg="#1E1E1E")

# Create a frame container
container = tk.Frame(root, bg="#252526")
container.pack(side="right", fill="both", expand=True)

# Configure the grid layout for the container frame
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
sidebar = tk.Frame(root, bg="#333333", width=300)  # Adjust width if necessary
sidebar.pack(side="left", fill="y")

style = ttk.Style()
style.configure("TButton", background="#2D2D30", foreground="#FFFFFF", font=("Segoe UI", 20))  # Increased font size
style.map("TButton",
          background=[("active", "#007ACC"), ("disabled", "#3A3A3A")],
          foreground=[("active", "#FFFFFF"), ("disabled", "#6D6D6D")])

button_typing_test = ttk.Button(sidebar, text="Typing Test", command=lambda: show_frame(typing_test_frame))
button_typing_test.pack(pady=20, padx=10, fill='x', ipady=10)  # Increased padding inside the button

button_voc_test = ttk.Button(sidebar, text="Voc Test", command=lambda: show_frame(voc_test_frame))
button_voc_test.pack(pady=20, padx=10, fill='x', ipady=10)  # Increased padding inside the button

# Add Exit button
button_exit = ttk.Button(sidebar, text="Exit", command=quit_app)
button_exit.pack(pady=20, padx=10, fill='x', ipady=10)  # Increased padding inside the button

# Show the initial frame
show_frame(typing_test_frame)

# Start the main loop
root.mainloop()
