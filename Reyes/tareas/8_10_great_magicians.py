# Start with a copy of your program from Exercise 8-9. 
# Write a function called make_great() 
#   that **modifies** the list of magicians by **adding** the phrase the Great to each magician’s name. 
# Call show_magicians() to see that the list has actually been modified.

def show_magicians(magicians:list[str])->str:
    """prints each name in the list of magicians.
    Args:
        names (list[str]): list of magicians names to be run through.
    """
    print ('Ladys and gentleman, I present to you the magicians, they are:')
    # loops through the list and printed each magicians names.
    for magician in magicians:
        print (f'\t{magician.title()}')
    
def make_great(magicians:list[str])->str:
    """Add 'the Great!' to each magician's name.
    Args:
        magicians (list[str]): list of magicians names to be run through.
    """
    # # Build a new list to hold the great magicians.
    # great_magicians = []
    
    # # Make each magician great, and add in to great_magicians.
    # while magicians:
    #     magician = magicians.pop()
    #     great_magician = f'the great {magician}'
    #     great_magicians.append(great_magician)
        
    # # Add the great magicians back into magicians        
    # for great_magician in great_magicians:
    #     magicians.append(great_magician)
    
    for magican in magicians:
        
        # Obtener index del mago
        index = magicians.index(magican)
        magicians[index] = f'the great {magican}'
            
#The list of magicians names it receives and prints each name.          
magicians = ['gandalf', 'sauron', 'dark magician', 'dr. fate', 'constantine']

make_great(magicians)
show_magicians(magicians)
        


        
       
        

        
    