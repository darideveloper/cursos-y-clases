# Función básicas
def conectar_db ():
    """ Conectar con la base de datos """
    
    print ("Leyando credenciales...")
    print ("Buscando conexión...")
    print ("Conectando...")
    print ("Conexión exitosa")
    
# Invocar función 
conectado = conectar_db ()
print (conectado) # None
print ()

# Función que recibe datos
def conectar_db (usuario, password, host, nombre):
    """ Conectar con base de ddatos recibiciando las credenciales

    Args:
        usuario (str): nombre de usuario que accede a la base de datos
        password (_type_): _description_
        host (_type_): _description_
        nombre (_type_): _description_
    """
    
    print ("Leyando credenciales...")
    print ("Buscando conexión...")
    print (f"Conectando a base de datos {nombre}...")
    print ("Conexión exitosa")

conectar_db ("dari", "123213", "localhost", "db1")
print ()

# Función que recibe datos especificando el tipo
def conectar_db (usuario:str, password:str, host:str, nombre:str):
    """ Conectar con base de ddatos recibiciando las credenciales, 
    especificando el tipo de dato

    Args:
        usuario (str): nombre de usuario que accede a la base de datos
        password (str): _description_
        host (str): _description_
        nombre (str): _description_
    """
    
    print ("Leyando credenciales...")
    print ("Buscando conexión...")
    print (f"Conectando a base de datos {nombre}...")
    print ("Conexión exitosa")

conectar_db ("dari", "123213", "localhost", "db1")
print ()

# Función que recibe datos especificando el tipo y valores por defecto
def conectar_db (usuario:str, password:str, nombre:str, host:str="localhost"):
    """ Conectar con base de ddatos recibiciando las credenciales, 
    especificando el tipo de dato y valor por defecto para el host

    Args:
        usuario (str): nombre de usuario que accede a la base de datos
        password (str): _description_
        nombre (str): _description_
        host (str, optional): _description_. Defaults to "localhost".
    """
    
    print ("Leyando credenciales...")
    print ("Buscando conexión...")
    print (f"Conectando a base de datos {nombre}...")
    print (f"Conexión exitosa con el host {host}")   
    

conectar_db ("dari", "123213", "ventas") # host por defecto (localhost)
conectar_db ("dari", "123213", "ventas", "www.darideveloper.com/hgasdgsd/") # host especificado
print ()

# Función que recibe datos, especificando el tipo, valores por defecto y retorna un valor
def conectar_db (usuario:str, password:str, nombre:str, host:str="localhost") -> bool:    
    """ Conectar con base de ddatos recibiciando las credenciales, 
    especificando el tipo de dato, valor por defecto para el host y devolviendo si se pudo conectar

    Args:
        usuario (str): nombre de usuario que accede a la base de datos
        password (str): _description_
        nombre (str): _description_
        host (str, optional): _description_. Defaults to "localhost".

    Returns:
        bool: True si se pudo conectar, de lo contrario devuelve False
    """
    
    conectado = True
    
    print ("Leyando credenciales...")
    print ("Buscando conexión...")
    print (f"Conectando a base de datos {nombre}...")
    print (f"Conexión exitosa con el host {host}")
        
    return conectado    

# Guardar valor que devuleve la función
is_connected = conectar_db ("dari", "123213", "ventas")
print (is_connected)

# Utilizar el valor que devulve la función
if is_connected:
    print ("Obteniendo tabla de ususuarios")
else:
    quit ()