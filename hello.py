print("Hello, here are your clocks so you stop procrastinating")


# website: http://127.0.0.1:8000
# python manage.py runserver   
#  


"""
### __1__ INITIAL EDITS - SZKIELET
in powershel run:
- python -m venv .venv
- .venv\Scripts\Activate.ps1
- python -m pip install django
- python -m django --version

szkielet Django:
in powershel run:
- django-admin startproject config .
- python manage.py startapp timers
this runs server:  python manage.py runserver
this is the site: http://127.0.0.1:8000/

all of this creates a structure (config directory and timers directory with files, manage.py, .venv)

when issues run:
python manage.py migrate
"""


"""
### __2__ FIRST SITE
In file config/settings.py change INSTALLED_APPS to
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'timers',
]
because django needs to know that timers are a part of this project. we can then use it's views, models, templates etc.


Find file timers/views.py and change it to:
from django.shortcuts import render
def home(request):
    return render(request, 'timers/home.html')

home - function that handles the request to enter the page
request - has information about browser's requests
render() - returns HTML website to the user


Create HTML template:
timers/
└── templates/
    └── timers/
        └── home.html

home.html file:
<!DOCTYPE html>
<html lang="pl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>TimeFlow</title>
</head>
<body>

    <header>
        <h1>TimeFlow</h1>
        <p>Zarządzaj swoim czasem świadomie.</p>
    </header>

    <main>
        <h2>Twoje aktywności</h2>

        <p>Nie masz jeszcze aktywnych timerów.</p>

        <button>+ Dodaj aktywność</button>
    </main>

</body>
</html>


Configurate website's address
create timers/urls.py file:
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
]

and in config/urls.py change it to:
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('timers.urls')),
]


Now the connection looks like that:
browser: http://127.0.0.1:8000/
config/urls.py: redirects request to timers app
timers/views.py - home() function
timers/templates/timers/home - out url site


Now django elements are connected:
config/urls.py — kieruje żądanie do aplikacji timers.
timers/urls.py — wskazuje odpowiedni widok.
timers/views.py — obsługuje żądanie i wybiera szablon.
home.html — odpowiada za zawartość strony.
"""

"""
### __3__ CHANGES TO WEBSITE
Added form to the home.html
<form>
    <label for="activity">Activity:</label><br>
    <input type="text" id="activity" name="activity" required>
    <label for="duration">Time:</label><br>
    <input type="number" id="duration" name="duration" min="1" required>
    <button type="submit">Add an activity</button><br>
</form>
"""

"""
### __4__ READ DATA FROM WEBSITE
timers/views.py change to:
from django.shortcuts import render

def home(request):
    activity = request.GET.get("activity")
    duration = request.GET.get("duration")

    context = {
        "activity": activity,
        "duration": duration,
    }

    return render(request, "timers/home.html", context)

request - request that django got from the browser
GET - data sent in the site's URL
.get("activity") — downloaded data with name "activity" 


timers/templates/timers/home.html:
{% if activity %}
    <h3>Your activity:</h3>
    <p>{{ activity }} — {{ duration }} minutes</p>
{% endif %}
Składnia szablonów Django, a nie zwykły HTML.
- {% if activity %} — sprawdza, czy przekazano aktywność.
- {{ activity }} — wyświetla wartość zmiennej.
- {{ duration }} — wyświetla czas trwania.
- {% endif %} — kończy warunek.
"""

"""
### __5__ CREATING MODEL
"""

"""
### SAVING ACTIVITY IN DATABASE
python manage.py makemigrations   -   prepares migration - instrukcję zmiany struktury bazy danych na podstawie modelu
python manage.py migrate  -   wykonuje przygotowane zmiany w bazie danych

models.py - describes data structure
makemigrations - django prepares instruction of changes
migrate - changes are made in SQLite



"""