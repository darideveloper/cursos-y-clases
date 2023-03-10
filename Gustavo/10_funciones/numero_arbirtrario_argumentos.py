def borrar_tablas (tablas:list):
    """ Eliminar tablas de la base de datos

    Args:
        tablas (list): nombre de las tablas a eliminar
    """
    
    for tabla in tablas:
        print(f'Borrando tabla {tabla}...')
    
tabla_a_borrar = ["usuarios", "productos", "ventas"]
borrar_tablas (tabla_a_borrar)


def borrar_tablas_argumentos_infinitos (*tablas):
    """ Eliminar tablas de la base de datos, usando argumentos infinitos
    
    Args:
        tablas (tupla): nombre de las tablas a eliminar
    """
    
    for tabla in tablas:
        print(f'Borrando tabla {tabla}...')
    
borrar_tablas_argumentos_infinitos ("usuarios", "productos", "ventas")

def borrar_tablas_db (db_name:str, tablas:list):
    """ Eliminar tablas de una base de datos en específico

    Args:
        db_name (str): nombre de la base de datos
        tablas (list): nombre de las tablas a eliminar
    """
    
    for tabla in tablas:
        print(f'Borrando tabla {tabla} de la base de datos {db_name}...')
    
borrar_tablas_db ("db_dari", tabla_a_borrar)


def borrar_tablas_db_argumentos_infinitos (db_name:str, *tablas):
    """ Eliminar tablas de una base de datos en específico
    
    Args:
        db_name (str): nombre de la base de datos
        tablas (tupla): nombre de las tablas a eliminar
    """
    
    for tabla in tablas:
       print(f'Borrando tabla {tabla} de la base de datos {db_name}...')
    
borrar_tablas_db_argumentos_infinitos ("db_dari", "usuarios", "productos", "ventas", "daridev", "procesos", "dari dev")