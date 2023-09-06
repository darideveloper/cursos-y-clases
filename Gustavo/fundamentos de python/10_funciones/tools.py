usuario = "dari dev"

# Función a utlizar desde otros archivos
def limpiar_texto (texto:str) -> str:
    """ Toma un texto y lo limpia

    Args:
        texto (str): texto a limpiar

    Returns:
        str: texto limpio
    """
    
    # Quitar espacios en blanco
    texto = texto.strip()
    
    # Remplazar caracteres innecesarios del texto
    replace_chars = {
        "$": "", # caracter original, caracter nuevo
        "!": "",
        "\n": " ",
        "-": "",
        "'": "",
        '"': "", 
    }
    for original_char, new_char in replace_chars.items():
        texto = texto.replace (original_char, new_char)
        
    return texto