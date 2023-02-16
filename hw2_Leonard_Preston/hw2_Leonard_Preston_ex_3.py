##Homework 2, Exercise 3  
##Name Leonard Preston
##Date 2/16/2023
##Basic list manipulation.



#strList()
#Parameters: a list
#Return: void
#Prints a string with all items separated by a comma and a space, with 'and'
#inserted before the last item
def strList(myList):

    #Everything but the last 2 elements of the list
    myNewList = ", ".join(myList[0:-2])

    #Last 2 elements of the list
    myOtherList = ", and ".join(myList[-2:])

    #Joining the 2 lists
    print(myNewList + ", " + myOtherList)

#Main
def main():

    # Creating list of names (1)
    names = ["Wallet", "Phone", "Keys"]

    # Print list using a single line of code (1)
    print("List: ",names)

    # (2) Sort the list using sort() function
    names.sort()

    # (2) Print sorted list
    print("Sorted: ", names)

    # (3) Print the first item in the list
    print("First item: ", names[0])

    # (4) Print everything but the first item using slice
    sliced = slice(1, 3)
    print("Sliced: ", names[sliced])

    # (5) Print the last item in the list using negative index
    print("Negative index: ", names[-1])

    # (6) Print index of keys using index()
    value = names.index("Keys")
    print("Index() of keys: ", value)

    # (7) Append "Tablet" to the list
    names.append("Tablet")

    # (7) Print append list
    print("Append tablet: ", names)

    # (8) Insert mask to the lsit as the second item in the list
    names.insert(1, "Mask")

    # (8) Print appended list
    print("Append mask: ", names)

    # (9) Remove Phone from the list
    names.remove("Phone")

    # (9) Print removed list
    print("Remove Phone: ", names)

    # (10) Reverse list then print list
    names.reverse()
    print("Reverse List: ", names)

    # (11) get strList
    strList(names)

main()






