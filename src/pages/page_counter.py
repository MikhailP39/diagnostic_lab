from src.assets.interface import *

class Counter(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        """Title."""
        tk_interface(self, "Counter")

        """Labels."""
        # Number Info
        self.number = 0
        self.cnt = []
        self.lbl_num = tk.Label(self, width=10, bg='white', font=('Arial', 12), text=int(self.number))
        self.lbl_num.place(x=470, y=611)

        """Buttons."""
        btn_menu = tk.Button(self, text='Menu', command=lambda: controller.up_frame("Menu"))
        btn_menu.place(x=757, y=610)
        btn_items = tk.Button(self, text='Items', command=lambda: num_of_it(self))
        btn_items.place(x=425, y=610)