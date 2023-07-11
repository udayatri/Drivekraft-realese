from flask import Flask,render_template, request
from flask_mysqldb import MySQL
from db import connect,disconnect 
from otp import sendotp,otpValueByUser
import json

app = Flask(__name__)

@app.route('/sendOtp', methods = ['GET', 'POST'])
def sendOtp():
        return sendotp()

@app.route('/otpvaluebyUser', methods = ['GET', 'POST'])
def otpvaluebyuser():
        return otpValueByUser()

if __name__ == "__main__":
   app.run()