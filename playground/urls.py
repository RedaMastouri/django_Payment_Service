# here we are going to map urls and view functions
from urllib.parse import urlparse
import django


from django.urls import path
#from current folder, import views
from . import views


'''
Now we declare a special variable called urlpatterns
'''
# Here we have a so-called URLConf 
#playground/hello
urlpatterns = [
    path('hello/', views.say_hello)

]