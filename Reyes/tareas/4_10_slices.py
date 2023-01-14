# Using one of the programs you wrote in this chapter, add several lines to the end of the program that do the following:
# • Print the message, The first three items in the list are:. Then use a slice to print the first three items from that program’s list.
# • Print the message, Three items from the middle of the list are:. Use a slice to print three items from the middle of the list.
# Print the message, The last three items in the list are:. Use a slice to print the last three items in the list.


my_guest_list = ['michael angelo','luke jaeger','buckethead','chris storey','rusty cooley']

first = my_guest_list [:3]
middle = my_guest_list [1:4]
last = my_guest_list [2:]
print (f'the first three items in the list are: {first}')
print (f'three items from the middle of the list are: {middle}') 
print (f'the last three items in the list are: {last}')