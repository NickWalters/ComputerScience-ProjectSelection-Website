from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import *

# Register your models here.
#admin.site.register(ProjectModel)

@admin.register(ProjectModel)
class ViewAdmin(ImportExportModelAdmin):
    pass