from email import message
from django.shortcuts import render
from .forms import LoginFields
from email.mime import application
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from Login import forms
from Login.forms import LoginFields
from Login.models import ResultDatabase
from django.db.models import Q
from django.contrib import messages

# Create your views here.


def LoginView(request):
    Result=False
    if request.method=='POST':
        fm=LoginFields(request.POST)
        if fm.is_valid():
            ApplicationId=fm.cleaned_data['ApplicationId']
            RollNumber=fm.cleaned_data['RollNo']
            Data=ResultDatabase.objects.all().filter( Q(Application=ApplicationId) & Q(RollNo=RollNumber))
            if Data:
                
                return render(request,"ResultPage.html",{'data':Data})
            else:
                Result=True
                messages.error(request,"Application Or Roll invalid !!")

    
    field=LoginFields()
    return render(request,'LoginPage.html',{'field':field,'result':Result})