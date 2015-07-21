# -*- coding:utf-8 -*-
import web, datetime

#db = web.database(dbn='mysql',user='shen', pw='shen', db='blog', charset='utf8')
db = web.database(dbn='sqlite', db='.\\DATA\\blog.db')
def get_posts():
    return db.query("SELECT id, title, content, datetime(posted_on) as posted_on FROM blogs order by id")
    #return db.select('entries', order='id DESC')

def get_post(id):
    try:
        return db.select('blogs', where='id=$id', vars=locals())[0]
    except IndexError:
        return None

def new_post(title, text):
    db.insert('blogs', title=title, content=text, posted_on=datetime.datetime.now())

def del_post(id):
    db.delete('blogs', where="id=$id", vars=locals())

def update_post(id, title, text):
    db.update('blogs', where="id=$id", vars=locals(),
        title=title, content=text)
