# django_Payment_Service
Django-based Payment Service v1.0


# intallation steps:
```
pip 3 install pipenv
pipenv install django
```

# Launching the subshell in virtual environment
```
pipenv shell
```

# Start Django-admin 
With a suffix ".", we are telling django to use the current projectname as current main directory
```
django-admin startproject paymentservice .
```
# Django-Skeleton
Please refer to the following link: >> https://django-project-skeleton.readthedocs.io/en/latest/structure.html

# Configuring Django's settings
without having runserver error for django, we use the following command on teh manage.py which is the app WRAPPER with a custom port number e.g. 9000
```
python manage.py runserver 9000
```
<a href="#" target="_blank" rel="noreferrer"><img alt="Django_Welcome_Screen" style="text-align: center; width: 100%;" src="img/welcome.PNG" /></a>

# installing Python interpreter
1. (Ctrl+Shift+P) on VSCode 
2. get the actual environment URL
```
pipenv --venv
```

copy the path 
e.g. "C:\Users\rmastour\.virtualenvs\django_Payment_Service-hKmBDVso"

3. install interpreter path (Ctrl+Shift+P) and type 
```
>python: select Interpeter
```
> by pasting the latter path 
"C:\Users\rmastour\.virtualenvs\django_Payment_Service-hKmBDVso\bin\python"

4. use the + sign on top right corner of terminal to open as many terminals as you wish 
5. (CTRL+L) to clear the window 

# Creating  a new playground app 
1. run this command
```
python manage.py startapp playground
```
2. Go back to the project setting.py and add the app name 
```
'playground', #here to add the newest app to settings.py
```

# Manipulating the app views

```
# Create your views here.
# A view function is a function that takes a request and return a response
# request -> response
# More accurately, it is a request handler 
# in some other frameworks, it is called an "Action"
# from architecture point of view, a view is often assosiated with somethign that user sees
# That part in Django is called "Template"


def say_hello(request):
    #What we can do is the following 
    '''
    1. Pull data from a DB
    2. Transfrom data 
    3. send an email 
    4. and so on..
    '''
    reponse = HttpResponse('Hello there!') #this one needs to be mapped to a URL
    #So when we get a request at that URL, this function will be called 
    return reponse 
```

# Mapping a URL to the newly created view 
1. in the project folder, let's create a file called "urls.py"
```
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
```

2.  Now we go to the main urls.py of the project 
```
from django.contrib import admin
from django.urls import path

# now let's add these libraries
from django.contrib import admin
from django.urls import path, include

from playground import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('playground/', include('playground.urls')), #newly added
]
```

# adding template 
1. in app folder, let's create another folder called "templates"
2. in "templates" we add a new html file called "hello.html"
```
<h1>{{name}}'s Portfolio Section:</h1>
```
3. back to view function, instead of returning HttpResponse('string blabla'), we will use the render function to render a template and return a html markup to the client 
4. in views.py
```
def say_hello(request):
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
    reponse = render(request, 'hello.html', {'name': 'Reda'}) # we add 3rd params as dictionary
    return reponse 
``` 

# Debugging Django
1. Click "Run and Debug Panel" on VSCode
2. Click on "Create a launch.json file"
3. in the popped-up list, choose "Django"
4. The code looks lke:
```
{
    // Use IntelliSense to learn about possible attributes.
    // Hover to view descriptions of existing attributes.
    // For more information, visit: https://go.microsoft.com/fwlink/?linkid=830387
    "version": "0.2.0",
    "configurations": [
        {
            "name": "Python: Django",
            "type": "python",
            "request": "launch",
            "program": "${workspaceFolder}\\manage.py",
            "args": [
                "runserver",
                "9000"
            ],
            "django": true
        }
    ]
}              
```

# Using Django Debug toolbar
1. install via pipenv
```
pipenv install django-debug-toolbar
```
2. add 'debug_toolbar', in the installed INSTALLED_APPS
3. CTRL+P to bring the seacrh box and search for settings.py
```
INSTALLED_APPS = [
    'django.contrib.admin', #give admin interface to manage the data
    'django.contrib.auth', #this used to authenticate the users in the app
    'django.contrib.contenttypes',
    #'django.contrib.sessions', #this manages the user's data
    'django.contrib.messages', # used to display notification to the user 
    'django.contrib.staticfiles', # this to manage the static files like CSS and images 
    # we also need to add all the newly created apps in here ~ Reda
    'playground', #here hour first beta app
    'debug_toolbar', #for debugging
]
```
4. Adding a new path to the URLConf module of the project folder 
```
urlpatterns = [
    path('admin/', admin.site.urls),
    path('playground/', include('playground.urls')), #newly added
    path('__debug__/', include('debug_toolbar.urls')), #newly added
]
```
5. Enabling a middleware to hook into django's request response processing. 
In our settings module we have a setting called MIDDLEWARE
```
MIDDLEWARE = [
    'debug_toolbar.middleware.DebugToolbarMiddleware', #Newly added for debugging
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    
]
```
6. Configuring Internal IPs:
```
#Configuring Internal IPs
INTERNAL_IPS = [
    # .. 
    '127.0.0.1',
    # ..
]
```