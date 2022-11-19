import requests

def get_location ():
    """ obtener las coordenadas de la ip actual, con el servicio ipinfo.io

    Returns:
        list: latitud y longit de la ip
    """
    
    res = requests.get ("https://ipinfo.io/json")
    res.raise_for_status ()
    data = res.json ()    
    location = data["loc"].split (",")
    return location