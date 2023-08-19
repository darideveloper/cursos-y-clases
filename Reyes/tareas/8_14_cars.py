# Write a function that stores information about a car in a dictionary. 
# The function should always receive a manufacturer and a model name. 
# It should then accept an arbitrary number of keyword arguments. 
# Call the function with the required information and two other name-value pairs, such as a color or an optional feature. Your function should work for a call like this one: 
# car = make_car('subaru', 'outback', color='blue', tow_package=True)
#Print the dictionary that’s returned to make sure all the information was stored correctly.

def make_car(manufacturer:str, model_name:str, **additional_info:str)->dict:
    """Build a dictionary containing everything we know about a car.
    Args:
        manufacturer (str): manufacturer name.
        model_name (str): the model car.
    Returns:
        dict: contains information about car with arbitrary number
        of keyword arguments.
    """
    car = {}
    car['manufacturer'] = manufacturer.title()
    car['model name'] = model_name.title()
    for key, value in additional_info.items():
        car[key] = value.title()
    # returns the value.
    return car

# calls the function, using keyword arguments.
car = make_car('mercedes benz', 'clase e', motor= 'gasoline', transmission= 'automatic')
print (car)
car = make_car('tesla', 'model y', motor= 'electric', transmission= 'automatic', color='black')
print (car)
    