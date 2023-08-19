# Write a function that accepts a list of items a person wants on a sandwich. The function should have one parameter that collects as many items as the function call provides, and it should print a summary of the sandwich that is being ordered. Call the function three times, using a different number of arguments each time.

def make_sandwich(user_name:str, *toppings:str)->tuple:
    """Summarize the pizza we are about to make and
    print the list of toppings that have been requested
    """
    print ('\nMaking a sandwich with the following toppings:')
    for topping in toppings:
        print (f'\t* {topping}')
        
#Calls the function, using a differents numbers of arguments each time.        
make_sandwich('atun', 'onion', 'peppers', 'lettuce', 'cheese')
make_sandwich('pepperoni', 'beans', 'extra cheese')
make_sandwich('beans', 'extra cheese', 'onion', 'fried chicken', 'green peppers', 'lettuce')