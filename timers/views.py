"""
Do requests and chooses a template
"""

from django.shortcuts import render

def home(request):
    return render(request, 'timers/home.html')