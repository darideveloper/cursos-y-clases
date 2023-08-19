# Put the functions for the example print_models.py in a separate file called printing_functions.py. 
# Write an import statement at the top of print_models.py, and modify the file to use the imported functions.

# importing the function module.
import printing_functions

# list to pass to functions.
unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
completed_models = []

# call the functions with the modules. 
printing_functions.print_models(unprinted_designs, completed_models)
printing_functions.show_completed_models(completed_models)