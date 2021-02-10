#imports 
from flask import Flask, session
from flask_restful import Api, Resource
import sqlite3
#conntect to the server
conn = sqlite3.connect('notificationssss.db')
c = conn.cursor()

c.execute('CREATE TABLE IF NOT EXISTS master(title TEXT, notification TEXT)')
class master(Resource):
    def post(self, title, body):
        #inset notification into database
        conn = sqlite3.connect('notificationssss.db')
        c = conn.cursor() 
        sql = "INSERT INTO master VALUES('"+ title + "', '" + body + "')"
        print(sql)
        c.execute(sql)
        conn.commit()
        pass

class person(Resource):
    def get(self):
        #retrive last notification then display it 
         conn = sqlite3.connect('notificationssss.db')
         c = conn.cursor()
         sql = "SELECT * FROM master" 
         c.execute(sql)
         items = c.fetchall()
         length = len(items)
         length = length - 1
         items1 = items[length][0]
         items1 = items1 + ': '
         items2 = items[length][1]
         items = items1 + items2
         print(items)
         return items
#setting up the restfull api
app = Flask(__name__)
api = Api(app)
api.add_resource(person, '/person')
api.add_resource(master, '/master/<string:title>/<string:body>')
if __name__  == "__main__":
    app.run(use_reloader=False, debug=True)
