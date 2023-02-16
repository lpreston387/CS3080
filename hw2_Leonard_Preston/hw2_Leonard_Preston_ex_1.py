

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


    collatz(float(userNum))

    
        
    

main()
    
    
    
