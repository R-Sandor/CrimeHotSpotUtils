import csv
#Raphael J. Sandor
#1/27/19
#CS41W
#Fixes the address in a CSV so they may be geocoded.

from geopy.geocoders import Nominatim
geolocator = Nominatim(user_agent="Crime HotSpot")
location = geolocator.geocode("1000 W 41st ST, Norfolk")
print(location)

infile = open('2017Crimemapping.csv', 'r+')
csv_reader = csv.reader(infile, delimiter=',')
line_count = 0 
for row in csv_reader:
    if line_count > 1:
        #Process addresses 
        line_count+=1
        row[4]=(row[4].replace("   -", ","))
        address = (row[4].replace("<>", "").replace("BLK", "")) 
        print(address)
                
    else:    
        line_count+=1
print(line_count)    
infile.close
