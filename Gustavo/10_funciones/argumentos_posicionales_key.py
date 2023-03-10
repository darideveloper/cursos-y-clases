# Función que recibe datos, especificando el tipo, valores por defecto y retorna un valor
def conectar_db (usuario:str, password:str=12345, nombre:str="database", host:str="localhost") -> bool:    
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

# Argumentos posicionales
conectar_db ("dari", "123213", "ventas", "localhost")

# Argumentos clave
conectar_db (host="localhost", password="123213", usuario="dari", nombre="ventas")

# Cmbinar Argumentos clave y posicionales
conectar_db ("dari", host="localhost", password="1212331", nombre="ventas")