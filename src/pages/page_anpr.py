from src.assets.interface import *

class ANPR(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg='#c9b4d9')
        self.controller = controller

        """Title."""
        tk_interface(self, "Automatic Number-Plate Recognition", '#c9b4d9')

        """Buttons."""
        btn_menu = tk.Button(self, text='Menu', command=lambda: controller.up_frame("Menu"))
        btn_menu.place(x=757, y=620)
