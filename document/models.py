from django.db import models

# Create your models here.

class Project(models.Model):
    
    
    programa =  models.CharField(max_length=50)
    n_sorte =  models.CharField(max_length=50)
    consultora =  models.CharField(max_length=50)
    id_solicitud =  models.CharField(max_length=50)
    num_registro =  models.CharField(max_length=50)
    fecha_y_hora_registro =  models.CharField(max_length=50)
    fecha_y_hora_solicitud =  models.CharField(max_length=50)
    documento_solicitante =  models.CharField(max_length=50)
    nombre_solicitante =  models.CharField(max_length=50)
    provincia =  models.CharField(max_length=50)
    poblacion =  models.CharField(max_length=50)
    cp =  models.CharField(max_length=50)
    email =  models.CharField(max_length=50)
    direccion =  models.CharField(max_length=50)
    telefono_solicitante =  models.CharField(max_length=50)
    documento_representante =  models.CharField(max_length=50)
    nombre_representante =  models.CharField(max_length=50)
    cargo =  models.CharField(max_length=50)
    email_representante =  models.CharField(max_length=50)
    anno_actividad =  models.CharField(max_length=50)
    nuevo =  models.CharField(max_length=50)
    iae =  models.CharField(max_length=50)
    ss_ok =  models.CharField(max_length=50)
    aeat_ok =  models.CharField(max_length=50)
    cif_ok =  models.CharField(max_length=50)
    dni_ok =  models.CharField(max_length=50)
    escrituras_ok =  models.CharField(max_length=50)
    dec_responsable_ok =  models.CharField(max_length=50)
    fases = models.CharField(max_length=50)
    acta = models.CharField(max_length=50)
    r_admision = models.CharField(max_length=50)
    notificado = models.CharField(max_length=50)
    tratamiento_tecnico = models.CharField(max_length=50)
    
    dni_tecnico = models.CharField(max_length=50)
    
    tratamiento_representante = models.CharField(max_length=50)
    deca_firmado_ok = models.CharField(max_length=50)
    bitacora = models.CharField(max_length=50)  
    fecha_documento_inicio_diagnostico = models.CharField(max_length=50)    
    fecha_diagnostico = models.CharField(max_length=50)
    anexo_18_firmado = models.CharField(max_length=50)    
    fecha_recepcion_presupuesto = models.CharField(max_length=50)
    fecha_envio_anexo_19 = models.CharField(max_length=50)    
    envio_ppi = models.CharField(max_length=50)
    duracion_del_plan = models.CharField(max_length=50)
    encuesta_satisfaccion = models.CharField(max_length=50)                    # sobra repetido
    proyectos = models.CharField(max_length=50)
    descripcion_empresa = models.CharField(max_length=50)   # no usado ?
    pagina_web = models.CharField(max_length=50)            # no usado ?
    solicitud_cumplimentada_ok = models.CharField(max_length=50)    
    domicilio_en_demarcacion_ok = models.CharField(max_length=50)    
    condiciones_participacion = models.CharField(max_length=50)    
    informacion_adicional_beneficiario_anexo_16 = models.CharField(max_length=50)        
    # duplicado fecha_convenido_deca_anexo_10 = models.CharField(max_length=50)    
    fecha_registro_participacion_fase_i_anexo_18 = models.CharField(max_length=50)    
    enviado_email_publicidad_ue = models.CharField(max_length=50)    
    fecha_registro_participacion_en_fase_ii_anexo_19 = models.CharField(max_length=50)    
    fecha_registro_servicio_seguimiento_fase_ii_anexo_20 = models.CharField(max_length=50)    
    memoria_proyecto_y_cuestionario_anexo_21 = models.CharField(max_length=50)   
    formulario_ccc_empresas_anexo_27 = models.CharField(max_length=50)    
    facturas = models.CharField(max_length=50)    
    orden_de_transferencia = models.CharField(max_length=50)    
    extracto_bancario = models.CharField(max_length=50)    
    evidencias_del_gasto = models.CharField(max_length=50) 
    obligaciones_publicidad_ue = models.CharField(max_length=50)   
    tecnico_diagnostico = models.CharField(max_length=50)
    importe_presupuestado = models.CharField(max_length=50)
    importe_subvencionado =  models.CharField(max_length=50)
    contador_secuencial_expendiente = models.CharField(max_length=50)
    #  crear importes prespuesado
    #  crear campo importe maximo
    # aqui viene un campo N en el excel que no se utiliza en la bbdd

    num_expediente = models.CharField(max_length=50)
    empresa_innocamara = models.CharField(max_length=50)
    estado = models.CharField(max_length=50)
    entrevista  = models.CharField(max_length=50)

    # en excel campo que no se utiliza en la bbdd : EMPRESA INNOCAMARAS(30/30)	
    # en excel campo que no se utiliza en la bbdd ESTADO	
    # campo en excel que no se utiliza en la bbdd seria bueno crearlo = fecha de ENTREVISTA?
    fecha_informe_valoracion = models.CharField(max_length=50)
    fecha_resolucion  = models.CharField(max_length=50)
    fecha_convenido_deca_anexo_10 = models.CharField(max_length=50)    
    tecnico_justificar = models.CharField(max_length=50)
    fecha_fin_fase_i = models.CharField(max_length=50)
    nivel_madurez = models.CharField(max_length=50)
    justificacion_diagnostico = models.CharField(max_length=50)    
    fecha_inicio_fase_ii = models.CharField(max_length=50)    
    segui_1 = models.CharField(max_length=50)
    segui_2 = models.CharField(max_length=50)
    segui_3 = models.CharField(max_length=50)
    segui_4 = models.CharField(max_length=50)
    segui_5 = models.CharField(max_length=50)
    

    # posibilidad de crear aqui fecha fin fase II
  
 
#fecha_memoria_final = models.CharField(max_length=50)
    
    
    
    
    
    
    
    


    
    

    #esto aprece en la parte de administracion para que en lugar de project aparezca proyectos
    class Meta:
        verbose_name = "Proyecto"
        verbose_name_plural = "Proyectos"

    # este soliciting aparece en la parte de administracion como solicitante
    def __str__(self):
        return self.nombre_solicitante