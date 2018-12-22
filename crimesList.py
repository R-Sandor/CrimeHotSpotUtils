import csv
#Raphael J. Sandor
#12/21/18
#CS411W
# This application will provide a list of unique crimes from the CSV

#TODO 
#Ask for which department the file is coming from
print('Where is this data comming from?:')
print('[1]ODU')
dataSrc = input()


#TODO 
#Provide the name of the file instead of hardcoding the file name

outF = open('uniqueIncidentTypes.txt', 'w')
inputFile = open('crimedata2017ODU.csv', 'r')
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

