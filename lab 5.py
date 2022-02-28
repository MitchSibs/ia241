'''
lab5 if statement
'''

#3.1

alien_color = 'green'

if alien_color == 'green':
    print('player 1 earned 5 points')


#3.2

alien_color = 'red'

if alien_color == 'green':
    print('player 1 earned 5 points')

else:
    print('player 2 earned 10 points')

#3.3

favorite_fruits = ['apple', 'banana', 'orange']

if 'orange' in favorite_fruits:
    print("Your really like orange's")

if 'strawberry' in favorite_fruits:
    print("Your really like strawberrie's")

if 'apple' in favorite_fruits:
    print("Your really like apple's")

#3.4

age = 21

if age < 10:
    print('You are a kid')

elif age < 20:
    print('You are a teenager')
else:
    print('You are an adult')
    if age > 65:
        print('You are an elder')


    


          
    
