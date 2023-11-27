from django.shortcuts import render

from django.http import HttpResponse

def inicio_view(request):
    return HttpResponse ("Bienvenidos!!!!!!!!!!!!!!!")

def curso_view(request):
   # return HttpResponse ("Aqui voy a mostrar mis cursos")
   return render(request, "AppCoder/padre.html")