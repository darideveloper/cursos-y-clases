def clean_text (text:str) -> str:
    """ Clean text from special characters

    Args:
        text (str): texto original

    Returns:
        str: texto limpio
    """
    
    # Quitar caracteres adicionales
    delete_chars = ["$", "-", "'", "`", "_"]
    for char in delete_chars:
        text = text.replace(char, "")
        
    # devolver dato
    return text
    

final_text = clean_text ("AA____AAA__---AAAA")
print (final_text)