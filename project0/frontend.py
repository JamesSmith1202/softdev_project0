#frontend flaskapp
import os

from flask import Flask, redirect, url_for, render_template, session, \
	request

'''
TODO
pass page_title var to template based on the next page they are requesting
'''

USER_SESSION = "logged_in"


app = Flask(__name__)
app.secret_key = os.urandom(16)

def add_session(user):
	if login()
	session[USER_SESSION] = user
	pass

def logout():
	'''
	Just logs the user out
	'''
	if USER_SESSION in session:
		session.pop(USER_SESSION)

@app.route("/")
def root():
	return redirect(url_for("home"))

@app.route("/home")
def home():
	#return render_template("home.html")
	return "It works"

@app.route("/login", methods=["GET", "POST"])
def login():
	if 
	#return render_template("login.html")
	return "It works"

@app.route("/create")
def create():
	#return render_template("create.html")
	return "It works"

@app.route("/available")
def available():
	#return render_template("available.html")
	return "It works"

@app.route("/page")
def page():
	#return render_template("page.html")
	return "It works"

if __name__ == "__main__":
	app.debug = True
	app.run()
