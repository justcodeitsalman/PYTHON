from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
import os

#Create your views here.

def Hello_World_Fun(request):
    date={'date': str(Current_date_time()), 'hostname': Host_Details(),'name':'salman','rollno':'3','marks':'100','list':[10,20,30,40]}
    response= render(request,'Testapp/home.html',context=date)
    return response

def Current_date_time():
    now = str(datetime.now().year)
    return now

def Host_Details():
    hostname=os.uname()[1]
    return hostname

def main(request):
    dict={}
    return render(request,"Testapp/main.html",dict)

def Login(request):
    dict={}
    return render(request,"Testapp/login.html",dict)

def join(request):
    dict={}
    return render(request,"Testapp/join.html",dict)
