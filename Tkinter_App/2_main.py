import tkinter as tk

root = tk.Tk()
logo = tk.PhotoImage(file="shakespere.gif")

w1 = tk.Label(root, image=logo).pack(side="right")

message = """Now is the winter of our discontent made
glorious summer of this sun of york, and all the clouds
tha loured upon our household, in the deep bossom of the
ocean buried."""

w2 = tk.Label(root,
              justify=tk.LEFT,
              padx = 10,
              text=message).pack(side="left")

root.mainloop()
