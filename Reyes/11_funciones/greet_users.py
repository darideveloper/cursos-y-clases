def greet_users(names:list):
    """ Saludar a un pinche usuario mamón

    Args:
        names (list): lista de pinches usuarios culeros 
    """
    for name in names:
        msg = "Hello, " + name.title() + "!"
        print(msg)

usernames = ['hannah', 'ty', 'margot']
greet_users(usernames)