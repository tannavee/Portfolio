# Tannavee Kumar


# Problem 1: creating kleinfeldt function with recursion

def kleinfeldt(n): # defining function 
    if n == 1: # if n = 1
        return 1 
    else: # else statement if > 1
        return 1/(n * n) + kleinfeldt(n - 1) # using recursion



# Problem 2
def ladder(n): # defining function
    if n == 1: # if the ladder has only 1 rung, then there is only 1 way to go up
        return 1 
    elif n == 2: # if the ladder has 2 rungs, there are 2 ways to go up 1 + 1, 2 + 0
        return 2 
    else: # if the ladder has > 2 rungs, then use the fibonacci seq
        return ladder(n - 1) + ladder(n - 2) # using recursion 
        


# Problem 3: Function that finds the largest integer in a given list

def findLargest(listOfInterest): # defining function 
    if len(listOfInterest) == 1: # if the inputed list is only 1 elmt long 
        return listOfInterest[0] # returns 1st elmt
    else: # if > 1 elmt 
        # the reduction step is shortening the first list and making a new list i,
        # the recursive step is using findLargest simultaneously
        i = findLargest(listOfInterest[1:]) 
        if i > listOfInterest[0]: # if given elmt is > 1st elmt
            return i # return that given elmt
        else: # if not greater
            return listOfInterest[0] # return the first element


# Problem 4: Finding the majority element in a given list

def findPossibilities(listOfInterest): # defining function, input list "a"
    listOfPossibilities = [] # list "b"
    if len(listOfInterest) == 0: # checks if inpted list is empty
        return listOfPossibilities # returns empty list
    else:
        listLen = 0 # defining new variable 
        if len(listOfInterest) % 2 != 0: # if list is odd
            listLen = len(listOfInterest) - 1 # length of list goes to 2nd to last elmt
            listOfPossibilities.append(listOfInterest[-1]) # adds the last elmt to "b"
        else: # if list is even
            listLen = len(listOfInterest) # length of list goes to the end
        i = 0 
        for i in range(0, listLen, 2): # starts at beginning, goes to the end defined above, and travels 2 elmts at a time
            if listOfInterest[i] == listOfInterest[i + 1]: # is elmt = the next one
                listOfPossibilities.append(listOfInterest[i]) # add to b
        
    if len(listOfPossibilities) > 2:  # if b > 2
        return findPossibilities(listOfPossibilities) # do recursion 
    elif (len(listOfPossibilities) == 2) and (listOfPossibilities[0] == listOfPossibilities[1]): # b has two elements and they're equal to each other
        listOfPossibilities.pop() # pop off one
        return listOfPossibilities
    else:
        return listOfPossibilities # otherwise just return b

def verifyPossibilities(listOfInterest, listOfPossibilities): # defining function 
    if len(listOfPossibilities) == 0: # if b is empty 
        print("There is no majority element since the list of interest is empty.") # lets user know that a is empty
        return None # returns none
    elif len(listOfPossibilities) == 1: # is b has 1 elmt
        i = 0 # counter for list
        counter = 0 # counter for verifying maj
        for i in range(0, len(listOfInterest), 1):
            if listOfInterest[i] == listOfPossibilities[0]: # if elmt in b matches elements in a
                counter = counter + 1 # counter increases
        if counter > (len(listOfInterest)) / 2: # if counter > n/2
            print("The majority element is", listOfPossibilities[0]) # print the element in b
        else: 
            print("There is no majority element in: ", listOfInterest) # if not, return none
            return None
    else: # if two elmts in b
        i = 0 # counter to iterate thru a, for 1st elmt in b
        counter1 = 0 # counter to check for maj, 1st elmt
        j = 0 # counter to iterate thru a, for 2nd elmt in b
        counter2 = 0 # counter to check for maj, 2nd elmt
        for i in range(0, len(listOfInterest), 1): # loop to check if 1st elmt in b is maj
            if listOfInterest[i] == listOfPossibilities[0]:
                counter1 = counter1 + 1
        for j in range(0, len(listOfInterest), 1): # loop to check if 2nd elmt in b is maj
            if listOfInterest[j] == listOfPossibilities[1]:
                counter2 = counter2 + 1
        if counter1 > (len(listOfInterest)) / 2: # if 1st in b is maj
            print("The majority element is", listOfPossibilities[0]) # let user know 
        elif counter2 > (len(listOfInterest)) / 2: # if 2nd in b is maj
            print("The majority element is", listOfPossibilities[1]) # let user know
        else: # if now maj
            print("There is no majority element in: ", listOfInterest) # let user know 
            return None # return none

# Sample Test Data for Problem 4  
# odD = [1,2,3,3,4,2,1,4,2,1,5,5,5]
# eveN = [1,2,3,3,5,5]
# nMajority = [1,2,3]
# empty = []
# aOdd = [4,4,3,3,4,2,1,4,2,1,4,5,6,4,12,1,2,31,4,4,4,4,4,3,1,2,3,4,4]
# liste = [1,2,2,3,4,4]
# listo = [1,2,1]
# maj = [4,4,4,4,4,4]


# Using the following Node class code for Problem 5 and 6
class Node:
    def __init__(self,initdata):
        self.data = initdata
        self.next = None

    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def setData(self,newdata):
        self.data = newdata

    def setNext(self,newnext):
        self.next = newnext


# Problem 5: finding a specific item in a linked list via recursion 

def findValue(item, nodeOfInterest): # defining function
    # if data associated w/ inputed node is not = to item, and there is no node after inputed
    # node
    if (nodeOfInterest.getData() != item) and (nodeOfInterest.getNext() == None):
        return False # it will return false
    # otherwise if data associated w/ inputed node does = item
    elif nodeOfInterest.getData() == item: 
        return True # function returns true
    # if data associated w/ inputed node doesn't equal item, and there are nodes after it
    else: 
        nodeOfInterest = nodeOfInterest.getNext() # new node = node next to inputed node
        # it will recursively keep going, if it goes through the entire list, and still hasn't
        # found match, function will return to the first if statement
        return findValue(item, nodeOfInterest) 
                                               
                                               

# Problem 6: finding last value in a linked list

    # For this problem, I modified the above code so that the function will just go to the
    # last node and get the data
def findLastValue(nodeOfInterest): # defining the function 
    if nodeOfInterest.getNext() == None: # if no node next to the node we put in the parameter
        return nodeOfInterest.getData() # returns data associated with the nodeOfInterest
    else: # otherwise 
        nodeOfInterest = nodeOfInterest.getNext() # new nodeOfInterest becomes the next one
        # will recursive do this until there is None and then it will return the data
        # associated with last one
        return findLastValue(nodeOfInterest) 

