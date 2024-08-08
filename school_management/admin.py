from django.contrib import admin
from .models import School,Section,Events,Academics,HomeWork,Notice,Student,Teacher,Settings
# Register your models here.
admin.site.register([Student,School,Section,Events,Academics,HomeWork,Notice,Teacher,Settings])