#Think of at least five places in the world you’d like to visit:
#Store the locations in a list. Make sure the list is not in alphabetical order.
#Print your list in its original order. Don’t worry about printing the listneatly,just print it as a raw Python list.
my_favorite_country = ['rusia', 'portugal', 'alemania', 'taiwan', 'españa']
print (my_favorite_country)
print()
#Use sorted() to print your list in alphabetical order without modifying the actual list.
print ( sorted(my_favorite_country))
print()

#Show that your list is still in its original order by printing it.
print (my_favorite_country)
print()
#Use sorted() to print your list in reverse alphabetical order without changing the order of the original list.
print ( sorted (my_favorite_country, reverse=True))
print()

#Show that your list is still in its original order by printing it again.
print (my_favorite_country)
print()
#Use reverse() to change the order of your list. Print the list to show that its order has changed.
my_favorite_country.reverse()
print (my_favorite_country)
print()
#Use reverse() to change the order of your list again. Print the list to show it’s back to its original order.

my_favorite_country.reverse()
print (my_favorite_country)
print()
#Use sort() to change your list so it’s stored in alphabetical order. Print the list to show that its order has been changed.

my_favorite_country.sort ()
print (my_favorite_country)
print()

#Use sort() to change your list so it’s stored in reverse alphabetical order. Print the list to show that its order has changed.

my_favorite_country.sort (reverse=True)
print (my_favorite_country)