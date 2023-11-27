from django.shortcuts import render
from django.http import HttpResponse
from django.template import Template, Context
from datetime import datetime

def inicio_view(request):
    return HttpResponse ("Bienvenidos!!!!!!!!!!!!!!!")

def xx_curso_view(request):
   # return HttpResponse ("Aqui voy a mostrar mis cursos")
   return render(request, "AppCoder/padre.html")

def curso_view(request):
    nom = "Leonel"
    ap = "Folino"
    ahora = datetime.now()

    diccionario = {'nombre': nom, 'apellido': ap, 'nacionalidad' : 'argentino', "hora" : ahora, 'ciudades_preferidas' : ['Buenos Aires', 'Lima', 'San Pablo']}

    mi_archivo = open(r'C:\Users\Leito-PC\Documents\Django Projext\ProyectoFinal-2\AppCoder\templates\AppCoder\padre.html', "r")
    plantilla = Template(mi_archivo.read())
    Contexto = Context(diccionario)
    documento = plantilla.render(Contexto)

    return HttpResponse(documento)