def borrar_tablas (tablas:list) -> list:
    """ Eliminar tablas de la base de datos

    Args:
        tablas (list): nombre de las tablas a eliminar
        
    Return:
        list: status de las tablas eliminadas
    """
    
    status = []
    
    for tabla in tablas:
        print(f'Borrando tabla {tabla}...')
        
        status.append ("ok")
    
    return status
    
tabla_a_borrar = ["usuarios", "productos", "ventas"]
status = borrar_tablas (tabla_a_borrar)
print (status)