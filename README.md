# Ex02 Django ORM Web Application
## Date: 18/10/2023

## AIM
To develop a Django application to store and retrieve data from a Football Players database using Object Relational Mapping(ORM).

## DESIGN STEPS

### STEP 1:
Clone the problem from GitHub

### STEP 2:
Create a new app in Django project

### STEP 3:
Enter the code for admin.py and models.py

### STEP 4:
Execute Django admin and create 10 Football players

## PROGRAM

```
admin.py 
from django.contrib import admin
from.models import football,footballAdmin
admin.site.register(football,footballAdmin)

models.py
from django.db import models
from django.contrib import admin
class football_player(models.Model)
player_name=models.CharField(max_length=20);
jersey_no=models.IntegerField()
age=models.IntergerField()
height=models.IntergerField()
weight=models.IntergerField()
goals_scored=models.IntergerField()
country=models.CharFields(max_length=20)
class football_playerAdmin(admin.ModelAdmin):
     list_display=["player_name","jersey_no","age","height","weight","goals_scored","country"]

```

## OUTPUT
![Alt text](<Screenshot 2023-10-13 215053-1.png>)

## RESULT
Thus the program for creating a database using ORM hass been executed successfully
