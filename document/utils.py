from django.template.loader import get_template

class AcctionDocument:

    def generarHTML(projects_selected):
        list_document_html = list()
        # print(data.documento_solicitante, data.documento_representante)
        
        # Se recorre el queryset de los registros en `projects`
        # se crea un contexto por cada registro, y se genera 
        # un template que será almacenado en list_document_html
        for p in projects_selected:
            template = get_template('Plantilla Base/document.html')

            context = {
                'programa': p.programa,
                'solicitante': p.solicitante,
                'documento_solicitante': p.documento_solicitante,
                'representante': p.representante,
                'documento_representante': p.documento_representante,
                'correo_representante': p.correo_representante,
            }

            # context = {
            #     'project': p,
            # }
    
            document_html = template.render(context)
            list_document_html.append(document_html)
        
        return list_document_html
