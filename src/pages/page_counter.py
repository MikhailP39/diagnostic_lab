import tkinter as tk

class Counter(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        """Title."""
        lb_ttl = tk.Label(self, text="Counter", font=("Arial Bold", 30))
        lb_ttl.pack(side='top')

        """Buttons."""
        btn_menu = tk.Button(self, text='Menu', command=lambda: controller.up_frame("Menu"))
        btn_menu.place(x=725, y=610)