import json
import csv

#----------------------------------------------------------------------------------------
#Raphael J. Sandor
#2/02/19
#CS411W
#Initial Revision: 1.0
#-----------------------------------------------------------------------------------------
#This application will take the 2017 ODU crime data and turn the data in .csv to json 
#for the Mongo Database. 
#
#The data is placed in to crimes.json and will contain the following attributes:
#   ID, Crime Category, Date, Offenses(multiple offenses stacked in a crime), latitude, 
#   longitude
#-----------------------------------------------------------------------------------------

#variables
#---------------
record_id=""
crime_cat=-1
date=""
offenses_list=[]
lat=""
lng=""
severity = 0
#---------------

#----------------------------------------------------------------------------------------
#Functions
#----------------------------------------------------------------------------------------
#The Crime category needs to switched from the index value of crime_cat_list
#to the actual crime category value

#These functions work as switch statement
def zero():
    return 0 
def one():
    return 1
def two():
    return 2
def three():
    return 4
def four():
    return 8
options = {0 : zero,
           1 : one,
           2 : two,
           3 : three,
           4 : four,
}
#-----------------------------------------------------------------------------------------

#-----------------------------------------------------------------------------------------
#Arrays of crime categories 
#-----------------------------------------------------------------------------------------

#Category 0 list - uncategorized
cat0 = ["Identity Theft", "Resisting Arrest","Credit Card Fraud", "Fraud", "False Report", "Evading", "Forgery",
"Obstructing", "Protective Order", "Traffic Arrest", "Uniform Notice of Violation", "Disturbance", "Medical Assist", "Resisting Arrest",
"Uniform Notice of Violation", "Assist Other Agency", "Protective Order", "Unauthorized Use of Motor Vehicle", "Lost Property",
"Served, Warrant", "Alarm"]


#Category 1 list - Crimes against the public 
cat1  = ["Criminal Mischief", "Curfew Violation", "DUI", "Disorderly Conduct", "Disturbance", "Fire Alarm",
"Liquor Law, Public", "Intoxication", "Liquor Law, Underage", "Minor in Possession - Alcohol",
"Narcotics Violation", "Narcotics Violation, Distribution/Sale", "Narcotics", "Violation, Marijuana","Narcotics Violation, Marijuana"
"Odor Of Marijuana","Poss of Controlled Substance", "Poss of Marijuana", "Public Indecency","Liquor Violation", 
"Public Intoxication", "Suspicious Person", "Suspicious Vehicle", "Student Conduct Violation"]

#Category 2 list - Crimes against property 
cat2 = ["Auto Theft","Burglary, Residence", "Burglary, Structure", "Destruction of Property", "Larceny", "Larceny From Auto", 
"Larceny, Electronics", "Motor Vehicle Crash, Property Damage", "Trespassing", "Tampering with Auto", "Larceny, Bicycle"]

#Category 4 list - crimes against the person
cat4 = ["Robbery", "Assault", "Dating Violence", "Harassment", "Animal Bite", "Intimidation/Threats", "Domestic Violence"
"Reckless Endangerment", "Sexual Assault", "Reckless Endangerment","Motor Vehicle Crash, Injury"]

#Category8 list - Severe crimes against the person
cat8 = ["Assault, Aggravated", "Abduction", "Motor Vehicle Crash, Hit and Run"]

#Array of crime categories
crime_cat_list = [cat0, cat1, cat2,cat4, cat8]
#--------------------------------------------------------------------------------------------

#JSON OBJECT 
data = {
        '_id':  '',     #The ODU CSV ID - Figured might as well use the this as an ID
        'crimeCat':' ', #Category of the most sever offense 
                        #The crime categories are
                        #{
                            #0- Uncategorized, 
                            #1- Public ofenses, 
                            #2- Crimes against property
                            #4- Crimes against the person
                            #8- Severe Crimes
                        #}
        'desc':' ',     #Description of the crimes, e.g. 3 offense, at {clean_address}, most sever being {most_severe_crime}
        'date':' ',     #Date of the offense(s)
        'time':' ',     #Time of the offense(s)
        'offenses': [], #List of offenses
        'severity':'',  #Static Sum of significance of the crime committed
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
    
    line_count = 0
    for row in csv_reader:
        if line_count >1:
            print("-------------------------------{Processing Row}-----------------------------------")

            #------------------------------------------------------------------------------------------
            #Manipulate the CSV row
            #-------------------------------------------------------------------------------------------

            offenses_list=[]
            record_id = row[0]
            #Crimes can have multiple offenses to evaluate
            #Breaks the offenses in the crime report by the "|" character
            offenses_to_parse = row[1]
            check_offense = ''

            #See if there are more offenses in offenses_to_parse variable
            pos = offenses_to_parse.find('|')

            #List of tuples
            #Will be used to store the crime with its category, this will be a sorted listed.
            tuple_list = []
            max_category = 0
            
            #This is used to speed up the sort up of the list.
            last_sort_cat = 0
            last_sort_location = 0
            
            #-------------------------------------
            # While there are still more offenses 
            # process them.
            #-------------------------------------
            while pos != -1:

                #Cut off the white space after a '|'
                #leaving only one offense
                check_offense = offenses_to_parse[:pos-1]

                #Cut off the bar and white space leaving the remaining offense(s) 
                #to be processed
                offenses_to_parse = offenses_to_parse[pos+2:]

                x = 0

                #There are only 4 crime categories therefore 
                #must be less than 5
                while (x<5):

                    #Check if crime is in that category
                    if check_offense in crime_cat_list[x]:
                        #Will store the crime category and the crime category in a list together
                        #in a tuple then store that tuple in a list
                        pos = offenses_to_parse.find('|') 
                        offense_tuple = (x, check_offense)

                        #if it is greater than the most severe crime so far, append to front
                        #save location and category of that incident to speed up future sorting
                        if x >= max_category:
                            tuple_list.insert(0, offense_tuple)
                            max_category = x
                            last_sort_cat = x
                            last_sort_location = 0
                            x+=1

                        #If its exactly the same category as the last
                        #insert where the last one was inserted to speed up sorting
                        elif x == last_sort_cat:

                            tuple_list.insert(last_sort_location, offense_tuple)
                            x+=1

                        #Manually find where it should be stored based on the contents
                        #of list of tuples where the first element of the tuple is cat
                        else:
                            y = 0
                            # z returns the crime category of the second element in the tuple list
                            z = tuple_list[y][0] 
                            while (x < z) and (y < len(tuple_list)) :
                                y+=1
                            last_sort_cat = offense_tuple[0]
                            last_sort_location = y
                            tuple_list.insert(y, offense_tuple)
                            x+=1
                        break
                    #Not found in that category move up a category
                    else:
                        x+=1

                    #-out of while loop
                    #find what the position of the next pipe is for
                    #the next search for above
                    pos = offenses_to_parse.find('|') 
                    #This is used to set the crime category
                    crime_cat = max_category
            #--------------------------------------------------------------------
            #This section is used on the last offense a multi-offense crime
            #it is all so used if there is only 1 offense.
            #The premise is that find command checks for more offenses in a crime 
            #report by searching for a pipe(|) and none is found returns -1 
            #
            #Logic is similar to above accept only works one record
            #
            #---------------------------------------------------------------------
            if pos == -1:
                x = 0 
                while (x<5):
                    if offenses_to_parse in crime_cat_list[x]:
                        #Will store the crime category and the crime category in a list together
                        #in a tuple then store that tuple in a list
                        offense_tuple = (x, offenses_to_parse)
                        if x >= max_category:
                            tuple_list.insert(0, offense_tuple)
                            max_category = x
                            last_sort_cat = x
                            last_sort_location = 0
                            x+=1
                            break
                        elif x == last_sort_cat:
                            tuple_list.insert(last_sort_location, offense_tuple)
                            x+=1
                            break
                        else:
                            y = 0
                            # z returns the crime category of the second element in the tuple list
                            z = tuple_list[y][0] 
                            while (x < z) and (y < len(tuple_list)) :
                                y+=1
                            last_sort_cat = offense_tuple[0]
                            last_sort_location = y
                            tuple_list.insert(y, offense_tuple)
                            break
                    x+=1
                crime_cat = max_category    


            #-- Done with looping ------------------------------------------------------------------------------------------------        
            #This section deals with taking the cleaned up records puting it in a json record.
            #   Severity score is calculated
            #   crime categories are adjusted
            #Then dumps the record into a file called: crimes.json
            #---------------------------------------------------------------------------------------------------------------------

            occurrence_time_date_to_parse = row[3]
            occurrence_time_date_to_parse = occurrence_time_date_to_parse.split()
            time = occurrence_time_date_to_parse[1][:-3] 
            date = occurrence_time_date_to_parse[0]
           
            tuple_count = 0
            #Create a list of offense from the sorted to tuple_list             
            while (tuple_count < len(tuple_list)):
                offenses_list.append(tuple_list[tuple_count][1])
                
                #Create the severity
                if tuple_count == 0:
                    severity = options[tuple_list[tuple_count][0]]()
                elif tuple_count == 1: 
                    severity+= options[tuple_list[tuple_count][0]]()/4
                
                tuple_count+=1 

            clean_address = row[6] 
            lat = row[7]
            lng = row[8]
            
            #using the id from the csv to better help find if there are
            #any errors with the data created from this script.
            data['_id'] = record_id


            data['crimeCat'] = crime_cat
            data['date'] = date
            data['time'] = time
            data['offenses'] = offenses_list
            data['lat'] = lat
            data['lng'] = lng
            data['severity'] = severity
            
            number_offenses = len(tuple_list)
            description = ''+str(number_offenses) + ' offense(s) at '+ clean_address 
            data['desc'] = description
            print(data)
            json.dump(data, outfile)
            outfile.write('\n')
            line_count+=1
        else:
            line_count+=1


#Close file, Done,YEET!!!!
infile.close
