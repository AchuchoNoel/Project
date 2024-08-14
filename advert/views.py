from django.shortcuts import render
from django.http import HttpResponse
from django.template import Template
# Create your views here.
def home(request):
    return render(request,'advert/home.html')

def location(request):
    return render(request, 'advert/loc.html')
