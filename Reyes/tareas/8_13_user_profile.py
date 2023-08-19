# Start with a copy of user_profile.py from page 153. Build a profile of yourself by calling build_profile(), using your first and last names and three other key-value pairs that describe you.

def build_profile(first: str, last: str, **user_info: str) -> dict:
    """Build a dictionary containing everything we know about 
       a user. 
    Args:
        first (str): first name
        last (str): last name
    Returns:
        dict: contains information about user with arbitrary number and
        keyword arguments.
    """
    profile = {}
    profile['first_name'] = first.title()
    profile['last_name'] = last.title()
    for key, value in user_info.items():
        profile[key] = value.title()
    # returns the values.
    return profile


user_profile = build_profile('elias', 'reyes',
                             genre='man',
                             preference='heterosexual',
                             religion='buddhism zen')

print(user_profile)
