# Make several dictionaries, where the name of each dictionary is the name of a pet. In each dictionary, include the kind of animal and the owner’s name. Store these dictionaries in a list called pets. Next, loop through your list and as you do print everything you know about each pet.
pets = [
    {
    'name': 'pelos',
    'type': 'dog',
    'propetary': 'juanito' 
    },
    {
    'name': 'kimichin',
    'type': 'cat',
    'propetary': 'karely'
    },
    {
    'name': 'chispas',
    'type': 'nutria',
    'propetary': 'frank'
    },
    {
    'name': 'manolo',
    'type': 'cerdo',
    'propetary': 'larry'
    }
]
for pet in pets:
    for pet, info in pet.items():
        print (f'{pet}: {info}')
        #print (f'{info}')
    print ("")
        