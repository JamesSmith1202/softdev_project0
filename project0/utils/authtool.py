#authtool
import sqlite3, hashlib

# Login - Returns true if successful, false otherwise
def login(username, password):
    db = sqlite3.connect("utils/database.db")
    c = db.cursor()
    c.execute("SELECT username, password FROM accounts WHERE username = '%s'" % (username));
    for account in c:
        user = account[0]
        passw = account[1]
        # Check if user and encrypted password match
        if username == user and encrypt_password(password) == passw:
            print "Successful Login"
            return True
    print "Login Failed"
    return False

# Encrypt password - SHA256
def encrypt_password(password):
    encrypted = hashlib.sha256(password).hexdigest()
    return encrypted

# Create account - Returns true if successful, false otherwise
def create_account(username, password):
    db = sqlite3.connect("utils/database.db")
    c = db.cursor()
    if not does_username_exist(username):
        # Add user to accounts table
        c.execute("INSERT INTO accounts VALUES('%s', '%s', '[]')" % (username, encrypt_password(password)))
        db.commit()
        db.close()
        print "Create Account Successful"
        return True
    print "Create Account Failed"
    return False

# Checks if username exists - Returns true if username exists, false otherwise
def does_username_exist(username):
    db = sqlite3.connect("utils/database.db")
    c = db.cursor()
    c.execute("SELECT username FROM accounts WHERE username = '%s'" % (username))
    for account in c:
        # Username exists
        print "Username exists"
        return True
    print "Username does not exist"
    return False

# Add contribution
def add_contribution(username, storyid):
    db = sqlite3.connect("utils/database.db")
    c = db.cursor()
    # Turn string into list
    storyids = contributed_list(username)
    # Append new story id
    storyids.append(storyid)
    # Turn list back into a string
    id_list = repr(storyids)
    c.execute("UPDATE accounts SET stories = '%s' WHERE username = '%s'" % (id_list, username))
    db.commit()
    db.close()
    print "Contribution added succesfully"

# Did contribute to story - Returns true if contributed, otherwise false
def did_contribute(username, storyid):
    storyids = contributed_list(username)
    for s_id in storyids:
        if s_id == storyid:
            print "User has contributed to story"
            return True
    print "User has not contributed to story"
    return False

# Return list of available story ids
def available_list(username):
    db = sqlite3.connect("utils/database.db")
    c = db.cursor()
    # Get story id list
    available_stories = []
    all_stories = []
    user_stories = contributed_list(username)
    # All stories
    c.execute("SELECT id FROM stories")
    for s_id in c:
        all_stories.append(s_id[0])

    # Populate available_stories
    for s_id in all_stories:
        if not s_id in user_stories:
            available_stories.append(s_id)
    return available_stories

# Returns user's contributed list
def contributed_list(username):
    db = sqlite3.connect("utils/database.db")
    c = db.cursor()
    c.execute("SELECT stories FROM accounts WHERE username = '%s'" % (username))
    for stories in c:
        storyids = eval(stories[0])
        return storyids
