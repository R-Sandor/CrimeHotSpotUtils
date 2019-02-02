import json
import csv

#----------------------------------------------------------------------------------------
#Raphael J. Sandor
#2/02/19
#CS411W
#Initial Revision: 1.0
#-----------------------------------------------------------------------------------------
#This application will take the 2017 ODU crime data and turn the data in to a .csv for the 
#Mongo Database. 
#
#The data is placed in to crimes.json and will contain the following attributes:
# ID, Crime Category, Date, Offenses(multiple offenses stacked in a crime), latitude, 
# longitude
#-----------------------------------------------------------------------------------------

#variables
#---------------
record_id=""
crime_cat=""
date=""
offenses_list=[]
lat=""
lng=""
#---------------
#Category 0 list - uncategorized
cat0 = ["Identity Theft", "Resisting Arrest","Credit Card Fraud", "Fraud", "False Report", "Evading", "Forgery",
"Obstructing", "Protective Order", "Traffic Arrest", "Uniform Notice of Violation"]

#Category 1 list - Crimes against the public 
cat1  = ["Criminal Mischief", "Curfew Violation", "DUI", "Disorderly Conduct", "Disturbance", "Fire Alarm",
"Liquor Law, Public", "Intoxication", "Liquor Law, Underage", "Minor in Possession - Alcohol",
"Narcotics Violation", "Narcotics Violation, Distribution/Sale", "Narcotics", "Violation, Marijuana",
"Odor Of Marijuana","Poss of Controlled Substance", "Poss of Marijuana", "Public Indecency", 
"Public Intoxication", "Suspicious Person", "Suspicious Vehicle"]

#Category 2 list - Crimes against property 
cat2 = ["Auto Theft","Burglary, Residence", "Destruction of Property", "Larceny", "Larceny From Auto", 
"Larceny, Electronics", "Motor Vehicle Crash, Property Damage", "Trespassing"]

#Category 4 list - crimes against the person
cat4 = ["Robbery", "Assault", "Dating Violence", "Harassment", "Animal Bite", "Intimidation/Threats",
"Reckless Endangerment", "Sexual Assault"]

#Category8 list - Severe crimes against the person
cat8 = ["Assault, Aggravated", "Abduction", "Motor Vehicle Crash, Hit and Run"]

crime_cat_list = [cat0, cat1, cat2,cat4, cat8]

data = {
        '_id':  '',     #The ODU CSV ID - Figured might as well use the this as an ID
        'crimeCat':' ', #The crime categories {
                            #0- uncategorized, 
                            #1- public ofenses, 
                            #2- crimes against property
                            #4- Crimes against the person
                            #8- Severe Crimes
                        #}
        'desc':' ',     #Description of the crimes, e.g. 3 offense, at {clean_address}, most sever being {most_severe_crime}
        'date':' ',     #Date of the offense(s)
        'offenses': [], #List of offenses
        'lat':' ',      #Latitude      
        'lng':' '}      #Longitude

#Open our data CSV
infile = open('2017Crimemapping.csv', 'r')
csv_reader = csv.reader(infile, delimiter=',')
#------------------------------------------------
#This is where the data json objects are created
#from the csv file
#------------------------------------------------
with open('crimes.json', 'w') as outfile:
    
    data['_id'] = record_id
    line_count = 0
    for row in csv_reader:
        if line_count >2:
            data['_id'] = record_id
            data['crimeCat'] = crime_cat
            data['date'] = date
            data['offenses'] = offenses_list
            data['lat'] = lat
            data['lng'] = lng
            # Let me see the data printed to screen while dumping to .json file. 
            print(data);
            json.dump(data, outfile)
        else:
            line_count+=1
infile.close
