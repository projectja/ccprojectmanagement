from django.shortcuts import get_object_or_404
from django.views.generic import TemplateView
from django.shortcuts import render, redirect

from document.models import Project
from document.utils import AcctionDocument as ad

class HomeView(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        #project_seleted = None
        try:
            for idstr in context['cadenaid'].split('-'):
                id = int(idstr)
                project_seleted = get_object_or_404(Project, id=id)
                # esto imprime los valroes al terminal para verlo internamente los datos del modelo
                #print(project_seleted.documento_solicitante, project_seleted.documento_representante
                ad.generarHTML(project_seleted)
        except: pass

        context['projects'] = Project.objects.all()
        print(context)
        # return render(TemplateView, 'index.html', context) esto no funciona , tengo que usar solo return context
        return context

