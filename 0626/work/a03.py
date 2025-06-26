import json,urllib.request
import ssl
from datetime import datetime


# ⚠️ 暫時關閉 SSL 憑證驗證 (請留意安全性考量)
ssl._create_default_https_context = ssl._create_unverified_context
API_KEY='XXXX'
url='https://opendata.cwa.gov.tw/api/v1/rest/datastore/F-D0047-075?Authorization='+API_KEY



data = urllib.request.urlopen(url).read()
output = json.loads(data)
location = output['records']['Locations'][0]['Location']
LocationsName=output['records']['Locations'][0]['LocationsName']

for i in location:
    city = i['LocationName']   #區域
    WeatherElement	 = i['WeatherElement'][0]['Time']
    print(f'{LocationsName}的{city}一周溫度:')
    for j in WeatherElement	:
        time=j['StartTime']
        Temperature= j['ElementValue'][0]['Temperature']

        print(f'時間{time}的溫度是{Temperature}')


