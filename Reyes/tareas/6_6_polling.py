# Use the code in favorite_languages.py (page 104):
# • Make a list of people who should take the favorite languages poll. Include some names that are already in the dictionary and some that are not.
# • Loop through the list of people who should take the poll. If they have already taken the poll, print a message thanking them for responding. If they have not yet taken the poll, print a message inviting them to take the poll.

favorite_languages = { 
    'dari': 'python',
    'sarah': 'c',
    'edward': 'ruby',
}

#recorriendo el diccionario y usando condiciones para confirmar la lista de encuestados.
polling_people = ['edward', 'sarah', 'dari', 'urquidi', 'barto']

for person in polling_people:
    if person in favorite_languages.keys():
        print (f'Hey, {person.title()} thanks for your response.\n')
    else:
        print (f'{person.title()}, answer you fucking idiot.\n')    
    
