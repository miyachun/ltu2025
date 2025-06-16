import json
from flask import Flask, render_template


app = Flask(__name__)
myD={'sarea':[],'name':[],'addr':[]}

@app.route('/')
def index():      

    url = open('臺中市停車場收費資訊.json','r',encoding="utf-8")       
    data = json.load(url)    
    
    location=data
   
    for i in location:
        #print(i)
        sarea=i['項次']
        name = i['停車場名稱']
        addr=i['地址']               
                
        #a=strT+city
        myD['sarea'].append(sarea)
        myD['name'].append(name)
        myD['addr'].append(addr)       
        

        
    return render_template('index.html',a=myD)


if __name__ == '__main__':
    app.run()