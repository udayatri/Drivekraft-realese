from flask import Flask,render_template, request
from flask_mysqldb import MySQL
from db import connect,disconnect 


app = Flask(__name__)
 

@app.route('/')
def index():
        obj=connect()
        mycursor = obj.cursor(buffered=True)
        sql="select * from activeTimes"
        mycursor.execute(sql)
        data=mycursor.fetchall() 
        print(data)
        disconnect(obj,mycursor)
        return "Done"

if __name__ == "__main__":
   app.run()