# Write a function called city_country() that takes in the name of a city and its country. The function should return a string formatted like this:
        #"Santiago, Chile" 
#Call your function with at least three city-country pairs, and print the value that’s returned.

def get_city_country(city:str, country:str)->str:
    """this function takes in the name of a city-country pairs, and print the value
    that's returned.
    
    Args:
        city (str): city name
        country (str): country name
        
    Returns:
        str : city-country pairs
    """
    cities = f'\n"{city.title()}, {country.title()}"'
    #return pairs values
    return cities

city_country = get_city_country('hungria', 'budapest')
print (city_country)    
city_country = get_city_country('lisboa', 'portugal')
print (city_country)
city_country = get_city_country('copenhague', 'dinamarca')
print (city_country)    