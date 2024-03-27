from django.contrib import admin

# Register your models here.
from datacollection.models import studentdetail,attendance
class saveadmin(admin.ModelAdmin):
    list_display=("name","email","course","joiningdate","duration","rollno")
admin.site.register(studentdetail,saveadmin)
class saveadmin1(admin.ModelAdmin):
    list_display=("date","topic","intime","outtime","feedback")
admin.site.register(attendance,saveadmin1)