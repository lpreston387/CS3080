

#Function collatz
#Parameters: user inputed number
#Return: Recurses until base case 1 is reached
def collatz(number):

    print(number)

 
    if number == 1:
        return 1
    
    elif number % 2 == 0:
        collatz(float(number // 2))
        
    else: 
        collatz(float(3*number + 1))
        
    



    

        
## Main
def main():
    
    #Getting user input
    print("Enter number:")
    userNum = input()

    #Try to call collatz. If the input is wrong throw except.
    #Excercise 1-2
    try:
        
        collatz(float(userNum))

    except:
        print("Must be a integer")
    
        
    

main()
    
    
    
