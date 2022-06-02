import tkinter as tk
from tkinter import filedialog
from PIL import ImageTk, Image
import cv2

"""Open functions."""
def open_img(self):
    self.file_img = tk.filedialog.askopenfilename(filetypes=[
        ('JPG files', '*.jpg'),
        ('PNG files', '*.png')])
    if len(self.file_img) > 0:
        img = cv2.imread(self.file_img)
        update_img(self, img)
    else:
        delete_img(self)

def open_video(self):
    delete_img(self)
    v_path = tk.filedialog.askopenfilename(filetypes=[
        ('AVI files', '*.avi'),
        ('MP4 files', '*.mp4')])
    if len(v_path) > 0:
        self.lbl_f_path.configure(text=v_path)
        self.cap = cv2.VideoCapture(v_path)
        update_video(self)
    else:
        delete_img(self)

def open_cam(self):
    delete_img(self)
    self.cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
    self.lbl_f_path.configure(text='WebCam')
    update_video(self)

"""Update functions."""

def update_img(self, frame):
    cv2_img = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    cv2_img = cv2.GaussianBlur(cv2_img, (self.var_blur.get(), self.var_blur.get()), 0)
    if self.btn_sw_gray.is_off == False:
        cv2_img = cv2.cvtColor(cv2_img, cv2.COLOR_RGB2GRAY)
    if self.btn_sw_canny.is_off == False:
        cv2_img = cv2.Canny(cv2_img, self.var_canny_l.get(), self.var_canny_h.get(), 2)
    if self.btn_sw_dilate.is_off == False:
        cv2_img = cv2.dilate(cv2_img, (self.var_kernel.get(), self.var_kernel.get()),
                             iterations=self.var_iteration.get())
    if self.btn_sw_contour.is_off == False:
        (self.cnt, hierarchy) = cv2.findContours(cv2_img.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        cv2_img = cv2.drawContours(rgb, self.cnt, -1, (0, 255, 0), 2)
    img = Image.fromarray(cv2_img)
    img = img.resize((600, 555), Image.ANTIALIAS)
    img_tk = ImageTk.PhotoImage(image=img)
    self.lbl_img = tk.Label(self, image=img_tk)
    self.lbl_img.imgtk = img_tk
    self.lbl_img.place(x=200, y=50)

def update_video(self):
    if self.cap is not None:
        ret, frame = self.cap.read()
        if ret == True:
            update_img(self, frame)
            self.lbl_img.after(10, lambda: update_video(self))
        else:
            delete_img(self)

"""Render functions."""

def refresh_img(self):
    delete_img(self)
    img = cv2.imread(self.file_img)
    update_img(self, img)

def delete_img(self):
    if self.cap is not None:
        self.cap.release()
        self.cap = None
    self.lbl_f_path.configure(text="Any file is not opened")
    self.lbl_img.destroy()

def num_of_it(self):
    self.number = len(self.cnt)
    self.lbl_num.destroy()
    self.lbl_num = tk.Label(self, width=10, bg='white', font=('Arial', 12), text=int(self.number))
    self.lbl_num.place(x=470, y=611)