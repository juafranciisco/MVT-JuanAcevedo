
from unittest import loader
from django.shortcuts import render
from django.http import HttpResponse
from django.template import Template, Context, loader
from Familiares.models import familiar

def probar_template(request):
    queryset = familiar.objects.all()
    diccionario = {'Familiares':queryset}
    template = loader.get_template('plantilla1.html')
    documento_html = template.render(diccionario)

    return HttpResponse(documento_html)



# Create your views here.
