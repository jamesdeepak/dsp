# The football.csv file contains the results from the English Premier League. 
# The columns labeled ‘Goals’ and ‘Goals Allowed’ contain the total number of 
# goals scored for and against each team in that season (so Arsenal scored 79 goals 
# against opponents, and had 36 goals scored against them). Write a program to read the file, 
# then print the name of the team with the smallest difference in ‘for’ and ‘against’ goals.
import csv

with open('football.csv', newline='') as csvfile:
    myreader = csv.reader(csvfile, delimiter=',', quotechar='|')
    next(myreader,None) #ignoring the header
    
    mainTuple = []
    for row in myreader:
        team = row[0]
        gs = int(row[5])
        ga = int(row[6])
        diff = gs-ga
        #print(diff)
        tup = (team,diff)
        
        mainTuple.append(tup)
        
def getKey(item):
    return item[-1] #index number for the tuple -1 means last


mainTuple.sort(key=getKey)
reqList = mainTuple[0] #Getting the first value of multielement tuple
#getting the first element of the tuple

print(reqList[0] +' had the smallest difference in for and against ' \
      'goals. Their difference was ' + str(reqList[1])) 



    

