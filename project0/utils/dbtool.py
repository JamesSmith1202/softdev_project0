#backend python propro
import sqlite3, authtool


def story_title(storyid):
    db = sqlite3.connect("utils/database.db")
    c = db.cursor()
    c.execute("SELECT * FROM stories WHERE id = %d" %(storyid))
    for row in c: 
        return row[1]

def story_body(storyid):
    db = sqlite3.connect("utils/database.db")
    c = db.cursor()
    c.execute("SELECT * FROM stories WHERE id = %d" %(storyid))
    for row in c: 
        return row[3]


def story_recent(storyid):
    db = sqlite3.connect("utils/database.db")
    c = db.cursor()
    c.execute("SELECT * FROM stories WHERE id = %d" %(storyid))
    for row in c: 
        return row[2]

def create_story(title,body,username):
    db = sqlite3.connect("utils/database.db")
    c = db.cursor()
    c.execute("SELECT * FROM stories;")
    for row in c:
        last = row
    newid = last[0] + 1
    try:
        c.execute('INSERT INTO stories VALUES(?,?,?,?);',(newid,title,body,body))
	db.commit()
    	authtool.add_contribution(username,newid)
    	return True
    except:
	print "oh no"
        return False
    
    db.commit()
    return True

def update_story(storyid,addition,username):
    db = sqlite3.connect("utils/database.db")
    c = db.cursor()
    body = story_body(storyid)
    c.execute('UPDATE stories SET recent = ?, body = ? WHERE id = ?', (addition,body + addition,storyid))
    db.commit()
    authtool.add_contribution(username,storyid)
    db.commit()
    


if __name__ == '__main__':
    print story_title(0)
    print story_body(0)
    print story_recent(0)
    create_story("Goldilocks and the Three Salads","Once upon a time,")

    db.close()