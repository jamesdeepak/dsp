import csv
from collections import Counter


with open('faculty.csv', newline='') as csvfile:
    myreader = csv.reader(csvfile, delimiter=',', quotechar='|')
    next(myreader,None) #ignoring the header

     
    allDegList = []
    allTitleList = []
    allEmailList = []
    allDomainList = []
    for row in myreader:
        #get different degrees
        degList = (row[1].strip()).split(' ') #trimming string and splitting
        # by space as there are multiple degrees for a single person
        for degree in degList:
            # Since same degrees written with and without full stops, we want
            # to convert all to one to avoid double counting
            degree = degree.replace(".","")
            
            if degree !="0" and degree != "":
                allDegList.append(degree)
                

        #get different titles
        fullTitle = row[2].strip()

        titleCharIndex = fullTitle.index("Professor")

        title = fullTitle[:titleCharIndex+9]
        
        if title !="":
            allTitleList.append(title)

        #get email addresses
        email = row[3].strip()
        if email != "":
            allEmailList.append(email)
        charIndex = email.index("@")
        domainName = email[charIndex+1:]

        if domainName !="":
            allDomainList.append(domainName)
        
    allDegList.sort()
    allTitleList.sort()

    uniqueDegrees = set(allDegList)
    uniqueTitles = set(allTitleList)
    uniqueDomainNames = set(allDomainList)
    
    print("There are " + str(len(uniqueDegrees)) + " differnt degrees.")
    
    #Using Counter Module
    #print(Counter(allDegList))
    #Another way to do without using Counter module
    print(dict((x,allDegList.count(x)) for x in set(allDegList)))

    print("")
    print("There are " + str(len(uniqueTitles)) + " differnt Titles.")
    print(dict((x,allTitleList.count(x)) for x in set(allTitleList)))

    print("")
    print(allEmailList)

    print("")
    print("There are " + str(len(uniqueDomainNames)) + " differnt email domains.")
    print (uniqueDomainNames)
