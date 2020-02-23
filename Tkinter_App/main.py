# Creates a tikinter window and packs a widget. mainloop lets it be executed from a python file

import tkinter as tk


# creating an object 'root' as instance of class Tk
root = tk.Tk()
greeting = tk.Label(root, text="Hello Tkinter")
greeting.pack()

# This will start the blank window 
root.mainloop()
