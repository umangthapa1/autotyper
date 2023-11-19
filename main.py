import tkinter as tk
from tkinter import ttk
import time
import threading
import keyboard

def auto_typer(text, delay_between_texts, keypress_delay, stop_event):
    time.sleep(5)

    while not stop_event.is_set():
        for char in text:
            keyboard.write(char)
            time.sleep(keypress_delay)
        keyboard.press('enter')
        time.sleep(delay_between_texts)

def start_auto_typer():
    text_to_type = entry_text.get()
    delay_between_texts = float(entry_delay.get())
    keypress_delay = 0.1 
    global stop_event 
    stop_event = threading.Event()

    global thread
    thread = threading.Thread(target=auto_typer, args=(text_to_type, delay_between_texts, keypress_delay, stop_event))
    thread.start()

def stop_auto_typer():
    if hasattr(thread, 'is_alive') and thread.is_alive():
        stop_event.set()  
        thread.join()  
        entry_delay.delete(0, tk.END)  

root = tk.Tk()
root.title("Auto Typer")

label_text = ttk.Label(root, text="Text to Type:")
label_text.grid(row=0, column=0, padx=10, pady=10, sticky=tk.W)

entry_text = ttk.Entry(root, width=30)
entry_text.grid(row=0, column=1, padx=10, pady=10)

label_delay = ttk.Label(root, text="Delay between Texts (seconds):")
label_delay.grid(row=1, column=0, padx=10, pady=10, sticky=tk.W)

entry_delay = ttk.Entry(root, width=10)
entry_delay.grid(row=1, column=1, padx=10, pady=10)

button_start = ttk.Button(root, text="Start Auto Typer", command=start_auto_typer)
button_start.grid(row=2, column=0, pady=10)

button_stop = ttk.Button(root, text="Stop Auto Typer", command=stop_auto_typer)
button_stop.grid(row=2, column=1, pady=10)

label= tk.Label(root, text="After starting switch to the Text input field in 5 seconds.")
label.grid(row=3, column=0, pady=10)

root.mainloop()
