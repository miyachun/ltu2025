#https://opendata.cwa.gov.tw/dist/opendata-swagger.html
import json,urllib.request

import ssl

ssl._create_default_https_context = ssl._create_unverified_context

API_KEY='XXXX'
url='https://opendata.cwa.gov.tw/api/v1/rest/datastore/F-D0047-073?Authorization='+API_KEY+'&ElementName=%E6%BA%AB%E5%BA%A6'

data = urllib.request.urlopen(url).read()
output = json.loads(data)
location=output['records']['Locations'][0]['Location']

'''
for i in location:
    print(f'{i}')
'''


for i in location:
    city = i['LocationName']    # 台中市
    Temp = i['WeatherElement'][0]['Time'][0]['ElementValue'][0]['Temperature']
    
    print(f'{city}未來 3 天溫度{Temp}')
