# Use a dictionary to store people’s favorite numbers. Think of five names, and use them as keys in your dictionary. Think of a favorite  number for each person, and store each as a value in your dictionary. Print  each person’s name and their favorite number. For even more fun, poll a few  friends and get some actual data for your program.

peoples_favorite_numbers = { 
    'cris': 8,
    'adriatique': 13,
    'carlos': 9,
    'mayte': 10,
    'cami': 6,
}
#este es mi primer intento de codigo:
#for people in peoples_favorite_numberºs:
    #print (f'The favorite number of {people} is {peoples_favorite_numbers[people]}')
for name, number in peoples_favorite_numbers.items():
    print (f'The favorite number of {name.title()} is {number}')    