from flask import Flask
import json
from config import dev, sum

app = Flask("server")

@app.get("/")
def hello():
    return "Hello from Flask"

@app.get("/test")
def test():
    return "Test Page!"


#/about
@app.get("/about")
def about():
    return "Thomas Marcello!"


####################### API METHODS ############################
################################################################

@app.get("/api/developer")
def developer():
    return json.dumps(dev)

@app.get("/api/sum")
def simple_sum():
    answ = sum(21,21)
    return json.dumps(answ)


# start the server
app.run(debug=True)

