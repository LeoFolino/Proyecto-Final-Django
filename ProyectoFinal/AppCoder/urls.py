from django.urls import path
from AppCoder.views import curso_view, inicio_view

urlpatterns = [
    path("inicio/", inicio_view),
    path("cursos/", curso_view)
]
