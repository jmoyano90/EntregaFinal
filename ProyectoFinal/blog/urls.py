from django.contrib import admin
from django.urls import path, include

from blog.views import (
    mostrar_inicio,
    buscar,
    procesar_fomulario_autor,
    procesar_fomulario_articulo,
    procesar_fomulario_seccion,
)


urlpatterns = [
    path("inicio/", mostrar_inicio),
    path("formulario-autor/", procesar_fomulario_autor),
    path("formulario-articulo/", procesar_fomulario_articulo),
    path("formulario-seccion/", procesar_fomulario_seccion),
    path("buscar-articulo/", buscar),
]
