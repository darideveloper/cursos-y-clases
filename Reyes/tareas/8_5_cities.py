# Write a function called describe_city() that accepts the name of a city and its country. The function should print a simple sentence, such as Reykjavik is in Iceland. Give the parameter for the country a default value. Call your function for three different cities, at least one of which is not in the default country.

def describe_city(city:str, country:str='russia'):
    """prints the name of a city and its country.
    Args:
        city (str): name of city.
        country (str, optional): name of country, default value.
    """
    print (f'{city.title()} is in {country.title()}')
    
describe_city('moscow')
describe_city('san petersburgo')
describe_city('morelos', 'mexico')