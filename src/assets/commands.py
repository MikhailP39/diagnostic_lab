import tkinter as tk
from tkinter import filedialog
from PIL import ImageTk, Image
import cv2

def open_img(self):
    file_img = tk.filedialog.askopenfilename(filetypes=[
        ('JPG files', '*.jpg'),
        ('PNG files', '*.png')])
    if len(file_img) > 0:
        img = cv2.imread(file_img)
        update_img(self, img)

def update_img(self, frame):
    cv2_img = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    img = Image.fromarray(cv2_img)
    img = img.resize((600, 555), Image.ANTIALIAS)
    img_tk = ImageTk.PhotoImage(image=img)
    lbl_img = tk.Label(self, image=img_tk)
    lbl_img.img_tk = img_tk
    lbl_img.place(x=200, y=50)