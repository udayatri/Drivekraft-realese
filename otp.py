from flask import Flask,render_template, request
from flask_mysqldb import MySQL
from db import connect,disconnect 
from datetime import datetime
import json

def sendotp():
        obj = json.loads(request.data)
        contact = obj['phone']
        otp=obj['otp']
        now = datetime.now()
        obj=connect()
        mycursor = obj.cursor(buffered=True)
        sql= f"Insert into OTP(user_contact,otpvalue,created,updated) values('{contact}','{otp}','{now}','{now}')"
        mycursor.execute(sql)
        obj.commit()
        disconnect(obj,mycursor)
        return "done"

def otpValueByUser():
        obj = json.loads(request.data)
        contact = obj['phone']
        status=obj['status']
        now = datetime.now()
        obj=connect()
        mycursor = obj.cursor(buffered=True)
        query=f"select id from otp where user_contact='{contact}' ORDER BY created DESC limit 1"
        mycursor.execute(query)
        data=mycursor.fetchall() 
        data=str(data)
        length=len(data)-3
        data=data[2:length]
        print(data)
        sql=f"UPDATE otp SET user_contact='{contact}',state='{status}',updated='{now}' WHERE id = '{data}'"
        print(sql)
        mycursor.execute(sql)
        obj.commit()
        disconnect(obj,mycursor)
        return "Done"
