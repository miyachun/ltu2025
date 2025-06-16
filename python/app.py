import json
url = open('臺中市停車場收費資訊.json','r',encoding="utf-8")       
data = json.load(url) 


for i in data:
    #print(i)
    print(i['地址'])
    
        