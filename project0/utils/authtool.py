import sqlite3, hashlib

db = sqlite3.connect("database.db")
c = db.cursor()

# Login - Returns true if successful, false otherwise
def login(username, password):
    c.execute("SELECT username, password FROM accounts");
    for account in c:
        user = account[0]
        passw = account[1]
        #print "%s : %s" % (user, hashedPass)
        # Check if user and encrypted password match
        if username == user and encrypt_password(password) == passw:
            print "Successful Login"
            return True
        else:
            print "Login Failed"
            return False

# Encrypt password
def encrypt_password(password):
    encrypted = hashlib.sha256(password).hexdigest()
    return encrypted

# Create account
def create_account(username, password):
    print does_username_exist(username)

# Checks if username exists
def does_username_exist(username):
    c.execute("SELECT username FROM accounts WHERE username = '%s'" % (username))
    for account in c:
        # Username exists
        print "Username exists"
        return True
    print "Username does not exist"
    return False
#create_account(username, password) #- Creates a new entry in .accounts
#does_username_exist(username) #- Returns true if username exists, false otherwise
#encrypt_password(password) #- Returns SHA-256 version of password
#add_contribution(username, storyid) #- Appends storyid to current list of story IDs using eval(idList) and repr(idList)

login("bob", "AS123#sjakld")
print encrypt_password("jasl")

create_account("Mr. Salad", "asldasd")
