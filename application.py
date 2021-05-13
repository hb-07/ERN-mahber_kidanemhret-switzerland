import datetime
from flask import Flask, render_template
app = Flask(__name__) # i want create a new wep application
                      # and i want this web application to be a flask application.
                      # __name__ represents just this current file
@app.route("/") # "/" defines the default page
def index():
    return render_template("index.html") # we pass the headline value to the variable headline in index.html


@app.route("/<string:name>") # "/" defines the default page
def hello(name):
    name = name.capitalize()
    return f"<h1>Hello, {name}!</h1>"


@app.route("/login") # "/" defines the default page
def login():
    return render_template("subPages/login.html" )

@app.route("/register") # "/" defines the default page
def register():
    return render_template("subPages/register.html" )

@app.route("/isitnewyear")
def isitnewyear():
    now = datetime.datetime.now()
    new_year = now.month == 1 and now.day == 1
    new_year = True
    return render_template("isItNewyear.html", newYear = new_year)
