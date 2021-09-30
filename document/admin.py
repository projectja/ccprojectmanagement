from django.contrib import admin

# Se importa fields & windets, para
# dar establecer a que campo del modelo
# se le dará formato.
from import_export import resources, fields, widgets
from import_export.admin import ImportExportModelAdmin

from .models import Project


class ProjectResource(resources.ModelResource):
   # attribute -> el campo dentro del model.
   # column_name -> la columna dentro del formato (.xls o .xlxs)
   # widget -> representa el objeto que dará formato al campo dentro del model.
   # https://django-import-export.readthedocs.io/en/latest/api_fields.html#fields -> SOBRE  Field
   # https://django-import-export.readthedocs.io/en/latest/api_widgets.html#import_export.widgets.DateWidget -> SOBRE Widgets

   # TODO aqui la sintaxis para dar formato a un campo.
   # fecha_diagnostico = fields.Field(attribute="fecha_diagnostico", column_name="fecha_diagnostico", widget=widgets.DateWidget('%d/%m/%Y'))


   class Meta:
      model = Project
      fields = ['id','fecha_documento', 'programa',  'n_sorte',  'consultora', 'id_solicitud', 'documento_solicitante','nombre_solicitante', 'provincia', 'poblacion','cp','email','direccion', 'telefono_solicitante', 'documento_representante','nombre_representante',
      'cargo', 'email_representante',  'anno_actividad', 'nuevo', 'iae', 'ss_ok', 'aeat_ok', 'cif_ok',  'dni_ok', 'escrituras_ok', 'dec_responsable_ok', 'fases', 'acta', 'r_admision', 'notificado', 'tratamiento_tecnico', 'tecnico',
      'dni', 'tratamiento_representante', 'fecha_doc', 'fecha_diagnostico', 'fecha_recepcion_presupuesto', 'fecha_envio_anexo_19', 'envio_ppi', 'duracion_del_plan', 'segui_1', 'segui_2', 'segui_3',
      'segui_4', 'fecha_memoria_final',  'encuesta_satisfaccion', 'num_expediente', 'proyectos', 'justificacion', 'descripcion_empresa', 'pagina_web',
      'solicitud_cumplimentada_ok','domicilio_en_demarcacion_ok','condiciones_participacion','fecha_informe_valoracion','fecha_resolucion','informacion_adicional_beneficiario_anexo_16','fecha_convenido_deca_anexo_10',
      'fecha_registro_participacion_fase_i_anexo_18','enviado_email_publicidad_ue','fecha_registro_participacion_en_fase_ii_anexo_19','fecha_registro_servicio_seguimiento_fase_ii_anexo_20','memoria_proyecto_y_cuestionario',
      'formulario_ccc_empresas','facturas','orden_de_transferencia','extracto_bancario','evidencias_del_gasto','obligaciones_publicidad_ue']

      
class ProjectAdmin(ImportExportModelAdmin):
   resource_class = ProjectResource
   list_display =  ['id','fecha_documento', 'programa',  'n_sorte',  'consultora', 'id_solicitud', 'documento_solicitante','nombre_solicitante', 'provincia', 'poblacion','cp','email','direccion', 'telefono_solicitante', 'documento_representante', 'nombre_representante',
   'cargo', 'email_representante',  'anno_actividad', 'nuevo', 'iae', 'ss_ok', 'aeat_ok', 'cif_ok',  'dni_ok', 'escrituras_ok', 'dec_responsable_ok', 'fases', 'acta', 'r_admision', 'notificado', 'tratamiento_tecnico', 'tecnico',
   'dni', 'tratamiento_representante', 'fecha_doc', 'fecha_diagnostico', 'fecha_recepcion_presupuesto', 'fecha_envio_anexo_19', 'envio_ppi', 'duracion_del_plan', 'segui_1', 'segui_2', 'segui_3',
   'segui_4', 'fecha_memoria_final',  'encuesta_satisfaccion', 'num_expediente', 'proyectos', 'justificacion', 'descripcion_empresa', 'pagina_web',
   'solicitud_cumplimentada_ok','domicilio_en_demarcacion_ok','condiciones_participacion','fecha_informe_valoracion','fecha_resolucion','informacion_adicional_beneficiario_anexo_16','fecha_convenido_deca_anexo_10',
   'fecha_registro_participacion_fase_i_anexo_18','enviado_email_publicidad_ue','fecha_registro_participacion_en_fase_ii_anexo_19','fecha_registro_servicio_seguimiento_fase_ii_anexo_20','memoria_proyecto_y_cuestionario',
   'formulario_ccc_empresas','facturas','orden_de_transferencia','extracto_bancario','evidencias_del_gasto','obligaciones_publicidad_ue']
  



admin.site.register(Project, ProjectAdmin)

