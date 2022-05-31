from src.assets.interface import tk_interface
from src.assets.commands import *

class Counter(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        """Title."""
        tk_interface(self, "Counter")

        """Buttons."""
        btn_menu = tk.Button(self, text='Menu', command=lambda: controller.up_frame("Menu"))
        btn_menu.place(x=725, y=610)