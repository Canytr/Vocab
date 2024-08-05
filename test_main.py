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

def create_button(parent, text, command, bg_color, fg_color):
    button = tk.Button(parent, text=text, command=command, bg=bg_color, fg=fg_color, font=("Segoe UI", 20),
                       bd=0, relief='flat', padx=20, pady=10)
    button.pack(pady=20, padx=10, fill='x')
    return button

# Initialize the main window
root = tk.Tk()
root.title("Learning Tool")
root.attributes('-fullscreen', True) # Make the window fullscreen
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
sidebar = tk.Frame(root, bg="#333333", width=300)
sidebar.pack(side="left", fill="y")

# Modern color scheme
button_bg_color = '#007ACC'  # Blue
button_fg_color = '#FFFFFF'  # White

# Create buttons with updated colors
button_typing_test = create_button(sidebar, "Typing Test", lambda: show_frame(typing_test_frame), button_bg_color, button_fg_color)
button_voc_test = create_button(sidebar, "Voc Test", lambda: show_frame(voc_test_frame), button_bg_color, button_fg_color)
button_exit = create_button(sidebar, "Exit", quit_app, '#FF5733', button_fg_color)  # Orange for exit button

# Show the initial frame
show_frame(typing_test_frame)

# Start the main loop
root.mainloop()
