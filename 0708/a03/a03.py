from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)
df = pd.read_csv('static/people108.csv')

@app.route('/')
def index():
    dataName=df.iloc[:,1].tolist()
    data=df.iloc[:,4].tolist()
    return render_template("index.html", dataName=dataName,data=data)
  

if __name__ == "__main__":
    app.run(debug=True)
