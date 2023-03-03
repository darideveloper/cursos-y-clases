# Add an if test to hello_admin.py to make sure the list of users is not empty.
# • If the list is empty, print the message We need to find some users!
# • Remove all of the usernames from your list, and make sure the correct message is printed.

users_names = []

for user_name in users_names:
    if user_name == 'admin':
        print (f'Hello {user_name.title()}!, would you like to see a status report?')
    else:
        print (f'Hello {user_name.title()}, thanks for logging in again.') 
else:
    print ('We need to find some users!')        