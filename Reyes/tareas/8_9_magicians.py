# Make a list of magician’s names. Pass the list to a function called show_magicians(), which prints the name of each magician in the list.

def show_magicians(magicians:list[str])->str:
    """prints each name in the list of magicians
    Args:
        names (list[str]): list of magicians names to be run through
    """
    print ('Ladys and gentleman, I present to you the magicians, they are:')
    # loops through the list and printed each magicians names.
    for magician in magicians:
        print (f'\t{magician.title()}')
    
    
# the list of magicians names it receives and prints each name.
magicians = ['gandalf', 'sauron', 'dark magician', 'dr. fate', 'constantine']
show_magicians(magicians)


        
