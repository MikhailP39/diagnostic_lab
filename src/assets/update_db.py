import tkinter as tk
from tkcalendar import DateEntry
from tkinter import messagebox

from src.assets.data_base import PlateNum_DB

def update_db():
    """Window."""
    window = tk.Tk()
    window.geometry('300x200')
    """Coordinates."""
    sep = 25
    lbl_x = 10
    lbl_y = 20
    e_x = 140
    e_y = 20
    """Labels."""
    lbl_date = tk.Label(window, text='Date of Registration', font=("Arial", 10))
    lbl_date.place(x=lbl_x, y=lbl_y)
    lbl_number = tk.Label(window, text='Plate Number', font=("Arial", 10))
    lbl_number.place(x=lbl_x, y=lbl_y + sep)
    lbl_city = tk.Label(window, text='City', font=("Arial", 10))
    lbl_city.place(x=lbl_x, y=lbl_y + sep * 2)
    lbl_first_name = tk.Label(window, text='First Name', font=("Arial", 10))
    lbl_first_name.place(x=lbl_x, y=lbl_y + sep * 3)
    lbl_second_name = tk.Label(window, text='Second Name', font=("Arial", 10))
    lbl_second_name.place(x=lbl_x, y=lbl_y + sep * 4)
    """Entry Spaces."""
    e_date = DateEntry(window, selectmode='day', width=20, date_pattern='yyyy-mm-dd')
    e_date.place(x=e_x, y=e_y)
    e_number = tk.Entry(window, width=23, bd=1)
    e_number.place(x=e_x, y=e_y + sep)
    e_city = tk.Entry(window, width=23, bd=1)
    e_city.place(x=e_x, y=e_y + sep * 2)
    e_first_name = tk.Entry(window, width=23, bd=1)
    e_first_name.place(x=e_x, y=e_y + sep * 3)
    e_second_name = tk.Entry(window, width=23, bd=1)
    e_second_name.place(x=e_x, y=e_y + sep * 4)

    """Commands."""
    def submit():
        db = PlateNum_DB()
        date = e_date.get()
        if len(e_number.get()) in range(6, 8) and len(e_city.get()) > 2 and len(e_first_name.get()) > 2 and len(e_second_name.get()) > 2:
            number = e_number.get().upper()
            city = e_city.get().upper()
            first = e_first_name.get().upper()
            second = e_second_name.get().upper()
            if number.isalnum() and city.isalpha() and first.isalpha() and second.isalpha():
                item = (date, number, city, first, second)
                db.insert(item)
                messagebox.showinfo("Info", date + " " + number + " " + city + " " + first + " " + second + "\n\nAdd to Data Base")
            else:
                messagebox.showerror("Error", "The Wrong Information!\nPlease, Insert Your information in the correct form!\nThe field Plate Number must contain only letters and numbers!\nOther fields must contain only letters!\n\n")


    """Buttons."""
    btn_submit = tk.Button(window, text='Submit', command=submit)
    btn_submit.pack(side='bottom')






