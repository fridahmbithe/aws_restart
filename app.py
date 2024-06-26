from flask import Flask
import json 

app = Flask(__name__)
x= '("apples", "guavas", "tomatoes")'
# converting json to python
y= json.dumps(x)

@app.route("/")



def hello_world():
    return f"Hello World {y}"
if __name__== "__main__":
    app.run(debug=True)