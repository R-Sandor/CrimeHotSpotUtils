import csv
import requests
#Raphael J. Sandor
#1/27/19
#CS41W


GOOGLE_MAPS_API_URL = 'https://maps.googleapis.com/maps/api/geocode/json?&key=AIzaSyAUMJIcUHZdtUOB0TtFzCY13Mc0x33yyy0'
params = {
'address': ' ',
'sensor': 'false',
'region': 'USA'
}

print (params)

outFile = open('addressRow.csv', 'w')
infile = open('2017Crimemapping.csv', 'r')
csv_reader = csv.reader(infile, delimiter=',')
address_writer = csv.writer(outFile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

line_count = 0 
for row in csv_reader:
    if line_count > 1:
        #Process addresses 
        line_count+=1
        row[4]=(row[4].replace("   -", ","))
        address = (row[4].replace("<>", "").replace("BLK", "")) 
        print("Before going to google:  "+ address)
        print("----------------------------------")
        params['address']=address
        req = requests.get(GOOGLE_MAPS_API_URL, params=params)
        res = req.json()
       # print(res)
        result = res['results'][0]
        print(result)
        geodata = dict()
        geodata['lat'] = result['geometry']['location']['lat']
        geodata['lng'] = result['geometry']['location']['lng']
        geodata['address'] = result['formatted_address']
        print('{address}. (lat, lng) = ({lat}, {lng})'.format(**geodata))
        address_writer.writerow([geodata['address'], geodata['lat'], geodata['lng']])
        
    else:    
        line_count+=1
print(line_count)    
infile.close
outFile.close
