# Tannavee Kumar
# ECS 32A
# Assignment 6 Part 5
#
# printing out wordle of the most used words
from wordle import wordleFromObject
from cleanWord import clean

# the Count class.  The wordleFromObject function takes a Count object as
# input, and calls its getTopWords method. 
class Count:
        # dictionary of word counts
        wordCounts = None

        # method to initialize any data structures, such as a dictionary to
        # hold the counts for each word, and a list of stop words
        def __init__(self):
                print("Initializing Word Counter")
                # set the attrbute wordCounts to an empty dictionary
                self.wordCounts = {}

                # reading in file for frequent words
                inFileFreq = open("stopWords.txt","r")

                # empty list of frequent list of words from stopWords.txt to stop
                # adding to dictionary
                self.stopList = []

                # loop to read lines of stopWords.txt and add to stopList
                while True:
                    # reading each of the lines in a loop
                    lineFreq = inFileFreq.readline()

                    # if statement for when there is an empty line, it will stop reading
                    if lineFreq == "":
                        break

                    # stripping of the newline
                    lineFreq = lineFreq.strip()

                    # splitting the line 
                    lineFreqSplit = lineFreq.split()

                    # adding all the lines from stopWords.txt to stopList    
                    for i in range(len(lineFreqSplit)):
                        self.stopList.append(lineFreqSplit[i].strip())

        # method to add one to the count for a word in the dictionary.
        # if the word is not yet in the dictionary, we'll need to add a
        # record for the word, with a count of one. 
        def incCount(self,word):
                # Add code to clean the word
                word = clean(word)
                # Do not add the empty string to the dictionary
                if word == "":
                        return self.wordCounts  
                # checking to see if word is in stopList
                elif word in self.stopList:
                    return
                # add word to dictionary
                else:
                    self.wordCounts[word] = self.wordCounts.get(word, 0) + 1
                return self.wordCounts

        # method to look up the count for a word
        def lookUpCount(self,word):
                if word not in self.wordCounts:
                        return 0
                else:
                        return self.wordCounts[word]

        # method to get the most frequent words out of the dictionary.
        # The argument "num" indicates how many words to return. 
        def getTopWords(self,num):
                # creating an empty list for top used words
                topList = []
                # for loop to add list of tuples to topList
                for word in self.wordCounts:

                    # tuple will have number and then word
                    tupleList = (self.wordCounts[word], word)
                    # adding tuples to topList
                    topList.append(tupleList)
                # sorting the tuples in the list
                topList.sort(reverse = True)
                return topList[:num]             

                
                
# The main program 
def main():
                                
        # Make a new counter object 
        # the counter holds the counts for all the words
        counter = Count()

        
        # open the file
        inFile = open("Alice.txt","r")          

        # put a loop here that extracts all words and
        # inserts each word into the counter object by calling
        # the counter.incCount() method

        # reading words in Alice.text
        for line in inFile:

            # stripping of the newline
            line = line.strip()

            # splitting the line into a list
            lineList = line.split()

            # adding all the lines from Alice.txt to wordList    
            for i in range(len(lineList)):
                counter.incCount(lineList[i])
        
        inFile.close()

        # Test code for Part 2 and 3. Comment for other parts
        # print(counter.lookUpCount("alice"))
        # print(counter.lookUpCount("rabbit"))
        # print(counter.lookUpCount("and"))
        # print(counter.lookUpCount("she")) 

        # test code for getTopLines.  Uncomment in Part 4.
        topTen = counter.getTopWords(10)
        print(topTen)

        # call to the wordle function 
        wordleFromObject(counter,30)


# run the main program
main()
        
