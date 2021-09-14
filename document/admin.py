from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin

from .models import Project


class ProjectResource(resources.ModelResource):
   class Meta:
      model = Project
      fields = ['id', 'programa', 'solicitante', 'documento_solicitante', 'representante', 'documento_representante', 'correo_representante']


class ProjectAdmin(ImportExportModelAdmin):
   resource_class = ProjectResource
   list_display = ['id', 'programa', 'solicitante', 'documento_solicitante', 'representante', 'documento_representante', 'correo_representante']


admin.site.register(Project, ProjectAdmin)
