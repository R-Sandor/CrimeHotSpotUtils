import csv
#Raphael J. Sandor
#12/21/18
#CS411W
# This application will provide a list of unique crimes from the CSV

def OduCrimeData():

    outF = open('uniqueIncidentTypes.txt', 'w')
    inputFile = open('2017Crimemapping.csv', 'r')
    crimeList = []
    csv_reader = csv.reader(inputFile, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count == 1:
            print(row[1])
            print('------------------------------------')
            line_count += 1
        elif line_count >1:
            if row[1] not in crimeList:
                remainingIncidents=row[1]
                checkIncident = ''
                pos = remainingIncidents.find('|')
                firstTime = True 
                while pos != -1:
             #if '|' in row[1]: #we will switch this for a find command 
                    if firstTime == True:
                        checkIncident=(remainingIncidents[:pos-1])
                        remainingIncidents=remainingIncidents[pos+2:]
                        firstTime=False
                        if checkIncident not in crimeList:
                            crimeList.append(checkIncident)
                            print(checkIncident)
                    else:        
                        checkIncident=(remainingIncidents[:pos-1])
                        remainingIncidents=remainingIncidents[pos+2:]
                        firstTime=False
                        if checkIncident not in crimeList:
                            crimeList.append(checkIncident)
                            print(checkIncident)
                    pos = remainingIncidents.find('|')
                crimeList.sort()
            line_count += 1
        else:
            line_count +=1
    print(f'Processed {line_count} lines.')
    print (crimeList)
    for incident in crimeList: 
        outF.write(incident + '\n')


    #Clean up, close files
    outF.close
    inputFile.close

    return;
#TODO 
#Ask for which department the file is coming from
departmentList = ['ODU']
print('Where is this data comming from?:')
for idx, i in enumerate(departmentList):
    print('[',idx,']', i )
userInput = input()
try:
    userInput = int(userInput)
    
    while userInput < 0 or userInput >= len(departmentList):
    
        userInput = int(input('Enter a valid selection: '))
except ValueError:
    userInput = int(input('Enter a valid selection: '))
    while userInput < 0 or userInput >= len(departmentList):
    
        userInput = int(input('Enter a valid selection: '))

if userInput == 0:
    OduCrimeData()

#TODO 
#Provide the name of the file instead of hardcoding the file name
