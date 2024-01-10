# 'This file is the GUI's backend

# 'Importing all frameworks and load dotenv

from CTkMessagebox import CTkMessagebox
from dotenv import load_dotenv

import threading
import winsound
import sqlite3
import os

load_dotenv()

class _LoginSystem:
    
    """
        Class for managing the login system.

        The `_LoginSystem` class is responsible for managing an application's login system.
        It allows users to log in and create new accounts.

        The class has two main methods:

        * `_login()`: Logs in a user.
        * `_create_account()`: Creates a new user account.
    """
    
    def __init__(self):
        self.database = os.getenv("DB_PATH")
        self._maxLength = 20

        self.thread = threading.Thread(target=lambda: winsound.PlaySound("SystemExclamation", winsound.SND_ALIAS))
        
        if not os.path.isfile(self.database):
            msg = CTkMessagebox(title="Erro",
                                message="Não foi possível estabelecer uma conexão com o banco de dados",
                                icon="warning",
                                corner_radius=20,
                                sound=self.thread)
            

            response = msg.get()
            
            if response:
                exit(1)

        if os.path.isfile(self.database):
            self.conn = sqlite3.connect(self.database)
            self.cursor = self.conn.cursor()

    def _login(self, user, pwd):
        
        """
            Logs a user in.

            The `_login()` method checks whether the credentials provided by the user are valid. If they are,
            the method displays a successful login message. Otherwise, the method displays an error message.

            Args:
                user: The user's username.
                pwd: The user's password.

            Returns:
                True if the login is successful, False otherwise.
        """
        
        if len(user) > self._maxLength or len(pwd) > self._maxLength:
            CTkMessagebox(title="Erro",
                          message="Você está enviando muitos caracteres!",
                          corner_radius=20,
                          sound=self.thread)

            return False

        if not user:
            CTkMessagebox(title="Erro",
                          message="Não é possível efetuar o login, pois há campos vazios.",
                          corner_radius=20,
                          sound=self.thread)
            
        else:
            self.cursor.execute('SELECT * FROM users WHERE username=? AND password=?', (user, pwd))
            search = self.cursor.fetchone()

            if search:
                CTkMessagebox(title="Login",
                            message="Login bem-sucedido!",
                            corner_radius=20,
                            icon="check",
                            sound=self.thread)    
            else:
                CTkMessagebox(title="Erro",
                            message="Nome de usuário ou senha incorretos.",
                            corner_radius=20,
                            icon="cancel",
                            sound=self.thread)          

    def _create_account(self, user, pwd):
        
        """
            Creates a new user account.

            The `_create_account()` method checks that the supplied username is not in use.
            If it isn't, the method creates a new user account in the database.
            Otherwise, the method displays an error message.

            Args:
                user: The user's username.
                pwd: The user's password.

            Returns:
                True if the account is successfully created, False otherwise.
        """
        
        if len(user) > 25 or len(pwd) > 25:    
            CTkMessagebox(title="Erro",
                          message="Senha ou Usuário com padrão muito grande!",
                          corner_radius=20,
                          sound=self.thread)   
            return False

        if not user:
            CTkMessagebox(title="Erro",
                          message="Não é possível efetuar o cadastro, pois há campos vazios.",
                          corner_radius=20,
                          sound=self.thread)  
        else:
            self.cursor.execute('SELECT * FROM users WHERE username=?', (user,))
            existing_user = self.cursor.fetchone()
            if existing_user:
                CTkMessagebox(title="Erro",                         
                              message="Este nome de usuário já está em uso, por favor insira outro usuário.",
                              corner_radius=20,
                              sound=self.thread)
                
                return False
                
            else:
                try:
                    self.cursor.execute(
                        '''
                        INSERT INTO users (username, password) VALUES (?, ?)
                        ''', (user, pwd))

                    self.conn.commit()
                    
                    CTkMessagebox(title="Cadastro",
                                  message="Cadastro bem-sucedido!",
                                  corner_radius=20,
                                  icon="check",
                                  sound=self.thread) 

                except Exception as e:
                    CTkMessagebox(title="Erro",
                                  message=f"Erro ao cadastrar: {str(e)}",
                                  corner_radius=20,
                                  icon="warning",
                                  sound=self.thread) 

                    
