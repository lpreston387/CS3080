##’’’ 
##Homework 2, Exercise 4-2 
##Name Leonard Preston
##Date 2/16/2023
##Guessing Game. With random upper and lower bounds 
##’’’

# import random 
import random

#Variables
lowerBound = random.randint(0, 49)
upperBound = random.randint(51, 100)
answer = random.randint(lowerBound,upperBound)

count = 0;

print("Guess the number I am thinking of between ", lowerBound,
      " and ", upperBound)
userInput = int(input())
while count < 10:
    print("You have: ", (10-count), "attempts left")
    if userInput == answer:
        print("Good job you guessed my number", userInput)
        count = count + 20

    elif userInput > answer:
        count = count + 1
        print("You have: ", (10-count), "attempts left")
        print("Your guess is to high: ", userInput)
        print("Take a guess:")
        userInput = int(input())
        

    elif userInput < answer:
        count = count + 1
        print("You have: ", (10-count), "attempts left")
        print("Your guess is to low: ", userInput)
        print("Take a guess:")
        userInput = int(input())

        
              
    
