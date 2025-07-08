from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    dataName=['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
    data=[150, 230, 224, 218, 135, 147, 260]
    return render_template("index.html",dataName=dataName,data=data)

if __name__ == "__main__":
    app.run(debug=True)