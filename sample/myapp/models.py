from django.db import models 
from django.contrib import admin
class football(models.Model):
    name=models.CharField(max_length=30)
    jersey_no=models.IntegerField()
    age=models.IntegerField()
    country=models.CharField(max_length=20)
    weight=models.IntegerField()
class footballAdmin(admin.ModelAdmin):
    list_display=["name","jersey_no","age","country","weight"]