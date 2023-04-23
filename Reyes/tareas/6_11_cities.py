# Make a dictionary called cities. Use the names of three cities as keys in your dictionary. Create a dictionary of information about each city and include the country that the city is in, its approximate population, and one fact about that city. The keys for each city’s dictionary should be something like country, population, and fact. Print the name of each city and all of the information you have stored about it.

# Data of cities
cities = {
    'moscow': {
        'country': 'russia',
        'population': 25121000,
        'fact': 'services ambulance number 2 in the world' 
    },
    'shenzen': {
        'country': 'china',
        'population': 17494398,
        'fact': 'the technologies city' 
    },
    'minsk': {
        'country': 'belarus',
        'population': 1995471,
        'fact': 'the gate of russia'
    }
}

# Loop cities
for city, city_info in cities.items():
    
    # Get data of cities
    country = city_info['country']
    population = city_info['population']
    fact = city_info['fact']
    
    # Print data of cities
    print (city.title())
    print (f"Country: {country.title()}")
    print (f"Population: {population}")
    print (f"Fact: {fact.title()}\n")