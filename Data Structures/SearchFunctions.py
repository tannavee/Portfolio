# Tannavee Kumar

# Problem 1: create a new function called ternarySearch. Should do what
# binary search does but now in three segments

def ternarySearch(alist, item):
    first = 0 # first = first index
    last = len(alist) - 1 # last = last index
    found = False
    while first <= last and not found:
        midpoint1 = first + (last - first)//3 # length of 1/3 of list and add to 0
        midpoint2 = last - (last - first)//3 # length of 1/3 of list and sbtrct from last
        if (alist[midpoint1] == item) or (alist[midpoint2] == item): 
            found = True # item is in list if either midpoints = items
        else:
            if item < alist[midpoint1]: # if item is less than the item at mdpt1
                last = midpoint1 - 1 # change the last value to the item bfr mdpt1
            elif item > alist[midpoint2]: # if item is greater than the item at mdpt2
                first = midpoint2 + 1 # change the 1st value to the item after mdpt2
            else: # if mdpt1 < item < mdpt2
                first = midpoint1 + 1 # first item becomes item after mdpt1
                last = midpoint2 - 1 # last value becomes item after mdpt2
    return found

# sample test case
a = [1, 5, 7, 9]
ternarySearch(a, 5)

# Problem 2: creat a new function called ternarySearchRec, which should be the
# recursive version of the above code.

def ternarySearchRec(alist, item): # defining the recursive function 
    if alist == []: # base case, if list is empty
        return False # user will see false
    else:
        midpoint1 = len(alist)//3 # mdpt1 at index at 1/3 mark
        midpoint2 = (len(alist) * 2)//3 # mdpt2 at index at 2/3 mark
        if (alist[midpoint1] == item) or (alist[midpoint2] == item):
            return True # true if item = mdpt 1 or mdpt2
        elif item < alist[midpoint1]: # if item < mdpt 1
            # base case is the slicing part, recrusily calls from 0, to the value before mdpt1
            return ternarySearchRec(alist[:midpoint1], item) 
        elif item > alist[midpoint2]: # if item > mdpt 2
            # base case is the slicing part, recrusily calls from value after mdpt2
            # to last value
            return ternarySearchRec(alist[midpoint2 + 1:], item)
        else: # if item is in between the mdpts
            # base case is the slicing part, recrusily calls from value after mdpt1
            # to value before mdpt2
            return ternarySearchRec(alist[midpoint1 + 1:midpoint2], item)

# Problem 3: modify the put function from the book, so that the hastable is able
# be extended 

class HashTable:

    # initializing
    def __init__(self, size = 11): 
        # default size is 11, but any size can be initialized
        self.size = size 
        # slot list is NONE * size of list, and same for data list
        self.slots = [None] * self.size 
        self.data = [None] * self.size

    def put(self,key,data): # put function 
        hashvalue = self.hashfunction(key,len(self.slots)) # calls the hashfunction 
        if self.slots[hashvalue] == None: # if slot empty
            self.slots[hashvalue] = key # that slot holds key
            self.data[hashvalue] = data # at same index, input data in the data list
        else: # if the key already exists
            if self.slots[hashvalue] == key: 
                self.data[hashvalue] = data  #replace
            else: # if not he same key, and not empty
                nextslot = self.rehash(hashvalue,len(self.slots)) # do linear probing
                # 3 conditions for the while loop to cont probing:
                # slot can't be empty
                # slot can't have the same key
                # nextslot cant = hashvalue, if it does then that means we've done 1 cycle
                while self.slots[nextslot] != None and self.slots[nextslot] != key and nextslot != hashvalue:
                    nextslot = self.rehash(nextslot,len(self.slots)) # cont probing
                
                if self.slots[nextslot] == None: # if slot is empty
                    self.slots[nextslot]=key # enter key
                    self.data[nextslot]=data # enter data in corresponding index
                
                elif self.data[nextslot] == key: # if slot has same key
                    self.data[nextslot] == data # update 
                
                else:
                    if nextslot == hashvalue: # if nextslot = inital hasvalue
                        self.newSize = (self.size * 2) + 1 # increase size
                        print("Resizing the table") # let's the user know about resizing
                        # divide newsize by 3 to newsiz - 1 to check if prime
                        for i in range(3, self.newSize):
                            if self.newSize % i == 0: # if remainder = 0
                                self.newSize = self.newSize + 2 # add 2
                        print("New Size: ", self.newSize) # print the final newsize
                        self.oldSlots = self.slots # old slots = the orignal slot array
                        self.oldData = self.data # old data = original data array
                        self.slots = [None] * self.newSize # currant slot array is addjusted 
                        self.data = [None] * self.newSize # currant data array is adjusted
                        self.oldSize = self.size # old size = original size
                        self.size = self.newSize # curratn size is updated
                        for i in range(len(self.oldSlots)): # for the indices in old slot array
                            self.put(self.oldSlots[i], self.oldData[i]) # put key, data in new arrays
                        self.put(key, data) # run this for any remained pairs not in the table yet
                            
    def hashfunction(self,key,size): # this function provides hasvalue
        return key%size 
    
    def rehash(self,oldhash,size): # used for linear probing 
        return (oldhash+1)%size

    def get(self,key): # user can input key, and get value 
        startslot = self.hashfunction(key,len(self.slots)) # gets hashvalue
        data = None 
        stop = False
        found = False
        position = startslot # counter starts at hashvalue(starting slot)
        # 3 conditions for while loop for it to stop
        # slot at postion should be empty, and
        # nothing found, and
        # not stopped
        while self.slots[position] != None and not found and not stop: 
            if self.slots[position] == key: # if slot has key
                found = True 
                data = self.data[position] # value returned is in corresponsing data array
            else: # otherwise do linear probing to find key
                position = self.rehash(position,len(self.slots))
                if position == startslot: # if position returns back to starting slot 
                    stop = True # loop stops 
        return data

    def __getitem__(self,key): # using brackets to easily get
        return self.get(key)

    def __setitem__(self,key,data): # using brackets to easilty put
        self.put(key,data)

        
        
