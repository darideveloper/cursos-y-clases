# Modify your program from Exercise 6-2 (page 102) so each person can have more than one favorite number. Then print each person’s name along with their favorite numbers.

peoples_favorite_numbers = { 
    'cris': [8, 6],
    'adriatique': [13, 9],
    'carlos': [9, 7],
    'mayte': [10, 7],
    'cami': [6, 100],
}

for name, numbers in peoples_favorite_numbers.items():
    print (f"{name} favorites numbers are:")
    for number in numbers:
        print (f"\t{number}")