# Start with your work from Exercise 8-10. 
# Call the function make_great() with a copy of the list of magicians’ names. Because the original list will be unchanged, 
# return the new list and store it in a separate list. 
# Call show_magicians() with each list to show that you have one list of the original names and one list with the Great added to each magician’s name.

def show_magicians(magicians:list[str])->str:
    """prints each name in the list of magicians
    Args:
        names (list[str]): list of magicians names to be run through
    """
    print ('Ladys and gentleman, I present to you the magicians, they are:')
    # loops through the list and printed each magicians names.
    for magician in magicians:
        print (f'\t{magician.title()}')
    
def make_great(magicians:list[str])->str:
    """Add 'the Great!' to each magician's name and return de value.
    Args:
        magicians (list[str]): list of magicians names to be run through.
    """
    # # Build a new list to hold the great magicians
    # great_magicians = []
    # # Make each magician great, and add in to great_magicians    
    # while magicians:
    #     magician = magicians.pop()
    #     great_magician = f'the great {magician}'
    #     great_magicians.append(great_magician)
    # # Add the great magicians back into magicians        
    # for great_magician in great_magicians:
    #     magicians.append(great_magician)
    # # return de value (list)
    # return magicians    
    
    for magican in magicians:
        
        # Obtener index del mago
        index = magicians.index(magican)
        magicians[index] = f'the great {magican}'
        
    return magicians
    
#The list of magicians names it receives and prints each name.              
magicians = ['gandalf', 'sauron', 'dark magician', 'dr. fate', 'constantine']

# Calls function with copy of the list without altering the original list.
print ('\nGreat magicians:')
great_magicians = make_great(magicians[:])
show_magicians(great_magicians)

# Calls function with the original list.
print ('\nOriginal magicians:')
show_magicians(magicians)

    
    


    



