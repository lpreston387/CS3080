#’’’ 
#Homework 1 
#Name: Leonard Preston
#Date: 2/2/2023
#Description of your program:
#   This program performs basic python functions including math and logical operations, for loops, if, elif, else statements, taking userinput, len and str conversions
#   additionally it goes over random() function. These are displayed over a very basic account login and security program.
#   The first portion of the program focuses on logging in with a username and password. The second while loop logs you in.
#   The third while loop lets you change your account name, password, and exit the program.
#’’’
import random

info = str('Leonard Preston Homework 1 CS3080') #str requirement simply turns something into a string representation
print(info)

humanAuthentication = True #Do while Sentinal. Boolean requirement

#Human Authentication
while humanAuthentication:
    x = random.randint(0,100) #Assigning x to rand int
    
    print("Please enter numbers shown to prove you are not a robot")
    print(x)
    robotCheck = input() # user enters rand int number
    
    robotCheck=int(robotCheck) #Casting robotCheck to an int rather then a string. int requirement
    
    if (robotCheck == x): # Checks if user entered correct number
        humanAuthentication = False
        


#simple log in program.
username = "Preston" #string requirement
pin = 123.2 #float requirement

#simple validation do while loop
attempts = 0
while True:
    print("Please enter username. (Preston)")
    usernameInput= input()
    print("Please enter password (123.2)")
    pinInput = input()
    attempts = attempts + 1 #addition + requirement
    if(attempts == 4):
        print("To many attempts shuttinw down")
        exit()
    elif(username != usernameInput): # validation
        continue
    elif(str(pin) != pinInput): #elif requirement and another str use conversion
        continue #continue requirement

    else: #else requirement. If both are entered correctly
        break #break requirement
    

birthyear = 1994 #int requirement
validation = True
while validation:
    print("Welcome")
    print("Press 1 to change username and password.  2 to log out")
    userInput = input()
    attempt = 3
    if(int(userInput)==2):
        print("Exting")
        exit()
    elif(int(userInput)==1):
       
        for n in range(0,2):

            if(n== 0 or n==1 or n==2):
                print("Please answer the following challenge question. You have 3 attempts. (birthyear = 1994)")
                print("What is your birthyear. Attempt:", n)
                birthYearInput = input()
                if(int(birthYearInput)!=birthyear):
                    print("Wrong input. Attempts left: ")
                    attempt = attempt-n # - operator requirement
                    print(attempt)
                else:
                    validation = False
                    print("success")
                    break
                    
                    
validation = True
while validation: 
    print("Please enter a new username must be more then 0 characters and less then 10 characters")
    newName=input()
    length = len(newName)
                        
    if(length > 0 and length < 10):
        newName=username
        print("New username",username)
        validation = False
    else:
        print("new username must be more then 0 characters and less then 10 characters")
        
        
validation = True
min = 10
              
                    
while validation:
    print("Please enter a new password. Must be atleast 10 characters. Has to be an even ammount of characters")
    newPas = input()
    passLength= len(newPas)
    passLengthVerification = 1 * passLength #operater requirement *
    if(passLengthVerification < 10):
                            
        if((passLength % 2) == 0): #modulo operater requirement. making sure password is an even length
            print("Your new password is", newPas)
            pin = newPas
            validation = False
                            
                            
                       
                        
                        
                            
                                  
                            
                        








    
    







