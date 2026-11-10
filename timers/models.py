from django.db import models

# creates model named "Activity" that represents single activity
"""
activities have 2 fieds: 
name - CharField - text with max length = 100
duration - PositiveIntegerField - positive number (int)
Django automativally adds id field
"""
class Activity(models.Model):
    name = models.CharField(max_length=100)
    duration = models.PositiveIntegerField()
