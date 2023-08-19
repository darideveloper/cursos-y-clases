import printing_magicians
from printing_magicians import show_magicians
from printing_magicians import show_magicians as sm
import printing_magicians as pm
from printing_magicians import *

# the list of magicians names it receives and prints each name.
magicians = ['gandalf', 'sauron', 'dark magician', 'dr. fate', 'constantine']

#Call functions using differents mettods the import.
#Importing an Entire Module
printing_magicians.show_magicians(magicians)
print()
#Importing Specific Functions
show_magicians(magicians)
print()
#Using as to Give a Function an Alias
sm(magicians)
print()
#Using as to Give a Module an Alias
pm.show_magicians(magicians)
print()
#Importing All Functions in a Module
fuck_you ()