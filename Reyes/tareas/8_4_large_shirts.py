# Modify the make_shirt() function so that shirts are large by default with a message that reads I love Python. Make a large shirt and a medium shirt with the default message, and a shirt of any size with a different message.

def make_shirt(shirt_size:str='large', printed_message:str='i love python'):
    """print the size shirt and the message printed on it.
    Args:
        shirt_size (str): size of shirt used. default 'size'.
        printed_message (str): printing message on shirt. default 'message'.
    """
    print (f'This shirt is a size {shirt_size.title()}')
    print (f'and has display nex message: {printed_message.title()}')
    
make_shirt () #large shirt with the default message.
make_shirt ('medium') #medium shirt with the default message
make_shirt('small', 'i love sex') #shirt of any size with a different message.




