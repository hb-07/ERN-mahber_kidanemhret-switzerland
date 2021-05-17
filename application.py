import datetime
from flask import Flask, render_template, request, session
from flask_session import Session



app = Flask(__name__) # i want create a new wep application
                      # and i want this web application to be a flask application.
                      # __name__ represents just this current file
@app.route("/") # "/" defines the default page
def index():
    return render_template("index.html") # we pass the headline value to the variable headline in index.html


# routes to the form page.
@app.route("/loginForm") # "/" defines the default page
def loginForm():
    return render_template("subPages/login.html" )

# process the login data.
@app.route("/membersList&activitities", methods=["POST"]) # "/" defines the default page
def loginProcess():
    name = request.form.get("username")
    password = request.form.get("password")
    if name == "" or password == "":
        return render_template("subPages/error.html")
    else:
        return render_template("subPages/membersList.html")

# routes to registration form.
@app.route("/register") # "/" defines the default page
def register():
    return render_template("subPages/register.html" )

# Process the registration data.
@app.route("/registration/dataProcessed", methods=["POST"]) # "/" defines the default page
def registerProcessed():
    username = request.form.get("username")
    lastname = request.form.get("LastName")
    place = request.form.get("adress")
    email = request.form.get("email")
    password = request.form.get("password")
    
    if username == "" or lastname == "" or email == "" or password == "":
        print("Sorry your data are not registered!, you have to fill out all required fields to register!")
    else:
        return render_template("subPages/success.html", name=username)

@app.route("/memberProfiles")
def membersProfile():
    return render_template("subPages/members.html")

@app.route("/completedActivities")
def completedActivities():
    return render_template("subPages/info.html")

@app.route("/generalInformation")
def information():
    return render_template("subPages/info.html")


@app.route("/form") # "/" defines the default page
def form():
    return render_template("subPages/layout/form.html" )

@app.route("/page1") # "/" defines the default page
def page1():
    return render_template("subPages/layout/page1.html" )

@app.route("/page2") # "/" defines the default page
def page2():
    return render_template("subPages/layout/page2.html" )

@app.route("/respondForm", methods=["POST"]) # here mehtods is part of the route, if you give /hello it doesnt going to work
def respondForm():
    #get the value of name in the form
    name = request.form.get("name") # "name" represents the name value defined in input tag in hello.html
    return render_template("subPages/hello.html", name=name )
#----------------------------------
# using sessions process user data in serverside
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

notes = []

@app.route("/note", methods=["GET", "POST"])
def note():
    if session.get("notes") is None:
        session["notes"] = []
    if request.method == "POST": # if i try to add a note(Button 'Add Note'), this line is called
        note = request.form.get("note")
        session["notes"].append(note)

    return render_template("subPages/processData/index.html", notes=session["notes"])

#-----------------------------------------

@app.route("/isitnewyear")
def isitnewyear():
    now = datetime.datetime.now()
    new_year = now.month == 1 and now.day == 1
    new_year = True
    return render_template("isItNewyear.html", newYear = new_year)

@app.route("/<string:name>") # "/" defines the default page
def hello(name):
    name = name.capitalize()
    return f"<h1>Hello, {name}!</h1>"
