# Write a function called make_album() that builds a dictionary describing a music album. 
# The function should take in an artist name and an album title, and it should return a dictionary containing these two pieces of information. Use the function to make three dictionaries representing different albums. Print each return value to show that the dictionaries are storing the album information correctly. Add an optional parameter to make_album() that allows you to store the number of tracks on an album. If the calling line includes a value for the number of tracks, add that value to the album’s dictionary. Make at least one new function call that includes the number of tracks on an album.

def make_album(artist:str, title:str, tracks:int=0)->dict:
    """_summary_

    Args:
        artist (str): _description_
        title (str): _description_
        tracks (int, optional): _description_. Defaults to 0.

    Returns:
        dict: diccionario de album
            name_artist (str): nombre del artista
            name_album (str): nombre del album
            number tracks (int): numero de canciones
    """
    
    the_album = {
        'name_artist':artist.title(), 
        'name_album':title.title()
    }
    
    # with add optional value, run sentence for add information
    if tracks:
        the_album['number_tracks'] = tracks
    # returns the values(dictionary).
    
    return the_album

music_album = make_album('all shall perish', 'awaken the dreamers')
print (music_album)
music_album = make_album('sleep terror', 'probing tranquility')
print (music_album)
music_album = make_album('all that remains', 'the fall of ideals')
print (music_album)
music_album = make_album('megadeth', 'rust in peace', tracks=9) # add optional value and printed.
print (music_album)
