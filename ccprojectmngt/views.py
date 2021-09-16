import pprint # Solo para test 

import zipfile
import base64
from io import BytesIO, StringIO


from django.shortcuts import get_object_or_404
from django.views.generic import TemplateView
from django.shortcuts import render, redirect
from django.http import HttpResponse

from xhtml2pdf import pisa

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
        check_id_list = list()
        pdf_list_buffer = list()

        # Se toman los id, proveniente
        # de los input que frueron marcados
        # con check y se almacenan en una lista.
        for key, value in request.POST.items():
            if key != 'csrfmiddlewaretoken':
                for pk in value:
                    check_id_list.append(pk)

        # Se hace un query y se toman
        # los registros, dependiendo
        # del id en check_id_list
        projects_selected = Project.objects.filter(pk__in=check_id_list)

        # Se genera la lista de HTML's
        html_generados = ad.generarHTML(projects_selected)

        try:
            # Se crea un Response Object del tipo zip
            
            # ver lista de content_type por documents
            # https://developer.mozilla.org/es/docs/Web/HTTP/Basics_of_HTTP/MIME_types/Common_types
            response = HttpResponse(content_type="application/zip")
            response['Content-Disposition'] = 'attachment; filename=test.zip'

            # Se crea un buffer para mantener el zip
            # en memoria.
            zip_buffer = BytesIO()

            # Se itera a travez de la lista
            # de html's generados.
            for html in html_generados:
                # Se crea un buffer para mantener los archivos
                # en memoria.
                buffer = BytesIO()

                # Se utiliza la libreria -> xhtml2pdf
                # para transformar un html --a--> pdf
                # https://xhtml2pdf.readthedocs.io/en/latest/
                pisa_status = pisa.CreatePDF(
                    html, dest=buffer
                )
                if pisa_status.err:
                    return HttpResponse("Error...")

                pdf_list_buffer.append(buffer)
            
            with zipfile.ZipFile(zip_buffer, "a", zipfile.ZIP_DEFLATED, False) as zip_file:
                for pdf_buffer in pdf_list_buffer:
                    zip_file.writestr("testy_ficher.pdf", pdf_buffer.getvalue())
            
            response.write(zip_buffer.getvalue())
            return response
        except Exception as e:
            print(e)
