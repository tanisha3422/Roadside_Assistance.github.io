from django.shortcuts import render, HttpResponse

def index(request):
    return render(request,'Home.html')


def About(request):
    return render(request,'About.html')

def FAQ(request):
    return render(request,'FAQ.html')
   
  
