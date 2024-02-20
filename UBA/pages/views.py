from django.shortcuts import render

# Create your views here.

# THIS THE FUNCTION IS CREATE  THE PAGES 
def index(request):
 return render(request,'pages/index.html')
