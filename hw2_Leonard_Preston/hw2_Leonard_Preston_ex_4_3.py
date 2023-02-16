##’’’ 
##Homework 2, Exercise 4-3 
##Name Leonard Preston
##Date 2/16/2023
##Guessing Game. With random upper and lower bounds and automated
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
userInput = random.randint(lowerBound,upperBound)
print("My first guess: ", userInput)
while count < 11:
    if userInput == answer:
        print("Good job you guessed my number", userInput)
        count = count + 20

    elif userInput > answer:
        count = count + 1
        if count > 10:
            print("Nice Try the answer is: ", answer)
        else:

            print("Your guess is to high: ", userInput)
            print("Take a guess. Attempt number: ", count)
            upperBound = userInput - 1
            userInput = random.randint(lowerBound,upperBound)
            print("My guess: ", userInput)
        
        

    elif userInput < answer:
        count = count + 1
        if count > 10:
            print("Nice Try the answer is: ", answer)
        else:

            print("Your guess is to low: ", userInput)
            print("Take a guess. Attempt number: ", count)
            lowerBound = userInput + 1
            userInput = random.randint(lowerBound,upperBound)
            print("My guess: ", userInput)


        
         
    
