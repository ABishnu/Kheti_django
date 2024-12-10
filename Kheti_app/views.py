from django.shortcuts import render
from django.template import loader
import pandas as pd
import numpy as np
from util.fertilizer import fertilizer_dic
import pickle
import mysql.connector as sql

email = ''
password = ''
confirmpassword = ''

with open('C:/Users/bbish/OneDrive/Documents/Python Program/DJango/Kheti/saved_models/Pickle_RF_Model.pkl', 'rb') as f:
    model = pickle.load(f)


# Create your views here.
def Home(request):
    return render(request,'index.html')
def sign(request):
    global email,password,confirmpassword
    if request.method=="POST":
        m = sql.connect(host="localhost",user="root",passwd="#Bishnu@123",database="login")
        cursor=m.cursor()
        d=request.POST
        for key,value in d.items():
            if key=="email": 
                email = value
            if key == "password":
                password = value
            if key == "confirmpassword":
                confirmpassword = value
        c="insert into users Values('{}','{}','{}')".format(email,password,confirmpassword)   
        cursor.execute(c)
        m.commit()
    return render(request,'login.html') 
def Crop_recommend(request):
    return render(request,'crop.html')
def crop_prediction(request):
    Nitrogen = request.POST.get('Nitrogen')
    Phosphorus = request.POST.get('Phosphorus')
    Potassium = request.POST.get('Potassium')
    Temperature = request.POST.get('Temperature')
    Humidity = request.POST.get('Humidity')
    ph = request.POST.get('ph')
    Rainfall = request.POST.get('Rainfall')
    y_pred = model.predict([[Nitrogen,Phosphorus,Potassium,Temperature,Humidity,ph,Rainfall]])

    return render(request, 'crop-result.html',{'prediction': y_pred})
def Fertilizer_recommendation(request):
    return render(request,'fertilizer.html')
def Fertilizer_prediction(request):
    crop_name = request.POST.get('crop_name')
    N = request.POST.get('Nitrogen')
    N = int(N)
    P = request.POST.get('Phosphorus')
    P = int(P)
    K = request.POST.get('Potassium')
    K = int(K)
    # ph = float(request.form['ph'])

    df = pd.read_csv('Data/fertilizer.csv')

    nr = df[df['Crop'] == crop_name]['N'].iloc[0]
    nr = nr.astype(int)
    pr = df[df['Crop'] == crop_name]['P'].iloc[0]
    pr = pr.astype(int)
    kr = df[df['Crop'] == crop_name]['K'].iloc[0]
    kr = kr.astype(int)

    n = nr - N
    p = pr - P
    k = kr - K
    temp = {abs(n): "N", abs(p): "P", abs(k): "K"}
    max_value = temp[max(temp.keys())]
    if max_value == "N":
        if n < 0:
            key = 'NHigh'
        else:
            key = "Nlow"
    elif max_value == "P":
        if p < 0:
            key = 'PHigh'
        else:
            key = "Plow"
    else:
        if k < 0:
            key = 'KHigh'
        else:
            key = "Klow"

    response = fertilizer_dic[key]
    return render(request, 'fertilizer-result.html', {'recommendation' : response})

def Disease_prediction(request):
    return render(request,'disease.html')