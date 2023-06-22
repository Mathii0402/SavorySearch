from django.contrib import admin

# Register your models here.
from .models import hotel
from import_export.admin import ImportExportModelAdmin 
 
admin.site.register(hotel, ImportExportModelAdmin)
class searchData(ImportExportModelAdmin):
    pass