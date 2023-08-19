# Funciones para realizar las tareas del menu

def query_client ():
    """ Consultar clientes de la base de datos
    """
    
    print ("Clientes...")
    
def query_product ():
    """ Consultar producto de la base de datos
    """
    
    print ("Productos...")

    
def query_tax ():
    """ Consultar factura de la base de datos
    """
    
    print ("Facturas...")

while (True):

    print ("\nMENU: ")
    print ("1. Consultar cliente")
    print ("2. Consultar producto")
    print ("3. Consultar factura")
    print ("4. Salir")

    option = input ("Elige una opción: ")

    if option == "1":
        
        # Llamar a función
        query_client ()   
              
    elif option == "2":
        query_product ()        
    elif option == "3":
        query_tax ()
    elif option == "4":
        
        # Detener el ciclo
        print ("\tHasta luego")
        break