import csv

myreader = csv.reader(open('faculty.csv'))
next(myreader,None) #ignoring the header

faculty_dict1 = {}
faculty_dict2 = {}
for row in myreader:
    fullNameList = row[0].split(" ")

    lastName = fullNameList[-1]
    firstName = fullNameList[0]
    if len(fullNameList) > 2:
        middleName = fullNameList[1]
    else:
        middleName = ""

    #get different titles
    fullTitle = row[2].strip()
    titleCharIndex = fullTitle.index("Professor", 0)
    title = fullTitle[:titleCharIndex+9]
    degree = row[1].strip()
    email = row[3].strip()

    value = [degree, title, email]
    
    key1 = lastName   
    if key1 in faculty_dict1:
        # duplicate row handling
        faculty_dict1[key1].append(value)
    else:
        faculty_dict1[key1] = [value]

    key2 = (firstName, lastName)
    if key2 in faculty_dict2:
        # duplicate row handling
        faculty_dict2[key2].append(value)
    else:
        faculty_dict2[key2] = [value]


print("This is Dictionary 1 with just Last Name as the key")
print("")
print(faculty_dict1)

print("")
print("This is Dictionary 2 with both First Name and Last Name as key")
print("")
print(faculty_dict2)

print("")
print("This is sorted Dictionary 2 (sorted by Last Name) with both First Name and Last Name as key")
print("")
sortedByKeyDict = sorted(faculty_dict2.keys(), key = lambda x:x[-1])
for faculty_keys in sortedByKeyDict:
    print(faculty_keys,faculty_dict2[faculty_keys])


