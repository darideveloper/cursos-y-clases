# Ordinal numbers indicate their position in a list, such as 1st or 2nd. Most ordinal numbers end in th, except 1, 2, and 3.

# • Store the numbers 1 through 9 in a list.
# • Loop through the list.
# • Use an if-elif-else chain inside the loop to print the proper ordinal ending for each number. Your output should read "1st 2nd 3rd 4th 5th 6th 7th 8th 9th", and each result should be on a separate line.

ordinal_numbers = list (range(1, 10))

for ordinal_number in ordinal_numbers:
        
    if ordinal_number == 1:
        print (f'{ordinal_number}st')
    elif ordinal_number == 2:
        print (f'{ordinal_number}nd')
    elif ordinal_number == 3:
        print (f'{ordinal_number}rd')
        
    else:
        print (f'{ordinal_number}th')
        
   