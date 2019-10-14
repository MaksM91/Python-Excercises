#This is guess a number game

import random

print("Hello! What is your name?")
name = input()

randomNum = random.randint(1,20)
print('Well ' + name + ' , I am thinking of a number between 1 and 20, take a guess')

#allow player to guess six times

for pickedNum in range(1,7):
    print('Take a guess')
    guess = int(input())
    if guess > randomNum:
        print('Too high')
    elif guess < randomNum:
        print('Too low')
    else:
        break
    
if guess == randomNum:
    print('Correct!')
    print('You guessed my number in ' + str(pickedNum) + 'turns')
else:
    print('Well nope, I was thinking about ' + str(randomNum))
    

    
