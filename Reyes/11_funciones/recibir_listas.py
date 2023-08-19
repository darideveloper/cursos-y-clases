from time import sleep

def send_welcome_email (emails:list):
    """ Enviar correo de bienvenida a los nuevos usuarios

    Args:
        emails (list): lista de correos
    """

    # Recorrer lista de correos 
    for email in emails:
        # Enviar correo
        # ...
        
        # Similar envio de correo con 2 segundos de espera
        sleep (2)
        
        # Mostrar mensaje de éxito
        print (f"Correo enviado a {email}...")

# Llamar a la función con una lista de correos
emails = [
    "daideveloper@gmail.com", 
    "darialternative@gmail.com", 
    "sample@gmail.com", 
    "sample2@gmail.com"
]

send_welcome_email (emails)