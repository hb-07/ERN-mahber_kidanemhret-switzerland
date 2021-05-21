import datetime, os, psycopg2, csv
from flask import Flask, render_template, request, session
from flask_session import Session

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

engine = create_engine("postgresql+psycopg2://Bsrat:asmayt@localhost:5433/mahhberKidanemhret")
db = scoped_session(sessionmaker(bind=engine))


app = Flask(__name__) # i want create a new wep application
                      # and i want this web application to be a flask application.
                      # __name__ represents just this current file



#-----------------------------------------------------------------------------
# route to the index html as default
#--------------------------------------------------------------------------------
@app.route("/") # "/" defines the default page
def index():
    return render_template("index.html") # we pass the headline value to the variable headline in index.html
#-------------------------------------------------------------------------------


#----------------------------------------------------------------
# routes to the form page.
@app.route("/loginForm") # "/" defines the default page
def loginForm():
    return render_template("subPages/login.html" )
#-------------------------------------------------------------


#-----------------------------------------------------------------------------------------------------------------
# process the login data.
#------------------------------------------------------------------------------------------------------------------
@app.route("/membersList&activitities", methods=["POST"]) # "/" defines the default page
def loginProcess():

    # get user data from the login form
    name = request.form.get("username")
    password = request.form.get("password")

    # retriev all username and lastname from the existing database members and save it as a list
    list = db.execute("SELECT username, password FROM members").fetchall()

    # member authentication whether this member really exists
    for member in list:
        # if exists allow the member to go in and show the members list and members activitities
        if name == member.username and password == member.password:
            members = db.execute("SELECT * FROM members order by id").fetchall()
            if members is None:
                return
            else:
                return render_template("subPages/membersList.html", members=members)
    # if member not exist tells them that they are not members yet. and give them hint to register
    if name != member.username or password != member.password:
        return render_template("subPages/loginError.html")
#-----------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------



#--------------------------------------------------------
@app.route("/adminLoginForm") # "/" defines the default page
def adminLoginForm():
    return render_template("subPages/adminLogin.html" )
#-------------------------------------------------------


#-----------------------------------------------------------------------------------------------------------------
# process the addminstration login data.
#------------------------------------------------------------------------------------------------------------------
@app.route("/groupActivitityManagment", methods=["POST"]) # "/" defines the default page
def adminLoginProcess():

    # get user data from the login form
    name = request.form.get("username")
    password = request.form.get("password")

    # retriev all username and lastname from the existing database members and save it as a list
    list = db.execute("SELECT name, password FROM admingroup").fetchall()

    # member authentication whether this member really exists
    for member in list:
        # if exists allow the member to go in and show the members list and members activitities
        if name == member.name and password == member.password:
            members = db.execute("SELECT * FROM members").fetchall()
            if members is None:
                return
            else:
                return render_template("administration.html", members=members)
        if name == member.name and password != member.password:
            return render_template("subPages/hello.html", response ="Username or Password is not correct!")
    # if member not exist tells them that they are not members yet. and give them hint to register
    if name != member.name or password != member.password:
        return render_template("subPages/adminLoginError.html")
#-----------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------







#------------------------------------------------------------
# routes to registration form.
@app.route("/registeratonForm") # "/" defines the default page
def register():
    return render_template("subPages/register.html" )
#-----------------------------------------------------------


#---------------------------------------------------------------------------------------
# Process the registration data.
#---------------------------------------------------------------------------------------

@app.route("/registerationDataProcessed", methods=["POST"]) # "/" defines the default page
def registrationProcess():

    # get the values of the registration form
    username = request.form.get("username")
    lastname = request.form.get("lastname")
    place = request.form.get("place")
    email = request.form.get("email")
    password = request.form.get("password")

    # To avoid user input failers
    username.capitalize()
    lastname.capitalize()
    place.capitalize()
    email.capitalize()
    password.capitalize()

    # check whether the new member not already exit in the members list in the database
    membersList = db.execute("SELECT * FROM members").fetchall()
    for member in membersList:
        if username == member.username and lastname == member.lastname:
            return render_template("subPages/memberExist.html", username=username, lastname=lastname)
        if username == "" or lastname == "" or place == "" or email == "" or password == "":
            return render_template("subPages/registrationError.html")

    # retriev the the id of the last registered member from the database
    row_id = db.execute("SELECT max(id) FROM members").fetchone()
    for i in row_id:
        member_id = i

    # inssert the new meber to the database
    db.execute("INSERT INTO members (id, username, lastname, place, email, password) VALUES(:id, :username, :lastname, :place, :email, :password)",
                                    {"id": member_id+1, "username": username, "lastname": lastname, "place": place, "email": email, "password": password})
    db.commit()
    return render_template("subPages/registrationSuccess.html", name=username)
#-----------------------------------------------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------------------------------------------

@app.route("/deleteForm")
def deleteForm():
    return render_template("subPages/deleteForm.html")

@app.route("/deleteMember")
def deleteProcess():
    id = request.form.get("id")
    list = db.execute("SELECT id FROM members").fetchall()
    for member_id in list:
        if id == member_id.id:
            db.execute("DELETE FROM members WHERE id = :member_id",
                        {"member_id": id})
            return render_template("subPages/deleteSuccess.html", response="Member deleted successfully!")
    db.commit()
    return render_template("subPages/deleteError.html", response="No member with that id =", id=id)




@app.route("/updateForm")
def updateForm():
    return render_template("subPages/update.html")


#-----------------------------------------------------------------------------------------------------------------------------------------------------------
# Update table members in database
#-----------------------------------------------------------------------------------------------------------------------------------------------------------
@app.route("/updateMembers", methods=["POST"]) # "/" defines the default page
def updateMembers():

    # get the values of the update form
    username = request.form.get("username")
    lastname = request.form.get("lastname")
    place = request.form.get("place")
    email = request.form.get("email")
    password = request.form.get("password")

    # To avoid user input failers
    username.capitalize()
    lastname.capitalize()
    place.capitalize()
    email.capitalize()
    password.capitalize()

    # check whether the member want update already exits in the database
    membersList = db.execute("SELECT * FROM members").fetchall()
    for member in membersList:
        if username == member.username and lastname == member.lastname:
            # found and indentify the member's id
            row_id = db.execute("SELECT id FROM members WHERE username = :username and lastname = :lastname", {"username":username, "lastname": lastname}).fetchone()
            for i in row_id:
                member_id = i
            # update member with the founded id
            db.execute("UPDATE members Set username = :username, lastname = :lastname, place = :place, email = :email, password = :password WHERE id = :member_id",
                        {"username": username, "lastname": lastname, "place": place, "email": email, "password": password, "member_id": member_id})
            db.commit()
            return render_template("subPages/updatSuccess.html", username=username)
    # otherwise inform that it is not possible to update
    return render_template("subPages/updateFail.html")
#-----------------------------------------------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------------------------------------------------

@app.route("/messageSent", methods=["POST"])
def message():
    name = request.form.get("name")
    email = request.form.get("email")
    date = request.form.get("date")
    message = request.form.get("message")

    savedMessages = db.execute("SELECT * FROM customer_info").fetchall()
    for msg in savedMessages:
        if message == msg.information and name == msg.name:
            return render_template("subPages/sendMessageFailed.html", name = name)
    db.execute("INSERT INTO customer_info (name, email, date, information) VALUES (:name, :email, :date, :info)",
                {"name": name, "email": email, "date": date, "info": message})
    db.commit()
    return  render_template("subPages/customer_message.html", name=name)

#-------------------------------------------

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


@app.route("/note", methods=["GET", "POST"])
def note():
    if session.get("notes") is None:
        session["notes"] = []
    if request.method == "POST": # if i try to add a note(Button 'Add Note'), this line is called
        note = request.form.get("note")
        session["notes"].append(note)

    return render_template("subPages/processData/index.html", notes=session["notes"])

#------------------------------------------------------------------------------

# insert members into a database from csv filename
#---------------------------------------------------------------------------------
#--------------------------------------------------------------------------------






#----------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------

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

if __name__ == "__main__":
    app.debug(run=True)
