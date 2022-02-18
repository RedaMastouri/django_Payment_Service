# here we are going to map urls and view functions
import imp
from re import L
from urllib.parse import urlparse
import django


from django.urls import path
#from current folder, import views
from . import views
from playground import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


'''
Now we declare a special variable called urlpatterns
'''
# Here we have a so-called URLConf 
#playground/hello
urlpatterns = [
    path("", views.home, name="home"),
    path('hello/<name>', views.say_hello, name="hello"),
    path('home/', views.home, name="home"),
    path("startup/", views.startup, name="startup"),
    path("mouth/", views.mouth, name="mouth"),

]

#this folder is here to locate the images from img
urlpatterns += staticfiles_urlpatterns()
