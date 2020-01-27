# Tannavee Kumar

# Problem 1: Creating a new sorting method called 'pancake sort'
def pancakeSort(plate): 
    if len(plate) <= 1:
        return plate
    else:
        for counter in range(0, len(plate) - 1):
            maxIndex = plate.index(max(plate[:len(plate) - counter]))
            plate[:maxIndex + 1] = plate[:maxIndex + 1][::-1]
            plate[:len(plate) - counter] = plate[:len(plate) - counter][::-1]
        return plate

# test list
#a = [1,9,5,4,62,7,10]
#pancakeSort(a)

# Problem 2: implement bubble sort using simultaneous sorting 
def bubbleSort(alist):
    for passnum in range(len(alist)-1,0,-1):
        for i in range(passnum):
            if alist[i] > alist[i+1]:
                alist[i], alist[i+1] = alist[i+1], alist[i]

# test list
ex = [54,26,93,17,77,31,44,55,20]
bubbleSort(ex)
print(ex)

# Problem 3: implement merge sort without using the slice operator

def mergeSort(alist):
    return mergeSortHelper(alist, 0, len(alist) - 1)

def mergeSortHelper(alist, start, end):
    print("Splitting ",alist)
    if len(alist)>1:
        mid = len(alist)//2

        lefthalf = []
        for i in range(0, mid):
            lefthalf.append(alist[i])

        righthalf = []
        for i in range(mid, len(alist)):   
            righthalf.append(alist[i])

        mergeSort(lefthalf)
        mergeSort(righthalf)

        i=0
        j=0
        k=0
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                alist[k]=lefthalf[i]
                i=i+1
            else:
                alist[k]=righthalf[j]
                j=j+1
            k=k+1

        while i < len(lefthalf):
            alist[k]=lefthalf[i]
            i=i+1
            k=k+1

        while j < len(righthalf):
            alist[k]=righthalf[j]
            j=j+1
            k=k+1
    print("Merging ",alist)

# test list
alist = [54,26,93,17,77,31,44,55,20]
mergeSort(alist)
#print(alist)

# Problem 4: Using the buildheap method, write a sorting function that can sort
# a list in O(nlogn) time

class BinHeap:
    def __init__(self):
        self.heapList = [0]
        self.currentSize = 0

    def percUp(self,i):
        while i // 2 > 0:
          if self.heapList[i] < self.heapList[i // 2]:
             tmp = self.heapList[i // 2]
             self.heapList[i // 2] = self.heapList[i]
             self.heapList[i] = tmp
          i = i // 2

    def insert(self,k):
      self.heapList.append(k)
      self.currentSize = self.currentSize + 1
      self.percUp(self.currentSize)

    def percDown(self,i):
      while (i * 2) <= self.currentSize:
          mc = self.minChild(i)
          if self.heapList[i] > self.heapList[mc]:
              tmp = self.heapList[i]
              self.heapList[i] = self.heapList[mc]
              self.heapList[mc] = tmp
          i = mc

    def minChild(self,i):
      if i * 2 + 1 > self.currentSize:
          return i * 2
      else:
          if self.heapList[i*2] < self.heapList[i*2+1]:
              return i * 2
          else:
              return i * 2 + 1

    def delMin(self):
      retval = self.heapList[1]
      self.heapList[1] = self.heapList[self.currentSize]
      self.currentSize = self.currentSize - 1
      self.heapList.pop()
      self.percDown(1)
      return retval

    def buildHeap(self,alist):
      i = len(alist) // 2
      self.currentSize = len(alist)
      self.heapList = [0] + alist[:]
      while (i > 0):
          self.percDown(i)
          i = i - 1

    def heapSort(self):
        # heaplist can't be empty and current size hase to be greater than 0
        while self.heapList != [0] and self.currentSize > 0:
            # simultaneously assignment so first elmt in heap becomes last vice/versa
            self.heapList[1], self.heapList[self.currentSize] = self.heapList[self.currentSize], self.heapList[1]
            # decreasing the size 
            self.currentSize = self.currentSize - 1
            # percolating down, so that heap property is resorted except for sorted portion
            self.percDown(1)
        # reversing the list so that, smallest number is in beginning
        self.heapList.reverse()
        # removing 0 from the last index which is rement of heap
        self.heapList.pop()
        print(self.heapList)

        
