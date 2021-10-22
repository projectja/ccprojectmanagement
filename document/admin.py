from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin

from .models import Project


class ProjectResource(resources.ModelResource):
   class Meta:
      model = Project
      fields = ['id','fecha_documento_inicio_diagnostico', 'programa', 
      'n_sorte',  'consultora', 'id_solicitud', 'num_registro','fecha_y_hora_registro',
      'fecha_y_hora_solicitud',
      'documento_solicitante','nombre_solicitante', 'provincia', 'poblacion','cp','email','direccion', 
      'telefono_solicitante', 'documento_representante','nombre_representante',
      'cargo', 'email_representante',  'anno_actividad', 'nuevo', 'iae', 'ss_ok', 'aeat_ok', 'cif_ok',  'dni_ok', 'escrituras_ok', 'dec_responsable_ok', 'fases', 'acta', 'r_admision', 'notificado', 'tratamiento_tecnico', 'tecnico_justificar', 'tecnico_diagnostico',
      'dni_tecnico', 'tratamiento_representante',  'fecha_diagnostico', 'fecha_recepcion_presupuesto', 'fecha_envio_anexo_19', 'envio_ppi', 'duracion_del_plan', 'segui_1', 'segui_2', 'segui_3',
      'segui_4','segui_5', 'encuesta_satisfaccion', 'num_expediente', 'proyectos', 'justificacion_diagnostico', 'descripcion_empresa', 'pagina_web',
      'solicitud_cumplimentada_ok','domicilio_en_demarcacion_ok','condiciones_participacion','fecha_informe_valoracion','fecha_resolucion','informacion_adicional_beneficiario_anexo_16','fecha_convenido_deca_anexo_10','deca_firmado_ok',
      'fecha_registro_participacion_fase_i_anexo_18','anexo_18_firmado','enviado_email_publicidad_ue','fecha_registro_participacion_en_fase_ii_anexo_19','fecha_registro_servicio_seguimiento_fase_ii_anexo_20','memoria_proyecto_y_cuestionario_anexo_21',
      'formulario_ccc_empresas_anexo_27','facturas','orden_de_transferencia','extracto_bancario','evidencias_del_gasto','obligaciones_publicidad_ue','bitacora','fecha_inicio_fase_ii']

      
class ProjectAdmin(ImportExportModelAdmin):
   resource_class = ProjectResource
   list_display =  ['id','fecha_documento_inicio_diagnostico', 'programa', 
   'n_sorte', 'consultora', 'id_solicitud', 'num_registro','fecha_y_hora_registro',
   'fecha_y_hora_solicitud','documento_solicitante','nombre_solicitante', 'provincia', 'poblacion','cp','email','direccion', 'telefono_solicitante', 'documento_representante', 'nombre_representante',
   'cargo', 'email_representante',  'anno_actividad', 'nuevo', 'iae', 'ss_ok', 'aeat_ok', 'cif_ok',  'dni_ok', 'escrituras_ok', 'dec_responsable_ok', 'fases', 'acta', 'r_admision', 'notificado', 'tratamiento_tecnico', 'tecnico_justificar','tecnico_diagnostico',
   'dni_tecnico', 'tratamiento_representante',  'fecha_diagnostico', 'fecha_recepcion_presupuesto', 'fecha_envio_anexo_19', 'envio_ppi', 'duracion_del_plan', 'segui_1', 'segui_2', 'segui_3',
   'segui_4', 'segui_5', 'encuesta_satisfaccion', 'num_expediente', 'proyectos', 'justificacion_diagnostico', 'descripcion_empresa', 'pagina_web',
   'solicitud_cumplimentada_ok','domicilio_en_demarcacion_ok','condiciones_participacion','fecha_informe_valoracion','fecha_resolucion','informacion_adicional_beneficiario_anexo_16','fecha_convenido_deca_anexo_10','deca_firmado_ok',
   'fecha_registro_participacion_fase_i_anexo_18','anexo_18_firmado','enviado_email_publicidad_ue','fecha_registro_participacion_en_fase_ii_anexo_19','fecha_registro_servicio_seguimiento_fase_ii_anexo_20','memoria_proyecto_y_cuestionario_anexo_21',
   'formulario_ccc_empresas_anexo_27','facturas','orden_de_transferencia','extracto_bancario','evidencias_del_gasto','obligaciones_publicidad_ue','fecha_inicio_fase_ii']
  



admin.site.register(Project, ProjectAdmin)

