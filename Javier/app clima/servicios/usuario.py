from .config import Config
from .mysql import MySQL

class Usuario (MySQL):
    """ Interactuar con la base de datos de usuarios, para iniciar sesión y registrarse """
    
    def __init__ (self):
        
        # Obtener credenciales
        credentials = Config()
        server = credentials.get ("server")
        database = credentials.get ("database")
        username = credentials.get ("username")
        password = credentials.get ("password")
        
        # Llamar al constructor del padre
        super().__init__ (server, database, username, password)               
    
    def login (self, name:str, password:str):
        """ Iniciar sesión en la base de datos de usuarios """
        
        
        # Consultar usuario en la base de datos
        sql = f""" SELECT * 
                FROM usuarios 
                WHERE 
                    name = '{name}' 
                    AND 
                    password = '{password}' """
                    
        user_found = self.run_sql (sql)
                
        # Verificar si el usuario fue encontrados
        if len(user_found) == 0:
            return False
        else:
            return True
        
    
    def singup (self, name:str, email:str, password:str):
        """ Añadir nuevo usuario a base de datos de usuarios """
        
        # Consultar en base de datos si ya existe un usuario con el mismo nombre o correo
        sql = f""" SELECT * 
                FROM usuarios 
                WHERE 
                    name = '{name}' 
                    OR 
                    email = '{email}' """
                    
        users_found = self.run_sql (sql)
        
        if users_found:
            return False
        
        # Sql para insertar el nuevo usuario
        sql = f""" INSERT INTO usuarios (name, email, password)
                VALUES 
                ('{name}', '{email}', '{password}')
        """
        
        try:
            # Intentar realizar sql
            self.run_sql (sql)
        except:
            # retonrar False si no se pudo realizar
            return False
        else:
            # Retunrar True si se pudo realizar
            return True