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
"Obstructing", "Protective Order", "Traffic Arrest", "Uniform Notice of Violation", "Disturbance", "Medical Assist", "Resisting Arrest",
"Uniform Notice of Violation", "Assist Other Agency", "Protective Order"]


#Category 1 list - Crimes against the public 
cat1  = ["Criminal Mischief", "Curfew Violation", "DUI", "Disorderly Conduct", "Disturbance", "Fire Alarm",
"Liquor Law, Public", "Intoxication", "Liquor Law, Underage", "Minor in Possession - Alcohol",
"Narcotics Violation", "Narcotics Violation, Distribution/Sale", "Narcotics", "Violation, Marijuana",
"Odor Of Marijuana","Poss of Controlled Substance", "Poss of Marijuana", "Public Indecency", 
"Public Intoxication", "Suspicious Person", "Suspicious Vehicle"]

#Category 2 list - Crimes against property 
cat2 = ["Auto Theft","Burglary, Residence", "Destruction of Property", "Larceny", "Larceny From Auto", 
"Larceny, Electronics", "Motor Vehicle Crash, Property Damage", "Trespassing", "Larceny, Bicycle"]

#Category 4 list - crimes against the person
cat4 = ["Robbery", "Assault", "Dating Violence", "Harassment", "Animal Bite", "Intimidation/Threats",
"Reckless Endangerment", "Sexual Assault", "Reckless Endangerment"]

#Category8 list - Severe crimes against the person
cat8 = ["Assault, Aggravated", "Abduction", "Motor Vehicle Crash, Hit and Run"]

crime_cat_list = [cat0, cat1, cat2,cat4, cat8]

data = {
        '_id':  '',     #The ODU CSV ID - Figured might as well use the this as an ID
        'crimeCat':' ', #Category of the most sever offense 
                        #The crime categories are
                        #{
                            #0- uncategorized, 
                            #1- public ofenses, 
                            #2- crimes against property
                            #4- Crimes against the person
                            #8- Severe Crimes
                        #}
        'desc':' ',     #Description of the crimes, e.g. 3 offense, at {clean_address}, most sever being {most_severe_crime}
        'date':' ',     #Date of the offense(s)
        'time':' ',     #Time of the offense(s)
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

            #Manipulate the CSV row
            #---------------------
            
            print(row[0])
            record_id = row[0]
            print(row[1]) 
            
            #Crimes can have multiple offenses to evaluate
            #Breaks the offenses in the crime report by the "|" character
            offenses_to_parse = row[1]
            check_offense = ''
            pos = offenses_to_parse.find('|')
            
            #List of tuples
            #Will be used to store the crime with its category, this will be a sorted listed.
            tuple_list = []
            max_category = 0
            #This is used to speed up the sort up of the list.
            last_sort_cat = 0
            last_sort_location = 0
            while pos != -1:
                check_offense = offenses_to_parse[:pos-1]
                offenses_to_parse = offenses_to_parse[pos+2:]
                first_time = False
                x = 0
                while (x<5):
                    if check_offense in crime_cat_list[x]:
                        #Will store the crime category and the crime category in a list together
                        #in a tuple then store that tuple in a list
                        offense_tuple = (x, check_offense)
                        if x >= max_category:
                            tuple_list = [offense_tuple] + tuple_list
                            max_category = x
                            last_sort_cat = x
                            last_sort_location = 0
                        elif x == last_sort_cat:
                            tuple_list.insert(last_sort_location, offense_tuple)
                        else:
                            y = 1
                            # z returns the crime category of the second element in the tuple list
                            z = tuple_list[y][0] 
                            while (x < z) and (y < len(tuple_list)) :
                                y=+1
                                if y == len(tuple_list):
                                    tuple_list.append(offense_tuple)
                                    last_sort_cat = offense_tuple[0]
                                    last_sort_location = y
                                    break
                            last_sort_cat = offense_tuple[0]
                            last_sort_location = y
                            tuple_list.insert(y, offense_tuple)
                            break
                    else:
                        x=+1
                    pos = offenses_to_parse.find('|') 
                    crime_cat = max_category
            #-- Done with looping ------------------------------------------------------------------------------------------------        
            occurrence_time_date_to_parse = row[3]
            occurrence_time_date_to_parse = occurrence_time_date_to_parse.split()
            time = occurrence_time_date_to_parse[1] 
            date = occurrence_time_date_to_parse[0]
           
            tuple_count = 0
            #Create a list of offense from the sorted to tuple_list             
            while (tuple_count < len(tuple_list)):
                offenses_lis.append(tuple_list[tuple_count][1])
                tuple_count=+1 
                

            clean_address = row[5] 
            lat = row[6]
            lng = row[7]
                
            data['_id'] = record_id
            data['crimeCat'] = crime_cat
            data['date'] = date
            data['time'] = time
            data['offenses'] = offenses_list
            data['lat'] = lat
            data['lng'] = lng


            json.dump(data, outfile)
            line_count=+1
        else:
            line_count+=1
infile.close
