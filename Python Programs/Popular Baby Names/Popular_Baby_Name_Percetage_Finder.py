# Tannavee Kumar

# This program reads in file  countsByName.csv and populates a dictionary
# that can be used to look up a list of counts by year using the person's name. Counts are stored as integers..
# Loop will ask the user to enter a name until it finds it in the dictionary.
# It will make a dot plot of the number of times the baby name was used in a
# given year, and also return the highest percentage of the instances the
# name was used in a given year. 

# importing plainchart.py
import plainchart

# opening file countsByName.csv
inFile = open("countsByName.csv", "r")

# opening file totalsByYear.csv
newInFile = open("totalsByYear.csv", "r")

# creating an empty dictionary that will be populated with the counts over the years a name was used
# nameDict = name dictionary
nameDict = {}

# empty list for the total number of names over the years
yearList = []

#skipping line 1 for countsByName
lineNames = inFile.readline()

#skipping line 1 for totalsByYear
lineYear = newInFile.readline()

while True:
    # user prompt asking the user for a name
    inputName = input("What's your name?")
    # making all values lowercase
    lowerCase = inputName.lower()
    # capitalizing the first letter
    inpName = lowerCase.capitalize()

    while True:

        while True:
            # for totalsByYear

            # reading each of the lines in a loop
            lineYear = newInFile.readline()
            #if statement for when there is an empty line, it will stop reading
            if lineYear == "":
                break
            # stripping off the newline
            lineYear = lineYear.strip()
            # splitting the line into a list
            lineYearList = lineYear.split(',')
            # extracting the second element from lineYearList
            yearList.append(int(lineYearList[1].strip()))       
                        
        # for countsByName
        
        # reading each of the lines in a loop
        line = inFile.readline()
        #if statement for when there is an empty line, it will stop reading
        if line == "":
            break
        # stripping off the newline
        line = line.strip()
        # splitting the line into a list
        lineList = line.split(',')
        # removing the first element (names) in the list
        name = lineList.pop(0)
        # making strings in list into integers
        for i in range(len(lineList)):
            lineList[i] = int(lineList[i])

        
        # making a list that is the percentage of a certain name in a given year
        normList = []
        for j in range(len(lineList)):
            normList.append((lineList[j] / yearList[j]) * 100)

        # key = names aka 1st element & values = names in a given year            
        nameDict[name] = normList

        
    # try- except to see if inputed name is found in the dictionary
    try:
        if inpName in nameDict:
            # if name is found it will print the corresponing key with Found
            print("Found", inpName)

            # extracting the maximum count in a list
            maxPopularity = max(nameDict[inpName]) 

            # printing the maximum count over the year
            print("Maximum Popularity =", "{0:.4f}".format(maxPopularity) + "%")

            # using plainchart to create a graph
            chart = plainchart.PlainChart(nameDict[inpName], height=25)
            print(chart.render())
            # creating a x-axis
            print("|1880     |1890     |1900     |1910     |1920     |1930     |1940     |1950     |1960     |1970     |1980     |1990     |2000     |2010     ")          
            
            # ending program once name is found       
            break
    except:
        # if name is not found in the dictionary, continue loop to prompt user to
        # continue inputing name
        continue




    




