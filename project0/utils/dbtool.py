#backend python propro
import sqlite3, authtool

db = sqlite3.connect("database.db")
c = db.cursor()


def story_title(storyid):
    c.execute("SELECT * FROM stories WHERE id = %d" %(storyid))
    for row in c: 
        return row[1]

def story_body(storyid):
    c.execute("SELECT * FROM stories WHERE id = %d" %(storyid))
    for row in c: 
        return row[3]


def story_recent(storyid):
    c.execute("SELECT * FROM stories WHERE id = %d" %(storyid))
    for row in c: 
        return row[2]

def create_story(title,body):
    c.execute("SELECT * FROM stories")
    for row in c:
        last = row
    newid = last[0] + 1
    try:
        c.execute('INSERT INTO stories VALUES(%d,"%s","%s","%s")' %(newid,title,body,body))
    except:
        return False
    
    db.commit()
    return True

def update_story(storyid,addition,username):
    body = story_body(storyid)
    c.execute('UPDATE stories SET recent = "%s", body = "%s" WHERE id = %d' %(addition,body + addition,storyid))
    db.commit()
    authtool.add_contribution(username,storyid)
    db.commit()
    


if __name__ == '__main__':
    print story_title(0)
    print story_body(0)
    print story_recent(0)
    create_story("Goldilocks and the Three Salads","Once upon a time,")


    ''' 
    print story_title(1)
    print story_body(1)
    print story_recent(1)
    update_story(1,' They smelled delicious', 'Mr. Salad')
    print story_title(1)
    print story_body(1)
    print story_recent(1)
    '''


    db.close()
