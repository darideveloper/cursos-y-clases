# Guardar la informacion de los estudiantes: 
#     matricula, nombre, apellidos, edad
# Modificar

nombres = ["Maria", "Pedro", "José", "Alberto"]
matriculas = ["M546124512", "P12654213", "j65125621", "A672167231"]
apellidos = ["Lopez", "Jimez", "Santiago", "Hernandez"]
edades = [18, 20, 25, 19]

def add_estudiante (nombre:str, matricula:str, apellido:str, edad:int):
    """ Añadir un estudiante a cada una de las listas

    Args:
        nombre (str): nombres del estudiante nuevo
        matricula (str): matricula del estudiante nuevo
        apellido (str): apellido paterno del estudiante nuevo
        edad (int): edad delestudiante nuevo
    """
    nombres.append (nombre)
    matriculas.append (matricula)
    apellidos.append (apellido)
    edades.append (edad)

def edit_estudiante (nombre:str, matricula:str, apellido:str, edad:int):
    """ Modicar los datos de un estudiante, en base a su matricula

    Args:
        nombre (str): nombres del estudiante nuevo
        matricula (str): matricula del estudiante nuevo
        apellido (str): apellido paterno del estudiante nuevo
        edad (int): edad delestudiante nuevo
    """
    
    # Localizar estudiante a modificar
    id_estudiante = matriculas.index (matricula)
    
    # Modificar los datos
    nombres[id_estudiante] = nombre
    apellidos[id_estudiante] = apellido
    edades[id_estudiante] = edad
    
add_estudiante ("valencia", "v671265721", "alk", 22)
add_estudiante ("dari", "d51451", "developer", 35)

print (f"nombres: {nombres}")
print (f"matriculas: {matriculas}")
print (f"apellidos: {apellidos}")
print (f"edades: {edades}")

edit_estudiante ("dari 2", "d51451", "dev", 16)

print ()
print (f"nombres: {nombres}")
print (f"matriculas: {matriculas}")
print (f"apellidos: {apellidos}")
print (f"edades: {edades}")