# Creates a tikinter window and packs a widget. mainloop lets it be executed from a python file

import tkinter as tk

window = tk.Tk()
greeting = tk.Label(text="Hello Tkinter")
greeting.pack()

window.mainloop()