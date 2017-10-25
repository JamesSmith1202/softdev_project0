#frontend flaskapp
import os

#from utils.dbtool import *

from flask import Flask, redirect, url_for, render_template, session, \
	request

'''
TODO
pass page_title var to template based on the next page they are requesting
'''

USER_SESSION = "logged_in"


app = Flask(__name__)
app.secret_key = os.urandom(16)

def add_session(username, password):
	'''
	Checks user's credentials and will add the login session if they match
	Returns True if successful, False otherwise
	'''
	
	if login(username, password):
		session[USER_SESSION] = user
		return True
	return False

def logout():
	'''
	Just logs the user out
	'''
	
	if USER_SESSION in session:
		session.pop(USER_SESSION)


#~~~~~~~~~~~~~ROUTE CODE GOES BELOW~~~~~~~~~~~~~~~~

@app.route("/")
def root():
	return redirect(url_for("home"))

#for now, logout requests are handled here
@app.route("/home", methods=["GET", "POST"])
def home():
	'''
	Main website page
	
	If user not logged in, shows instructions
	otherwise, shows stories the user contributed to
	
	Will also handle logout requests
	'''
	
	if request.method == "POST":
		if request.form["Log out"]:
			logout()
			return redirect(url_for("home"))
	
	if USER_SESSION in session:
		#do some fancy template stuff
		pass
	
	#return render_template("home.html")
	return "It works"

@app.route("/login", methods=["GET", "POST"])
def login():
	if USER_SESSION in session:
		return redirect(url_for("home"))
	
	#is user trying to log in or register
	if request.method == "POST":
		if request.form["LOGGING IN"]:
			if add_session(
				request.form["username"],
				request.form["password"]
			):
				return redirect(url_for("home"))
			else:
				flash("Incorrect login")
				#return render_template("login.html")
				return 
		elif request.form["REGISTERING"]:
			pass
	else:
		#return render_template("login.html")
		return "It works"

@app.route("/create")
def create():
	'''
	Route for creating a new story
	'''
	
	if not(USER_SESSION in session):
		return redirect(url_for("home"))
	
	#return render_template("create.html")
	return "It works"

@app.route("/available")
def available():
	'''
	Displays a list of stories the user hasn't contributed to yet
	'''
	
	if not(USER_SESSION in session):
		return redirect(url_for("home"))

	#return render_template("available.html")
	return "It works"

@app.route("/page")
def page():
	'''
	Displays a single story
	if user has contributed, just view story
	otherwise, display the most recent section of the story
	and a form to add another section
	'''	
	
	if not(USER_SESSION in session):
		return redirect(url_for("home"))

	#return render_template("page.html")
	return "It works"

if __name__ == "__main__":
	app.debug = True
	app.run()


