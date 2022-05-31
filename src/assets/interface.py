from src.assets.commands import *
import tkinter as tk

def tk_interface(self, title):
    """Labels."""
    # Title
    lbl_ttl = tk.Label(self, text=title, font=("Arial Bold", 30))
    lbl_ttl.pack(side='top')

    """Buttons."""
    btn_img = tk.Button(self, text='Image', command=lambda: open_img(self))
    btn_img.place(x=30, y=50)
