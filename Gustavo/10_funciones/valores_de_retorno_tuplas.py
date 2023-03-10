# Función que recibe datos, especificando el tipo, valores por defecto y retorna un valor
def conectar_db (usuario:str, password:str, nombre:str, host:str="localhost") -> tuple:    
    """ Conectar con base de ddatos recibiciando las credenciales, 
    especificando el tipo de dato, valor por defecto para el host y devolviendo si se pudo conectar

    Args:
        usuario (str): nombre de usuario que accede a la base de datos
        password (str): _description_
        nombre (str): _description_
        host (str, optional): _description_. Defaults to "localhost".

    Returns:
        conn: conector de la base de datos
        error: mensaje de error
        status: estado de conexión
    """

    conn = "proceso para conectar con db"
    error = ""
    status = "contectado"
    
    print ("Leyando credenciales...")
    print ("Buscando conexión...")
    print (f"Conectando a base de datos {nombre}...")        

    # Devolver varios datos
    return conn, error, status

# Obtener datos que devuelve la función por separado
conector, error_message, status_message = conectar_db ("dari", "123", "daridb")

if error_message:
    print (f"Error: {error_message}")
else:
    print ("Obteneiendo lista de usuarios...")
    sql = "select * from user where estatus = 1"
    # usuarios = conector.excute (sql)

# Desestructurar tuplas / listas (spread)
# nombres = ["dari", "gus", "maria"]
# nombre_1, nombre_2, nombre_3 = nombres