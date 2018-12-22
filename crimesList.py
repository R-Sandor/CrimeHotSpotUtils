import csv
#Raphael J. Sandor
#12/21/18
#CS411W
# This application will provide a list of unique crimes from the CSV

#TODO 
#Ask for which department the file is coming from


#TODO 
#Provide the name of the file instead of hardcoding the file name

outF = open('outputFile', 'w')
inputFile = open('crimedata2017ODU.csv', 'r')

csv_reader = csv.reader(inputFile, delimiter=',')
line_count = 0
for row in csv_reader:
    if line_count == 1:
        print(row[1])
        line_count += 1
    elif line_count >1:
        line_count += 1
        break 
    else:
        line_count +=1
print(f'Processed {line_count} lines.')


#Clean up, close files
outF.close
inputFile.close

