from django.template.loader import render_to_string

class AcctionDocument:

    def generarHTML(projects_selected):
        # Devuelve un diccionario con
        # el nombre del solicitante como key
        # y un SafeString del codigo HTML del template
        # como value.
        
        dict_doc_html = dict()
        
        # Se recorre el queryset de los registros en `projects`
        # se crea un contexto por cada registro, y se genera 
        # un template que será almacenado en dict_doc_html
        for p in projects_selected:
            context = {
                'project': p,
            }
            # Se utiliza render_to_string para tomar el codigo html
            # y convertirlo en un objeto SafeString
            document_html = render_to_string('Plantilla Base/document.html', context)
            dict_doc_html[p.nombre_solicitante] = document_html

        return dict_doc_html