# Start with the program you wrote for Exercise 6-1 (page 102).
# Make two new dictionaries representing different people, and store all three dictionaries in a list called people. Loop through your list of people. As you loop through the list, print everything you know about each person.


people = [
    {
        'first_name': 'luke',
        'last_name': 'jaeger',
        'age': 45,
        'city_live': 'seattle',
    },
    {
        'first_name': 'justin',
        'last_name': 'gaethje',
        'age': 33,
        'city_live': 'phoenix',
    },
    {
        'first_name': 'satoshi',
        'last_name': 'nakamoto',
        'age': 71,
        'city_live': 'unknown',
    },
]
print('The list of people is:')
for person in people:
    first_name = person['first_name']
    last_name = person['last_name']
    age = person['age']
    city = person['city_live']
    print(f'\nName: {first_name} {last_name}')
    print(f'\tAge: {age}')
    print(f'\tCity: {city}')
