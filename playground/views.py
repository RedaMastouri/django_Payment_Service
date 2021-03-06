from cgitb import html
from re import T
from urllib import response
from django.shortcuts import render
#here we add this library
from django.http import HttpResponse
from datetime import datetime

# Create your views here.
# A view function is a function that takes a request and return a response
# request -> response
# More accurately, it is a request handler 
# in some other frameworks, it is called an "Action"
# from architecture point of view, a view is often assosiated with somethign that user sees
# That part in Django is called "Template"


def say_hello(request, name):
    #What we can do is the following 
    '''
    1. Pull data from a DB
    2. Transfrom data 
    3. send an email 
    4. and so on..
    '''
    #reponse = HttpResponse('Hello there! I work for Fulcrum Digital Inc.') #this one needs to be mapped to a URL
    #So when we get a request at that URL, this function will be called 
    
    #render html
    reponse = render(request, 
                    'hello.html', 
                    {'name': name,
                    'date': datetime.now()
                    }) # we add 3rd params as dictionary
    return reponse 


def home(request): 
    jawab = render(request, 
                    'home.html',) # we add 3rd params as dictionary
    
    return jawab

def startup(request):
    return render(request, "hello.html", {"name": "bel contra 3lik"})


'''
Stream the camera 
'''

def calculate():
    x = 1
    return x

def mouth(request):
    x = calculate()
    return render(request, "mouth.html", {"name": x})
'''
Debug toolbar:
'''
# this debug toolbar car serve to merge both the cut point and conf modeu