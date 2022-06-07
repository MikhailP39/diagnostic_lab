import imutils
from src.assets.interface import *

class ANPR(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg='#c9b4d9')
        self.controller = controller

        """Separators."""
        sep = 35
        sep_s = 50
        """Coordinates"""
        lbl_sw_x = 30
        lbl_sw_y = 130
        lbl_sl_x = 30
        lbl_sl_y = 350
        btn_sw_x = 110
        btn_sw_y = 125
        sl_x = 30
        sl_y = 370

        """Labels."""
        # Title
        background = '#c9b4d9'
        tk_interface(self, "Automatic Number-Plate Recognition", background)
        # Options
        lbl_filter = tk.Label(self, text="Filters", font=("Arial Bold", 10), fg='blue', bg=background)
        lbl_filter.place(x=70, y=100)
        lbl_settings = tk.Label(self, text="Settings", font=("Arial Bold", 10), fg='blue', bg=background)
        lbl_settings.place(x=70, y=330)
        # Toggles
        lbl_gray = tk.Label(self, text="GrayScale", font=("Arial", 10), bg=background)
        lbl_gray.place(x=lbl_sw_x, y=lbl_sw_y)
        lbl_bfilter = tk.Label(self, text="BilatFilter", font=("Arial", 10), bg=background)
        lbl_bfilter.place(x=lbl_sw_x, y=lbl_sw_y + sep)
        lbl_canny = tk.Label(self, text="Canny", font=("Arial", 10), bg=background)
        lbl_canny.place(x=lbl_sw_x, y=lbl_sw_y + sep*2)
        lbl_mask = tk.Label(self, text="Mask", font=("Arial", 10), bg=background)
        lbl_mask.place(x=lbl_sw_x, y=lbl_sw_y + sep * 3)
        lbl_cropping = tk.Label(self, text="Cropping", font=("Arial", 10), bg=background)
        lbl_cropping.place(x=lbl_sw_x, y=lbl_sw_y + sep * 4)
        # Sliders
        lbl_s_iteration = tk.Label(self, text="Iteration", font=("Arial Bold", 10), bg=background)
        lbl_s_iteration.place(x=lbl_sl_x, y=lbl_sl_y)
        lbl_s_sigma = tk.Label(self, text="Sigma", font=("Arial Bold", 10), bg=background)
        lbl_s_sigma.place(x=lbl_sl_x, y=lbl_sl_y + sep_s)
        lbl_s_canny_l = tk.Label(self, text="Canny Low", font=("Arial Bold", 10), bg=background)
        lbl_s_canny_l.place(x=lbl_sl_x, y=lbl_sl_y + sep_s*2)
        lbl_s_canny_h = tk.Label(self, text="Canny High", font=("Arial Bold", 10), bg=background)
        lbl_s_canny_h.place(x=lbl_sl_x, y=lbl_sl_y + sep_s * 3)


        """Buttons."""
        btn_menu = tk.Button(self, text='Menu', command=lambda: controller.up_frame("Menu"))
        btn_menu.place(x=757, y=620)

        """Toggle Switches."""
        self.btn_sw_gray = ButtonSwitch(self, background)
        self.btn_sw_gray.place(x=btn_sw_x, y=btn_sw_y)
        self.btn_sw_bfilter = ButtonSwitch(self, background)
        self.btn_sw_bfilter.place(x=btn_sw_x, y=btn_sw_y + sep)
        self.btn_sw_canny = ButtonSwitch(self, background)
        self.btn_sw_canny.place(x=btn_sw_x, y=btn_sw_y + sep*2)
        self.btn_mask = ButtonSwitch(self, background)
        self.btn_mask.place(x=btn_sw_x, y=btn_sw_y + sep * 3)
        self.btn_cropping = ButtonSwitch(self, background)
        self.btn_cropping.place(x=btn_sw_x, y=btn_sw_y + sep * 4)


        """Sliders."""
        self.var_iteration = tk.IntVar()
        sl_iteration = tk.Scale(self, from_=1, to=21, length=130, width=4, orient='horizontal',
                                font=('Console', 10), resolution=1, variable=self.var_iteration,
                                bg=background, troughcolor='white', highlightthickness=0)
        sl_iteration.place(x=sl_x, y=sl_y)

        self.var_sigma = tk.IntVar()
        sl_kernel = tk.Scale(self, from_=1, to=31, length=130, width=4, orient='horizontal',
                             font=('Console', 10), resolution=1, variable=self.var_sigma,
                             bg=background, troughcolor='white', highlightthickness=0)
        sl_kernel.place(x=sl_x, y=sl_y + sep_s)

        self.var_canny_l = tk.IntVar()
        sl_canny_l = tk.Scale(self, from_=1, to=151, length=130, width=4, orient='horizontal',
                              font=('Console', 10), resolution=1, variable=self.var_canny_l,
                              bg=background, troughcolor='white', highlightthickness=0)
        sl_canny_l.place(x=sl_x, y=sl_y + sep_s*2)

        self.var_canny_h = tk.IntVar()
        sl_canny_h = tk.Scale(self, from_=1, to=301, length=130, width=4, orient='horizontal',
                              font=('Console', 10), resolution=1, variable=self.var_canny_h,
                              bg=background, troughcolor='white', highlightthickness=0)
        sl_canny_h.place(x=sl_x, y=sl_y + sep_s * 3)

    def update_img(self, frame):
        cv2_img = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        if self.btn_sw_gray.is_off == False:
            cv2_img = cv2.cvtColor(cv2_img, cv2.COLOR_RGB2GRAY)
        if self.btn_sw_bfilter.is_off == False:
            cv2_img = cv2.bilateralFilter(cv2_img, self.var_iteration.get(), self.var_sigma.get(), self.var_sigma.get())
        if self.btn_sw_canny.is_off == False:
            cv2_img = cv2.Canny(cv2_img, self.var_canny_l.get(), self.var_canny_h.get(), 2)

        img = Image.fromarray(cv2_img)
        img = img.resize((599, 557), Image.ANTIALIAS)
        img_tk = ImageTk.PhotoImage(image=img)
        self.lbl_img = tk.Label(self, image=img_tk)
        self.lbl_img.imgtk = img_tk
        self.lbl_img.place(x=200, y=50)

    def get_mask(self, image):
        keypoints = cv2.findContours(image.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        contours = imutils.grab_contours(keypoints)
        contours = sorted(contours, key=cv2.contourArea, reverse=True)[:10]
        location = None
        for contour in contours:
            approx = cv2.approxPolyDP(contour, 10, True)
            if len(approx) == 4:
                location = approx
                break
