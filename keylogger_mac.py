from pynput.keyboard import Key, Listener
import tkinter as tk
from tkinter import messagebox
import re

# File to store the logged keys
log_file = "keystroke_log.txt"

# List of inappropriate words to detect (add any words here)
inappropriate_words = ["badword1", "badword2", "inappropriate", "fuck", "bitch", "dick", "porn"]

# Buffer to hold typed keys
typed_keys = []

# Function to show a pop-up alert for inappropriate words
def show_alert(word):
    # Set up the Tkinter root window (it's hidden, we only need the messagebox)
    root = tk.Tk()
    root.withdraw()  # Hide the root window
    messagebox.showwarning("Inappropriate Word Detected", f"Alert: {word} is inappropriate!")
    root.quit()  # Close the Tkinter window after showing the alert

# Function to handle key press
def on_press(key):
    global typed_keys
    try:
        # Convert key to string and append to the buffer
        if hasattr(key, 'char') and key.char is not None:
            typed_keys.append(key.char)
            print(f"Key pressed: {key.char}")  # Print regular keys
        else:
            # Handle special keys
            if key == Key.space:
                typed_keys.append(" ")
                print("[SPACE]")  # Print special key
            elif key == Key.enter:
                typed_keys.append("\n")
                print("[ENTER]")
            elif key == Key.tab:
                typed_keys.append("\t")
                print("[TAB]")
            elif key == Key.backspace and typed_keys:
                typed_keys.pop()
                print("[BACKSPACE]")  # Remove the last character on Backspace
            else:
                typed_keys.append(f"[{key}]")
                print(f"Special Key pressed: [{key}]")
    except Exception as e:
        print(f"Error: {e}")

    # Convert the typed keys to a string and make it lowercase for case-insensitive matching
    typed_string = "".join(typed_keys).lower()  # Convert the typed string to lowercase
    
    # Use regex to match words in the typed string, ignoring non-alphanumeric characters
    typed_words = re.findall(r'\b\w+\b', typed_string)  # Match only words (ignores punctuation)
    
    for word in typed_words:
        if word in inappropriate_words:  # Check if the word is in the inappropriate words list
            print(f"\n[ALERT] Inappropriate content detected! Word: {word}\n")
            with open(log_file, "a") as file:
                file.write(f"\n[ALERT] Inappropriate content detected! Word: {word}\n")
            show_alert(word)  # Show pop-up alert
            typed_keys.clear()  # Clear the buffer to avoid repeated alerts
            break  # Exit the loop to avoid redundant alerts

    # Write the current key to the log file
    if typed_keys:
        with open(log_file, "a") as file:
            file.write(typed_keys[-1])  # Safely write the latest key

# Function to handle key release
def on_release(key):
    # Stop the logger when ESC key is pressed
    if key == Key.esc:
        print("Keylogger stopped.")
        return False

# Start the key listener
print("Keylogger is running. Press ESC to stop.")
with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()