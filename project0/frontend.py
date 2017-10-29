#frontend flaskapp
import os

from utils.dbtool import *
from utils.authtool import *

from flask import Flask, redirect, url_for, render_template, session, \
	request, flash

USER_SESSION = "logged_in"


app = Flask(__name__)
app.secret_key = os.urandom(16)

def add_session(username, password):
	'''
	Checks user's credentials and will add the login session if they match
	Returns True if successful, False otherwise
	'''
	
	if authtool.login(username, password):
		session[USER_SESSION] = username
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
		print request.form
		if "log_out" in request.form:
			print "calling logout"
			logout()
			return redirect(url_for("home"))
	
	if USER_SESSION in session:
		#do some fancy template stuff
		
		ids = contributed_list(session[USER_SESSION])
		
		contributed_stories = []
		for story in ids:
			temp = []
			temp.append(story)
			temp.append(story_title(story))
			print "%d, %s"%(temp[0],temp[1])
			contributed_stories.append(temp)
		
		print contributed_list(session[USER_SESSION])
		return render_template("home.html",
			stories_contributed=contributed_stories,
			logged_in=True)
		
		pass
	
	return render_template("home.html", logged_in=False)
	#return "It works"

@app.route("/login", methods=["GET", "POST"])
def login():
	if USER_SESSION in session:
		return redirect(url_for("home"))
	print "method: %s"%(request.method)
	
	#is user trying to log in or register
	if request.method == "POST":
		print "form: %s"%(request.form)
		#print "form: %s"%(request.form["login"])
		if "login" in request.form:
			print "Login user %s and pass %s"%(request.form["username"], 
				request.form["password"])
			if add_session(
				request.form["username"],
				request.form["password"]
			):
				return redirect(url_for("home"))
			else:
				flash("Incorrect login")
				return render_template("login.html")
		elif "register" in request.form:
			username = request.form["username"]
			password = request.form["password"] 
			print "Register user %s and pass %s"%(
				username, password)
			if username != "" or password != "":
				if create_account(request.form["username"], 
						request.form["password"]):
					flash("registration successful")
				else:
					flash("username taken")
			else:
				flash("blank fields")
			return render_template("login.html")
	else:
		return render_template("login.html")
		#return "It works"

@app.route("/create", methods=["GET", "POST"])
def create():
	'''
	Route for creating a new story
	'''
	
	if not(USER_SESSION in session):
		return redirect(url_for("login"))
	
	if request.method == "POST":
		title = request.form["title"]
		body = request.form["body"]
		print "title: %s, body: %s, user: %s"%(title, body,session[USER_SESSION])
		
		if create_story(title, body, session[USER_SESSION]):
			return redirect(url_for("home"))
		else:
			flash("story creation failed, try a different title")
			return render_template("create.html")
			
	
	return render_template("create.html")
	#return "It works"

@app.route("/available")
def available():
	'''
	Displays a list of stories the user hasn't contributed to yet
	'''
	
	if not(USER_SESSION in session):
		return redirect(url_for("login"))
	
	ids = available_list(session[USER_SESSION])
	
	available = []
	for story in ids:
		temp = []
		temp.append(story)
		temp.append(story_title(story))
		#print "%d, %s"%(temp[0],temp[1])
		available.append(temp)
	
	return render_template("available.html", stories_available=available)
	#return "It works"

@app.route("/page", methods=["GET", "POST"])
def page():
	'''
	Displays a single story
	if user has contributed, just view story
	otherwise, display the most recent section of the story
	and a form to add another section
	'''	
	
	if request.method == "POST":
		contribution = request.form["body"]
		story_id = int(request.form["story_id"])
		
		if contribution != "":
			update_story(story_id,
				" " + contribution, #creating a space before so that the last and first words of the contributions arent stuck together
				session[USER_SESSION])
			flash("Successfully added contribution")
			return redirect(url_for("home"))
		else:
			flash("Please enter content and try again")
			return redirect(url_for("available"))
	
	if not(USER_SESSION in session):
		return redirect(url_for("home"))
	
	if "id" in request.args:
		story_id = int(request.args["id"])
		title = story_title(story_id)
		contributed = did_contribute(session[USER_SESSION], story_id)
		content = ""
		
		if contributed:
			content = story_body(story_id)
		else:
			content = story_recent(story_id)
		
	
	return render_template("page.html",
		story_id=story_id,
		page_title=title,
		story_content=content,
		user_contributed=contributed)
	#return "It works"

if __name__ == "__main__":
	app.debug = True
	app.run()


