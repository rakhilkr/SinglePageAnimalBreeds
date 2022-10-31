from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import *
# Register your models here.

class selectionModelAdmin(ImportExportModelAdmin):
    list_display=['id','animal','breed']

class ResultsModel_Admin(ImportExportModelAdmin):
    list_display=['id','animal','breed']
admin.site.register(selectionModel,selectionModelAdmin)
admin.site.register(ResultsModel,ResultsModel_Admin)
