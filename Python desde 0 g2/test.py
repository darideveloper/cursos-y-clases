"""Save each of the following exercises as a separate file with a name like 
name_cases.py. If you get stuck, take a break or see the suggestions in 

Appendix C.
"""

"""
2-3. Personal Message: 

    1. Use a variable to represent a person's name
    nombre = "Martin"
    2. and print a message to that person. 
    print(nombre)
    Your message should be simple, such as, “Hello Eric, would you like to learn some Python today?”
"""
# Martin
nombre = "Martin"
print(f"Hello {nombre}, would you like to learn some Python today?")

# Xavier
name = "Xavier"
print(f"Hola {name}, would you like to learn some Python today?")

"""
2-4. Name Cases: 
    1. Use a variable to represent a person's name, 
    2. and then print that person's name in lowercase, 
    3. uppercase, 
    4. and title case.
"""
#Xavier
name = "dArI"
print(name.lower())
print(name.upper())
print(name.title())

#Martin
nombre = "mArtIn"
print(nombre.lower())
print(nombre.upper())
print(nombre.title())

"""
2-5. Famous Quote: 
    1. Find a quote from a famous person you admire. 
    2. Print the quote and the name of its author.
     
    Your output should look something like the following, including the quotation marks:
    "A person who never made a mistake never tried anything new.” - Albert Einstein
"""
# Xavier
author = "Gran Sayayin Dari"
quote = "Al que madruga, se duerme en el trabajo xD"
print(f'{author} "{quote}"')
# Gran Sayayin Dari "Al que madruga, se duerme en el trabajo xD"

# Martin
texto = "El cielo es el limite"
print(f'Martin ALVA dijo: "{texto}"')


"""
2-6. Famous Quote 2: 
    1. Repeat Exercise 2-5, 
    2. but this time, represent the famous person's name using a variable called famous_person. 
    3. Then compose your message and represent it with a new variable called message. 
    4. Print your message.
"""
# Xavier
famous_person = author
message = quote
print(f'{famous_person} "{message}"')

# martin
famous_person = "Martin Alva"
mensaje = "e cielo es el limite"
print(f'{famous_person} "{mensaje}"')
# Martin Alva e cielo es el limite

"""
2-7. Stripping Names: 
    1. Use a variable to represent a person's name, and include some whitespace characters at the beginning and end of the name. 
        a. Make sure you use each character combination, "\t" and "\n", at least once.
    2. Print the name once, so the whitespace around the name is displayed. 
    3. Then print the name using each of the three stripping functions, lstrip(), 
    4. rstrip(), 
    5. and strip().
"""

# Dari
nombre = " \t  jose  \t \n \t"
print (f"--{nombre}--")
print(f"--{nombre.lstrip()}--")
print(f"--{nombre.rstrip()}--")
print(f"--{nombre.strip()}--") 

# Xavier


#martin
nombre = f"\tmartin"