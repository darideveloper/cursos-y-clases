# Turn your if-else chain from Exercise 5-4 into an if-elifelse chain.

# • If the alien is green, print a message that the player earned 5 points.
# • If the alien is yellow, print a message that the player earned 10 points.
# • If the alien is red, print a message that the player earned 15 points.
# • Write three versions of this program, making sure each message is printed for the appropriate color alien.

alien_color = 'yellow'

if alien_color == 'green':
    print ("Your a winner of five points")
    
elif alien_color == 'red':
    print ("Your a winner of fifteen  points")
     
else:
    print ('Your a winner of ten points')        
    
print ()

alien_1 = alien_color
alien_1 = 'green'

if alien_1 == 'red':
    print ("Your a winner of fifteen  points")
    
elif alien_1 == 'green':
    print ("Your a winner of five points")
    
else:
    print ('Your a winner of ten points')  
   
print ()

alien_2 = alien_1
alien_2 = 'red'

if alien_2 == 'red':
    print ("Your a winner of fifteen  points")
    
elif alien_2 == 'green':
    print ("Your a winner of five points")
else:
    print ('Your a winner of ten points')  

# Simplificación
alien = "red"

if alien == "green":
    print (5)
elif alien == "yellow":
    print (10)
else:
    print (15)