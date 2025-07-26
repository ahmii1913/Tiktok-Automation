import tkinter as tk
from tkinter import ttk
from threading import Thread
from main import run_bot

def start_bot_thread():
    Thread(target=run_bot).start()

root = tk.Tk()
root.title("TikTok Auto Bot")

tk.Label(root, text="Batch size (5-50):").pack()
batch_entry = tk.Entry(root)
batch_entry.insert(0, "5")
batch_entry.pack()

lang_var = tk.StringVar(value="en")
ttk.Combobox(root, textvariable=lang_var, values=["en", "ur", "hi"]).pack()

use_ai_face_var = tk.BooleanVar()
tk.Checkbutton(root, text="Use AI Face Video", variable=use_ai_face_var).pack()

start_btn = tk.Button(root, text="Start Automation", command=start_bot_thread)
start_btn.pack()

log_text = tk.Text(root, height=20)
log_text.pack()

root.mainloop()
