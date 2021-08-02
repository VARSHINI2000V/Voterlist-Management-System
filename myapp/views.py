from django.shortcuts import render,redirect
from .models import voters
from django.http.response import HttpResponse
from django.contrib import messages
# Create your views here.



def home(request):
    return render(request,'home.html')

def goadd(request):
        return render(request,'add.html')
def add(request):
    if request.method=="POST":
        name=request.POST['name']
        gender=request.POST['gender']
        age=request.POST['age']
        place=request.POST['place']
        status=request.POST['status']
        s=voters(name=name,gender=gender,age=age,place=place,status=status)
        s.save()
        messages.success(request,"Voter details added successfully!!!")
        return render(request,'add.html')

def display(request):
        profile={'voters':voters.objects.all()}
        return render(request,'display.html',profile) 



def update(request,id):
    bk={'voters':voters.objects.filter(pk=id)}
    return render(request,'update.html',bk) 

def updated(request):
       if request.method=="POST":
           id=request.POST['id']
           name=request.POST['name']
           gender=request.POST['gender']
           age=request.POST['age']
           place=request.POST['place']
           status=request.POST['status']
           bk={'voters':voters.objects.filter(pk=id)}
           s=voters.objects.filter(id=id).update(name=name,gender=gender,age=age,place=place,status=status)
           messages.success(request,"Updated successfully!!!")
           return redirect("/display")


def delete(request,id):
    vote=voters.objects.get(pk=id)
    vote.delete()
    return redirect("/display")


def searchpla(request):
        srecord={'voters':voters.objects.all().distinct('place')}
        return render(request,'searchp.html',srecord)
def splace(request):
        place=request.POST['place']
        profile={'voters':voters.objects.all().filter(place=place)}
        return render(request,'display.html',profile)

def searchgen(request):
        srecord={'voters':voters.objects.all().distinct('gender')}
        return render(request,'searchg.html',srecord)

def sgen(request):
        gender=request.POST['gender']
        profile={'voters':voters.objects.all().filter(gender=gender)}
        return render(request,'display.html',profile)

def cvoter(request):
        a=voters.objects.all().count()
        messages.success(request,a)
        return render(request,'home.html')
