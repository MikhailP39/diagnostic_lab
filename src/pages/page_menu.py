import tkinter as tk

class Menu(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        """Title."""
        lbl_ttl = tk.Label(self, text="Menu", font=("Arial Bold", 30))
        lbl_ttl.pack(side='top')

        """Buttons."""
        sep = 30
        btn_counter = tk.Button(self, text="Counter", width=10, command=lambda: controller.up_frame('Counter'))
        btn_counter.place(x=210, y=50)

        btn_quit = tk.Button(text='Quit', command=quit)
        btn_quit.place(x=770, y=610)