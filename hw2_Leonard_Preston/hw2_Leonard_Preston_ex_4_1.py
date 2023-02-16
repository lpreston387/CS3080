##’’’ 
##Homework 2, Exercise 1 (or 2, 3, ...) 
##Name Leonard Preston
##Date 2/16/2023
##Guessing Game. 
##’’’

# import random 
import random

#Variables

answer = random.randint(0,21)

count = 0;

print("Guess the number I am thinking of between 0-20")
userInput = int(input())
while count < 10:
    print("You have: ", (10-count), "attempts left")
    if userInput == answer:
        print("Good job you guessed my number", userInput)
        count = count + 20

    elif userInput > answer:
        print("Your guess is to high: ", userInput)
        count = count + 1
        print("Take a guess:")
        userInput = int(input())

    elif userInput < answer:
        print("Your guess is to low: ", userInput)
        count = count + 1
        print("Take a guess:")
        userInput = int(input())
        
              
    
