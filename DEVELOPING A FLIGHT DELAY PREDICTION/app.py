from flask import Flask,request,render_template
import numpy as np
import pandas as pd
import pickle
import os
model=pickle.load(open('flight.pkl','rb'))
app=Flask (___name___)
@app.route('/')
def home():
    return render_template("home.html")

@app.route('\prediction',methods=['POST'])

def predict():
    name = request.form['name']
    month = request.form['month']
    dayofmonth = request.form['dayofmonth']
    dayofweek = request.form['dayofweek']
    orgin = request.form['orgin']
    if(origin == "msp");
        origin1,origin2,origin3,origin4,origin5 =0,0,0,0,1
         if(origin == "dtw");
        origin1,origin2,origin3,origin4,origin5 =0,0,0,0,1
         if(origin == "jfk");
        origin1,origin2,origin3,origin4,origin5 =0,0,0,0,1
        if(origin == "sea");
        origin1,origin2,origin3,origin4,origin5 =0,0,0,0,1
         if(origin == "alt");
        origin1,origin2,origin3,origin4,origin5 =0,0,0,0,1

        
