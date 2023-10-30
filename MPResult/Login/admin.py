from django.contrib import admin
from .models import ResultDatabase
# Register your models here.


class AdminData(admin.ModelAdmin):
    list_display=('Enrollment','RegularPrivate','Application','RollNo','StudentName','FatherName','MotherName','BirthDate','Hindi','English','Maths','Science','SocialScience','Sanskrite')

admin.site.register(ResultDatabase,AdminData)