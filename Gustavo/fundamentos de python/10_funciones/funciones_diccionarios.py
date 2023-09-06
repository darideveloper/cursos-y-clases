def obtener_datos_urls_list (urls:list) -> dict:
    """ Obtener información de las urls usando el api ....

    Args:
        urls (list): lista de urls a consultar
        
    Return:
        list: información de las urls obteneida de la api
    """
    
    status = []
    
    for url in urls:
        
        # TODO: Obtener información de la url usando el api ...
        print(f'Obteniendodatos de la url {url}...')
        
        # TODO: Procesar información
        
        data = {
            "url": url,
            "estatus": "ok",
            "message": "Tabla eliminada correctamente",
            "clicks_dia": 221,
            "impresiones": 125,
        }
        status.append (data)
        
    return status
    
status = obtener_datos_urls_list (["https://www.google.com", "https://www.facebook.com", "https://www.youtube.com"])
print (status)


def obtener_datos_urls_dic (urls:list) -> dict:
    """ Obtener información de las urls usando el api ....

    Args:
        urls (list): lista de urls a consultar
        
    Return:
        dict: información de las urls obteneida de la api
    """
    
    status = {}
    
    for url in urls:
        
        # TODO: Obtener información de la url usando el api ...
        print(f'Obteniendodatos de la url {url}...')
        
        # TODO: Procesar información
        
        status[url] = {
            "estatus": "ok",
            "message": "Tabla eliminada correctamente",
            "clicks_dia": 221,
            "impresiones": 125,
        }
        
    return status
    
status = obtener_datos_urls_dic (["https://www.google.com", "https://www.facebook.com", "https://www.youtube.com"])
print (status)