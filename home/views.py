from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return HttpResponse('<h1>Alegrosz</h1>')

def contact(request):
    return HttpResponse('<h1>Contact</h1>')
