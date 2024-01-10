# 'This app file is used to build the GUI and make the direct relationship with its backend!

# 'Importing all frameworks

from customtkinter import CTkEntry, CTkButton, CTkLabel, CTkImage
from PIL import Image

import customtkinter 
import warnings
import PIL

# 'Importing modules and core functions

from module.core.system import _LoginSystem

# 'Mother class of the dashboard frontend

class Ui:
    
    """
        Class responsible for the application's user interface.

        The `Ui` class builds the graphical user interface (GUI) for the login application. 
        It defines the appearance of the main window, positions the visual elements and 
        manages interaction with the user.
        
        
        Constructor of the Ui class.

        Args:
            master: The application's main window.
    """

    warnings.filterwarnings("ignore", category=UserWarning)
    
    def __init__(self, master):
        
        """
            Configures the main window.
            Sets the size, title, icon, appearance and theme of the main window.
        """
        
        self.master = master
        self.master.geometry("600x440")
        self.master.title("Dashboard - Login")
        self.master.iconbitmap('assets/logo.ico')

        customtkinter.set_appearance_mode("System")
        customtkinter.set_default_color_theme("blue")

        self._loginsys = _LoginSystem()
        self.setup_ui()

    def setup_ui(self):
        
        """
            Configures the elements of the user interface.

            Creates the interface widgets, such as labels, frames, buttons, input fields and images,
            and positions them in the main window.
        """
        
        backgroundLogin = PIL.ImageTk.PhotoImage(Image.open('assets/pattern.png'))
        
        l1 = customtkinter.CTkLabel(master=self.master,image=backgroundLogin)
        l1.pack()

        frame = customtkinter.CTkFrame(master=l1,width=320,height=400,corner_radius=30)
        frame.place(relx=0.5, rely=0.5, anchor=customtkinter.CENTER)

        login_logo = CTkImage(Image.open('assets/loginlogo.png'), size=(40, 40))
        login_image = CTkLabel(master=frame, text='', image=login_logo)
        login_image.place(x=140, y=80)

        ppg_logo = PIL.ImageTk.PhotoImage(Image.open('assets/logo.png').resize((30, 30)))
        l2 = CTkLabel(master=frame, text='', image=ppg_logo)
        l2.place(x=145, y=20)

        text_login = CTkLabel(master=frame, text="Faça login em sua conta.", font=('Century Gothic', 20))
        text_login.place(x=38, y=135)

        entry_username = CTkEntry(master=frame, width=220, corner_radius=15, placeholder_text='Usuário')
        entry_username.place(x=50, y=175)

        entry_password = CTkEntry(master=frame, width=220, corner_radius=15, placeholder_text='Senha', show="*")
        entry_password.place(x=50, y=210)

        button_login = CTkButton(master=frame, font=('Century Gothic', 15), text="Login", corner_radius=100,
                                command=lambda: self._loginsys._login(entry_username.get(), entry_password.get()))

        button_create = CTkButton(master=frame, font=('Century Gothic', 15), text="Cadastrar-se", corner_radius=100,
                                command=lambda: self._loginsys._create_account(entry_username.get(), entry_password.get()))

        button_login.place(x=90, y=255)
        button_create.place(x=90, y=292)

        about = CTkLabel(master=frame, text="Protect and beautify. ®", font=('Nunito', 9))
        about.place(x=110, y=360)

    def run_app(self):
        
        """
            Starts the application's main loop.
            Starts execution of the graphical interface and keeps it active until the user closes it.
        """
        self.master.mainloop()



