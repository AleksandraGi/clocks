"""
Do requests and chooses a template
Przygotowuje dane które są w szablonie
"""

from django.shortcuts import render

def home(request):
    activity = request.GET.get("activity")
    duration = request.GET.get("duration")

    context = {
        "activity": activity,
        "duration": duration
    }

    return render(request, 'timers/home.html', context)