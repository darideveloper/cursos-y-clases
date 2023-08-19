# Write a function called make_shirt() that accepts a size and the text of a message that should be printed on the shirt. The function should print a sentence summarizing the size of the shirt and the message printed on it. Call the function once using positional arguments to make a shirt. Call the function a second time using keyword arguments.

# shirts of size with print message
def make_shirt(shirt_size:str, printed_message:str):
    """ Print the size shirt and the message printed on it.
    
    Args:
        shirt_size (str): size of shirt.
        printed_message (str): printing message on shirt.
    """
    print (f'This shirt is a size {shirt_size.title()}')
    print (f'and has display nex message: {printed_message.title()}')
  
# calls function with positional arguments.    
make_shirt('small', 'fucking shit')

# calls function with keyword arguments.
make_shirt(shirt_size='large', printed_message='i am heterosexual')
    