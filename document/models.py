from django.db import models

# Create your models here.


class Project(models.Model):
    
    fecha_documento = models.CharField(max_length=50, null=True, blank=True)
    programa =  models.CharField(max_length=50, null=True, blank=True)
    n_sorte =  models.CharField(max_length=50, null=True, blank=True)
    consultora =  models.CharField(max_length=50, null=True, blank=True)
    id_solicitud =  models.CharField(max_length=50, null=True, blank=True)
    documento_solicitante =  models.CharField(max_length=50, null=True, blank=True)
    nombre_solicitante =  models.CharField(max_length=50, null=True, blank=True)
    provincia =  models.CharField(max_length=50, null=True, blank=True)
    poblacion =  models.CharField(max_length=50, null=True, blank=True)
    cp =  models.CharField(max_length=50, null=True, blank=True)
    email =  models.CharField(max_length=50, null=True, blank=True)
    direccion =  models.CharField(max_length=50, null=True, blank=True)
    telefono_solicitante =  models.CharField(max_length=50, null=True, blank=True)
    documento_representante =  models.CharField(max_length=50, null=True, blank=True)
    nombre_representante =  models.CharField(max_length=50, null=True, blank=True)
    cargo =  models.CharField(max_length=50, null=True, blank=True)
    email_representante =  models.CharField(max_length=50, null=True, blank=True)
    anno_actividad =  models.CharField(max_length=50, null=True, blank=True)
    nuevo =  models.CharField(max_length=50, null=True, blank=True)
    iae =  models.CharField(max_length=50, null=True, blank=True)
    ss_ok =  models.CharField(max_length=50, null=True, blank=True)
    aeat_ok =  models.CharField(max_length=50, null=True, blank=True)
    cif_ok =  models.CharField(max_length=50, null=True, blank=True)
    dni_ok =  models.CharField(max_length=50, null=True, blank=True)
    escrituras_ok =  models.CharField(max_length=50, null=True, blank=True)
    dec_responsable_ok =  models.CharField(max_length=50, null=True, blank=True)
    fases = models.CharField(max_length=50, null=True, blank=True)
    acta = models.CharField(max_length=50, null=True, blank=True)
    r_admision = models.CharField(max_length=50, null=True, blank=True)
    notificado = models.CharField(max_length=50, null=True, blank=True)
    tratamiento_tecnico = models.CharField(max_length=50, null=True, blank=True)
    tecnico = models.CharField(max_length=50, null=True, blank=True)
    dni = models.CharField(max_length=50, null=True, blank=True)
    tratamiento_representante = models.CharField(max_length=50, null=True, blank=True)
    fecha_doc = models.CharField(max_length=50, null=True, blank=True)
    fecha_diagnostico = models.CharField(max_length=50, null=True, blank=True)
    fecha_recepcion_presupuesto = models.CharField(max_length=50, null=True, blank=True)
    fecha_envio_anexo_19 = models.CharField(max_length=50, null=True, blank=True)
    envio_ppi = models.CharField(max_length=50, null=True, blank=True)
    duracion_del_plan = models.CharField(max_length=50, null=True, blank=True)
    segui_1 = models.CharField(max_length=50, null=True, blank=True)
    segui_2 = models.CharField(max_length=50, null=True, blank=True)
    segui_3 = models.CharField(max_length=50, null=True, blank=True)
    segui_4 = models.CharField(max_length=50, null=True, blank=True)
    fecha_memoria_final = models.CharField(max_length=50, null=True, blank=True)
    encuesta_satisfaccion = models.CharField(max_length=50, null=True, blank=True)
    num_expediente = models.CharField(max_length=50, null=True, blank=True)
    proyectos = models.CharField(max_length=50, null=True, blank=True)
    justificacion = models.CharField(max_length=50, null=True, blank=True)
    descripcion_empresa = models.CharField(max_length=50, null=True, blank=True)
    pagina_web = models.CharField(max_length=50, null=True, blank=True)    
    solicitud_cumplimentada_ok = models.CharField(max_length=50, null=True, blank=True)    
    domicilio_en_demarcacion_ok = models.CharField(max_length=50, null=True, blank=True)    
    condiciones_participacion = models.CharField(max_length=50, null=True, blank=True)    
    fecha_informe_valoracion = models.CharField(max_length=50, null=True, blank=True)    
    fecha_resolucion = models.CharField(max_length=50, null=True, blank=True)    
    informacion_adicional_beneficiario_anexo_16 = models.CharField(max_length=50, null=True, blank=True)    
    fecha_convenido_deca_anexo_10 = models.CharField(max_length=50, null=True, blank=True)    
    fecha_registro_participacion_fase_i_anexo_18 = models.CharField(max_length=50, null=True, blank=True)  
    enviado_email_publicidad_ue = models.CharField(max_length=50, null=True, blank=True)    
    fecha_registro_participacion_en_fase_ii_anexo_19 = models.CharField(max_length=50, null=True, blank=True)    
    fecha_registro_servicio_seguimiento_fase_ii_anexo_20 = models.CharField(max_length=50, null=True, blank=True)    
    memoria_proyecto_y_cuestionario = models.CharField(max_length=50, null=True, blank=True)   
    formulario_ccc_empresas = models.CharField(max_length=50, null=True, blank=True)    
    facturas = models.CharField(max_length=50, null=True, blank=True)    
    orden_de_transferencia = models.CharField(max_length=50, null=True, blank=True)    
    extracto_bancario = models.CharField(max_length=50, null=True, blank=True)    
    evidencias_del_gasto = models.CharField(max_length=50, null=True, blank=True) 
    obligaciones_publicidad_ue = models.CharField(max_length=50, null=True, blank=True)    


    """ programa = models.CharField(max_length=40)
    solicitante = models.CharField(max_length=100)
    documento_solicitante = models.CharField(max_length=15)
    representante = models.CharField(max_length=100)
    documento_representante = models.CharField(max_length=15)
    correo_representante = models.CharField(max_length=10) """

    #esto aprece en la parte de administracion para que en lugar de project aparezca proyectos
    class Meta:
        verbose_name = "Proyecto"
        verbose_name_plural = "Proyectos"

    # este soliciting aparece en la parte de administracion como solicitante
    def __str__(self):
        return self.nombre_solicitante

""" 
fecha_documento = models.CharField(max_length=50)
programa =  models.CharField(max_length=50)
n_sorte =  models.CharField(max_length=50)
consultora =  models.CharField(max_length=50)
id_solicitud =  models.CharField(max_length=50)
documento_soclitiante =  models.CharField(max_length=50)
nombre_solicitante =  models.CharField(max_length=50)
provincia =  models.CharField(max_length=50)
poblacion =  models.CharField(max_length=50)
cp =  models.CharField(max_length=50)
email =  models.CharField(max_length=50)
direccion =  models.CharField(max_length=50)
telefono_solicitante =  models.CharField(max_length=50)
docoumento_representante =  models.CharField(max_length=50)
cargo =  models.CharField(max_length=50)
email_representante =  models.CharField(max_length=50)
anno_actividad =  models.CharField(max_length=50)
nuevo =  models.CharField(max_length=50)
iae =  models.CharField(max_length=50)
ss =  models.CharField(max_length=50)
aeat =  models.CharField(max_length=50)
cif =  models.CharField(max_length=50)
dni =  models.CharField(max_length=50)
escrituras =  models.CharField(max_length=50)
dec_responsable =  models.CharField(max_length=50)
fases = models.CharField(max_length=50)
acta = models.CharField(max_length=50)
r_admision = models.CharField(max_length=50)
notificado = models.CharField(max_length=50)
tratamiento_tecnico = models.CharField(max_length=50)
tecnico = models.CharField(max_length=50)
dni = models.CharField(max_length=50)
tratamiento_representante = models.CharField(max_length=50)
fecha_doc = models.CharField(max_length=50)
fecha_diagnostico = models.CharField(max_length=50)
fecha_recepcion_presupuesto = models.CharField(max_length=50)
fecha_envio_anexo_19 = models.CharField(max_length=50)
envio_ppi = models.CharField(max_length=50)
duracion_del_plan = models.CharField(max_length=50)
segui_1 = models.CharField(max_length=50)
segui_2 = models.CharField(max_length=50)
segui_3 = models.CharField(max_length=50)
segui_4 = models.CharField(max_length=50)
fecha_memoria_final = models.CharField(max_length=50)
encuesta_satisfaccion = models.CharField(max_length=50)
num_expediente = models.CharField(max_length=50)
proyectos = models.CharField(max_length=50)
justificacion = models.CharField(max_length=50)
descripcion_empresa = models.CharField(max_length=50)
pagina_web = models.CharField(max_length=50) """

""" 

Fecha documento
programa	
NºSORTEO	
Consultora	
Id. solicitud	
Documento solicitante	
Nombre Solicitante	
Provincia	
Población	
CP	
Email	
Dirección	
Teléfono solicitante	
Documento representante	
Nombre representante	
CARGO	
Email representante	
AÑO ACTIVIDAD	
Nuevo	
IAE	
SS	
AEAT	
CIF	
DNI	
ESCRITURAS	
DEC RESPONSABLE	
FASES	
ACTA	
R-ADMISION	
NOTIFICADO 	
TRATAMIENTO TECNICO	
TECNICO	
DNI	
TRATAMIENTO REPRESENTANTE
Fecha doc	
Envio Diagnostico	
Fecha Recepción presupuestos
Fecha envío Anexo 19
Envío PPI
DURACION DEL PLAN ( DATO PARA EL ANEXO 21)	
segui 1	
segui 2	
segui 3	
segui 4	
fecha memoria final	
Encuenta satisfacción	
EXPEDIENTE	
PROYECTOS	
JUSTIFICACION	
Descripcion de la empresa 	
Pagina web
 """



