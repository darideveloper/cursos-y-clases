# Make a list of five or more usernames, including the name 'admin'. Imagine you are writing code that will print a greeting to each user after they log in to a website. Loop through the list, and print a greeting to each user:
    
# • If the username is 'admin', print a special greeting, such as Hello admin, would you like to see a status report?
#• Otherwise, print a generic greeting, such as Hello Eric, thank you for logging in again.

users_names = ['bob', 'putricio', 'robalo', 'admin', 'plancton', 'barto' ]

for user_name in users_names:
    if user_name == 'admin':
        print (f'Hello {user_name.title()}!, would you like to see a status report?')
    else:
        print (f'Hello {user_name.title()}, thanks for logging in again.')        