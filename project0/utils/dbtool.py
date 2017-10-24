#backend python propro
import sqlite3

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
    c.execute('INSERT INTO stories VALUES(%d,"%s","%s","%s")' %(newid,title,body,body))
    db.commit()
    
    


if __name__ == '__main__':
    print story_title(0)
    print story_body(0)
    print story_recent(0)
    create_story("Goldilocks and the Three Salads","Once upon a time,")
    print story_title(1)
    print story_body(1)
    print story_recent(1)



    db.close()
