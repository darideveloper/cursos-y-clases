# Start with your program from Exercise 8-7. Write a while loop that allows users to enter an album’s artist and title. Once you have that information, call make_album() with the user’s input and print the dictionary that’s created. Be sure to include a quit value in the while loop.

def make_album(artist:str, title:str, tracks:str='')->dict[str, str]:
    """Build a dictionary of information about a music album
    with a optional value.
    Args:
        artist (str): name music artist
        album (str): name music album
        number tracks (int): the number of tracks on an album(optional value)
    Returns:
        dictionary: return a dictionary with two pieces information and optional value
    """
    the_album = {'name_artist':artist.title(), 'name_album':title.title()}
    # with add optional value, run sentence for add information.
    if tracks:
        the_album['number tracks'] = tracks
    # returns the value(dictionary).
    return the_album

#Let the user know how to quit.
print ("Enter 'quit' at any time to stop.")

#Using loop While and using Input for user enter information.
while True:
    
    title = input('\nWhat album are you thinking of?: ')
    
    #Exit loop using break.
    if title == 'quit':
        break
    
    artist = input("Who's the artist?: ")
    #Exit loop using break.
    if artist == 'quit':
        break
    
    music_album = make_album(artist, title)
    print(music_album)
    
print ('\nThanks for responding')
    
    