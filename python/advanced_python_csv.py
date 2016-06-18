import csv

with open('faculty.csv', newline='') as csvfile:
    myreader = csv.reader(csvfile, delimiter=',', quotechar='|')
    next(myreader,None) #ignoring the header

    allEmailList = []

    for row in myreader:

        #get email addresses
        email = row[3].strip()
        if email != "":
            allEmailList.append(email)


csvfile = "emails.csv"
with open(csvfile, "w") as output:
    writer = csv.writer(output, lineterminator='\n')
    for val in allEmailList:
        writer.writerow([val])
