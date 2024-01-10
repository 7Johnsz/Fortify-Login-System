# This is the main file, the code uses a modular structure,
# Separating the logic of the graphical interface into its own class

# 'Importing all modules/cores

from module.core.app import *

if __name__ == "__main__":
    root = customtkinter.CTk()
    app = Ui(root)
    app.run_app()
