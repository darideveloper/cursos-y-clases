def query_table (table_name:str) -> tuple:
    """ Consultar columnas de una tabla de la base de datos

    Args:
        table_name (str): tabla a consultar

    Returns:
        tuple: columnas de la tabla
    """
    
    # Simular consulta a la base de datos
    if table_name == "clientes":
        columns = ("id", "nombre", "apellido", "email", "telefono", "ultima venta")
    elif table_name == "usuarios":
        columns = ("id", "nombre", "apellido", "email", "password", "departamento")
    else:
        columns = ()
    
    # Devolver datos
    return columns


cols = query_table ("ventas")
print (cols)