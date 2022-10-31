class Menu:
    
    def __init__ (self, nombre:str, items:list, hora_inicio:str, hora_fin:str):
        # Crear constructor de clase que recibe 4 parámetros
        
        # Inicializar atributos de clase
        self.nombre = nombre
        self.items = items
        self.hora_inicio = hora_inicio
        self.hora_fin = hora_fin
        
    def imprimir_menu (self):
        # Imprime el menú actual
        print ("El menu es el siguiente: ")
    
    def cuenta (self, items_cuenta:list):
        # Calcula y devuelve el total de la cuenta
        
        # Variable para almacenar el total de la cuenta
        total = 0
        
        # Recorrer cada item de la cuenta
        for item in items_cuenta:
            
            # Sumar el iteam actual al total
            total += self.items[item]
            
        # Devolver el total de la cuenta
        return total
    
    def __repr__ (self):
        # Representación de la instancia
        
        # Crear variable para almacenar la representación
        representacion = ""
        
        # Añadir información general (inicia con salto de linea)
        representacion += f"\nEl menu de {self.nombre} está disponible de {self.hora_inicio} a {self.hora_fin} y tiene los siguientes items: "
        
        # Añadir items del menu
        
        # Ciclo por cada item
        for nombre, precio in self.items.items():
            
            # Formatear iteam actual (inicia con salto de linea tabulación)
            item_text = f"\n\t{nombre} - {precio}"
        
            # Añsdir item actual a la representación
            representacion += item_text
        
        # Devolver mensaje
        return representacion
    
    def menu_disponible (self, hora:int):
        # Consdultar si el menu está disponible en la hora dada
        
        # Comprobar siu la hora está entre la hora de inicio y la hora de fin
        if hora >= self.hora_inicio and hora <= self.hora_fin:
            return True
        else:
            return False

class Franquicia ():
    def __init__ (self, nombre, direccion:str, menus:list):
        # Constructor de clase que recibe 3 parámetros
        
        # Inicializar atributos de clase
        self.nombre = nombre
        self.direccion = direccion
        self.menus = menus
    
    def __repr__(self):
        
        # Variable para almacenar la representación
        representacion = f"Franquicia {self.nombre} con dirección en {self.direccion} y los siguientes menus:" 
        
        # Añadir cada menu a la repesentación
        
        # Ciclo por cada menu
        for menu in self.menus:
            representacion += str(menu)
        
        return representacion
    
    def consultar_menus (self, hora):
        # Consultar los menus disponibles a imprimirlos
        
        # Mensaje inicial
        print (f"Menus disponibles a las {hora} hrs: ")
        
        # Variable para dterminar si se encontró al menos un menu
        menus_encontrados = False
        
        # Recorrer cada menu de la franquicia
        for menu in self.menus:
            
            # Si el menu está disponible, imprimirlo
            if menu.menu_disponible(hora):
                print (menu)  
                
                # Guardar que se ha encontrado un menu
                menus_encontrados = True
                
        # Mostrar mensaje de error si no hay menu disponible
        if not menus_encontrados:
            print ("No hay menus disponibles en ese horario")

# MENUS DE LAS FRANQUICIAS

# Items de ejemplo para crear el primer
items = {
    "pancakes": 150,
    "chilaquiles": 200,
    "arrachera": 300,
    "café": 20,
    "jugo": 25
}

# Crear instancia de la clase menu
desayuno = Menu("Desayuno", items, 7, 12)

# Items de ejemplo para crear el segundo menu
items = {
    "tacos": 200,
    "ensalada": 100,
    "pasta": 150,
    "refresco": 25,
    "café": 20
}

# Crear instancia de la clase menu
comida = Menu("Comida", items, 13, 17)

# Items de ejemplo para crear el segundo menu
items = {
    "nuggets": 75,
    "jugo": 25,
    "hamburgesa": 100,
    "leche": 25,
}

# Crear instancia de la clase menu
kids = Menu("Kids", items, 11, 17)

# Items de ejemplo para crear el segundo menu
items = {
    "pollo": 150,
    "ensalada": 95,
    "alitas": 1250,
    "cerveza": 50,
}

# Crear instancia de franquicia 1
fran_1 = Franquicia("McDonalds", "Av. Paseo de la Reforma 500", [desayuno, comida, kids])

# Mostrard fatos de franquicia
print (fran_1)
print ("----------------------------") # Separador

# Consultar menus en diferentes horarios 
fran_1.consultar_menus(7)
print ("----------------------------") # Separador
fran_1.consultar_menus(14)
print ("----------------------------") # Separador
fran_1.consultar_menus(19)