import pprint # Solo para test 

import zipfile
from io import BytesIO

from django.shortcuts import get_object_or_404
from django.views.generic import TemplateView
from django.shortcuts import render, redirect
from django.http import HttpResponse

# from django_filters.views import FilterView
# from document.filter import ProjectFilter

from document.models import Project
from document.utils import AcctionDocument as ad



class HomeView(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        #project_seleted = None
        # try:
        #     for idstr in context['cadenaid'].split('-'):
        #         id = int(idstr)
        #         project_seleted = get_object_or_404(Project, id=id)
        #         # esto imprime los valroes al terminal para verlo internamente los datos del modelo
        #         #print(project_seleted.documento_solicitante, project_seleted.documento_representante
        #         ad.generarHTML(project_seleted)
        # except: pass

        context['projects'] = Project.objects.all()
        # print(context)
        # return render(TemplateView, 'index.html', context) esto no funciona , tengo que usar solo return context
        return context


    def post(self, request, *args, **kwargs):
        # TODO imprime el objeto QueryDict, especificamente
        # https://docs.djangoproject.com/en/3.2/ref/request-response/#querydict-objects
        # el method `POST` por consola
        # print(request.POST)

        #TODO Tomar un valor en especifico del QueryDict.
        # print(request.POST['check1'])
        # output -> 

        #TODO Otra forma de tomar un valor en especifico del QueryDict.
        # print(request.POST.get('check1'))
        # output -> 1

        #TODO Trae la `lista` completa de valores de un valor en especifico del QueryDict.
        # print(request.POST.getlist('check1'))
        # output -> ['1']

        check_id_list = list()
        text_file_dict = dict()

        # # Se toman los id, proveniente
        # # de los inputs que fueron marcados
        # # con check y se almacenan en una lista.
        for key, value in request.POST.items():  # request.POST.items() => [(key, value), (key, value)....(keyN, ValueN)]
            if key != 'csrfmiddlewaretoken':
                check_id_list.append(value)
        
        # TODO test: verificar contenido de check_id_list por consola
        # print(check_id_list)
        # output e.g -> ['1', '2',....,[n]]

        # # Se hace un query y se toman
        # # los registros, dependiendo
        # # del id en check_id_list
        projects_selected = Project.objects.filter(pk__in=check_id_list)
        
        # TODO test: verificar contenido de projects_selected por consola
        # print(projects_selected)
        # output e.g -> <QuerySet [<Objeto Model 1>, <Objeto Model 2>,.....<Objeto Model N>]

        # # Se genera la lista de HTML's
        html_generados = ad.generarHTML(projects_selected)

        try:
            # Se crea un Response Object del tipo zip
            
            # ver lista de content_type(MIME's) por documents
            # https://developer.mozilla.org/es/docs/Web/HTTP/Basics_of_HTTP/MIME_types/Common_types
            response = HttpResponse(content_type="application/zip")
            response['Content-Disposition'] = 'attachment; filename=test.zip'

            # Se crea un buffer para mantener el zip
            # en memoria.
            zip_buffer = BytesIO()

            # Se itera a travez de la lista
            # de html's generados y crear un documento
            # con extension .txt que contendrá el codigo HTML.
            for solicitante, html_code in html_generados.items():
                # Se crea un buffer para mantener los archivos
                # en memoria.
                buffer = BytesIO()

                # El codigo HTML, viene como objeto SafeString.
                # el metodo encode('UTF-8') permitirá darle el formato
                # adecuado para poder ser volcado en el buffer.
                buffer.write(html_code.encode('UTF-8')) 
                buffer.seek(0)

                text_file_dict[solicitante] = buffer
            
            # Se crea un documento Zip, apartir de la libreria de Python zipfile.
            with zipfile.ZipFile(zip_buffer, "a", zipfile.ZIP_DEFLATED, False) as zip_file:

                # Se recorre el diccionario de documentos .txt, generados anteriormente
                # Se toma el nombre del solicitante, para construir el nombre del documento,
                # y se ingresa el documento dentro del Zip.
                for solicitante, txt_file_buffer in text_file_dict.items():
                    file_name = "{}.txt".format(solicitante)
                    zip_file.writestr(file_name, txt_file_buffer.getvalue())
            
            response.write(zip_buffer.getvalue())
            return response
        except Exception as e:
            print(e)