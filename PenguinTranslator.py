from pynput import keyboard
import pyperclip
import googletrans
import notify2
import time

# Initialize notify2
notify2.init("Translation")


def translate_text(selected_text):
    # Translate text to Ukrainian
    translator = googletrans.Translator()
    translated_text = translator.translate(selected_text, dest='uk').text

    # Display translation as notification with adjusted timeout
    display_translation(translated_text)

def display_translation(translated_text):
    

    # Create a notification
    notification = notify2.Notification("Translation", translated_text)
    notification.set_timeout(10000)  # Set timeout 
    notification.show()

def launch_translation_script():
    # Example of fetching text from clipboard (replace with actual clipboard handling logic)
    selected_text = pyperclip.paste()

    if not selected_text.strip():
        print("No text selected!")
        return

    # Translate and display the text
    translate_text(selected_text)

def on_press(key):
    try:
        if key == keyboard.Key.alt_r:
            print("Alt pressed, performing action")
            launch_translation_script()

    except AttributeError:
        pass

def on_release(key):
    if key == keyboard.Key.alt:
        print("Alt released")

def main():
    print("Listening for alt shortcut... Press alt to trigger.")

    with keyboard.Listener(
        on_press=on_press,
        on_release=on_release) as listener:
        listener.join()

if __name__ == "__main__":
    main()
