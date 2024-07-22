import customtkinter as ctk
from settings import *
try:
    from ctypes import windll, byref, c_int, sizeof
except:
    pass

class App(ctk.CTk):
    def __init__(self):
        
        # window setup
        super().__init__(fg_color=GREEN)
        self.title('')
        self.iconbitmap('empty.ico')
        self.geometry('400x400')
        self.resizable(False, False)
        self.change_title_bar_color()
        
        self.mainloop()
        
    def change_title_bar_color(self):
        try:
            HWND = windll.user32.GetParent(self.winfo_id())
            windll.dwmapi.DwmSetWindowAttribute(HWND, 
                                                DWMWA_ATTRIBUTE, 
                                                byref(c_int(TITLE_HEX_COLOR)),
                                                sizeof(c_int))
        except:
            pass
        
        
if __name__ == '__main__':
    App()