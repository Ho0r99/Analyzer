from django.shortcuts import render

# Create your views here.

# THIS THE FUNCTION IS CREATE  THE PAGES 
def index(request):
 return render(request,'pages/index.html',)

def Register(request):
  return render(request,'pages/Register.html',)

def Login(request):
  return render(request,'pages/Login.html') 
