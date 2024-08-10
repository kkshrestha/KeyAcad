from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse("Home ")

def index(request):
    return render(request, 'my_app/index.html')

def viewcertificate(request):
    return render(request, 'my_app/viewcertificate.html')


# Create your views here.
