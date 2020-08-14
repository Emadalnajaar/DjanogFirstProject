from django.shortcuts import render
from django.http import HttpResponse

def homepage(request):
    return render(request,"home.html",{})
    #return HttpResponse('homepage')

def about(request):
    return HttpResponse('about me')