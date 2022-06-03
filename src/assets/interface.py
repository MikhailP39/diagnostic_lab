from src.assets.commands import *
from src.gui.button_switch import ButtonSwitch
import tkinter as tk

def tk_interface(self, title, background):
    """Capture."""
    self.cap = None

    """Labels."""
    # Title
    lbl_ttl = tk.Label(self, text=title, font=("Arial Bold", 30), bg=background, fg='white')
    lbl_ttl.pack(side='top')
    # Options
    lbl_filter = tk.Label(self, text="Filters", font=("Arial Bold", 10), fg='blue', bg=background)
    lbl_filter.place(x=70, y=100)
    lbl_settings = tk.Label(self, text="Settings", font=("Arial Bold", 10), fg='blue', bg=background)
    lbl_settings.place(x=70, y=280)
    # Toggles Labels
    sep = 35
    lbl_gray = tk.Label(self, text="GrayScale", font=("Arial", 10), bg=background)
    lbl_gray.place(x=30, y=130)
    lbl_canny = tk.Label(self, text="Canny", font=("Arial", 10), bg=background)
    lbl_canny.place(x=30, y=130 + sep)
    lbl_dilate = tk.Label(self, text="Dilate", font=("Arial", 10), bg=background)
    lbl_dilate.place(x=30, y=130 + sep*2)
    lbl_contour = tk.Label(self, text="Contour", font=("Arial", 10), bg=background)
    lbl_contour.place(x=30, y=130 + sep*3)
    # Sliders
    sep_s = 50
    lbl_s_blur = tk.Label(self, text="GaussianBlur", font=("Arial Bold", 10), bg=background)
    lbl_s_blur.place(x=30, y=300)
    lbl_s_canny_l = tk.Label(self, text="Canny Low", font=("Arial Bold", 10), bg=background)
    lbl_s_canny_l.place(x=30, y=300 + sep_s)
    lbl_s_canny_h = tk.Label(self, text="Canny High", font=("Arial Bold", 10), bg=background)
    lbl_s_canny_h.place(x=30, y=300 + sep_s*2)
    lbl_s_kernel = tk.Label(self, text="Kernel", font=("Arial Bold", 10), bg=background)
    lbl_s_kernel.place(x=30, y=300 + sep_s*3)
    lbl_s_iteration = tk.Label(self, text="Iteration", font=("Arial Bold", 10), bg=background)
    lbl_s_iteration.place(x=30, y=300 + sep_s*4)
    # Image
    self.lbl_img = tk.Label(self, bg='#F0F0F0', width=85, height=37)
    self.lbl_img.place(x=200, y=50)
    # File Path Info
    self.lbl_f_path = tk.Label(self, text="Any file is not opened", font=("Arial", 10), bg=background)
    self.lbl_f_path.place(x=430, y=645)

    """Buttons."""
    btn_img = tk.Button(self, text='Image', command=lambda: open_img(self))
    btn_img.place(x=30, y=50)
    btn_video = tk.Button(self, text='Video', command=lambda: open_video(self))
    btn_video.place(x=74, y=50)
    btn_cam = tk.Button(self, text='Camera', command=lambda: open_cam(self))
    btn_cam.place(x=115, y=50)
    btn_ref = tk.Button(self, text='Refresh', command=lambda: refresh_img(self))
    btn_ref.place(x=30, y=620)
    btn_del = tk.Button(self, text='Delete', command=lambda: delete_img(self))
    btn_del.place(x=80, y=620)

    """Toggle Switches."""
    self.btn_sw_gray = ButtonSwitch(self,'#83CDEA')
    self.btn_sw_gray.place(x=110, y=125)
    self.btn_sw_canny = ButtonSwitch(self,'#83CDEA')
    self.btn_sw_canny.place(x=110, y=125 + sep)
    self.btn_sw_dilate = ButtonSwitch(self,'#83CDEA')
    self.btn_sw_dilate.place(x=110, y=125 + sep*2)
    self.btn_sw_contour = ButtonSwitch(self,'#83CDEA')
    self.btn_sw_contour.place(x=110, y=125 + sep*3)

    """Sliders."""
    self.var_blur = tk.IntVar()
    sl_blur = tk.Scale(self, from_=1, to=121, length=130, width=4, orient='horizontal',
                                font=('Console', 10), resolution=2, variable=self.var_blur,
                                bg=background, troughcolor='white', highlightthickness=0)
    sl_blur.place(x=30, y=320)

    self.var_canny_l = tk.IntVar()
    sl_canny_l = tk.Scale(self, from_=1, to=151, length=130, width=4, orient='horizontal',
                                font=('Console', 10), resolution=1, variable=self.var_canny_l,
                                bg=background, troughcolor='white', highlightthickness=0)
    sl_canny_l.place(x=30, y=320 + sep_s)

    self.var_canny_h = tk.IntVar()
    sl_canny_h = tk.Scale(self, from_=1, to=301, length=130, width=4, orient='horizontal',
                                font=('Console', 10), resolution=1, variable=self.var_canny_h,
                                bg=background, troughcolor='white', highlightthickness=0)
    sl_canny_h.place(x=30, y=320 + sep_s*2)

    self.var_kernel = tk.IntVar()
    sl_kernel = tk.Scale(self, from_=1, to=11, length=130, width=4, orient='horizontal',
                                font=('Console', 10), resolution=1, variable=self.var_kernel,
                                bg=background, troughcolor='white', highlightthickness=0)
    sl_kernel.place(x=30, y=320 + sep_s*3)

    self.var_iteration = tk.IntVar()
    sl_iteration = tk.Scale(self, from_=1, to=21, length=130, width=4, orient='horizontal',
                                font=('Console', 10), resolution=1, variable=self.var_iteration,
                                bg=background, troughcolor='white', highlightthickness=0)
    sl_iteration.place(x=30, y=320 + sep_s*4)





