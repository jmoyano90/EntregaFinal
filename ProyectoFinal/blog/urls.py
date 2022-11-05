from django.contrib import admin
from django.urls import path, include

from blog.views import (
    mostrar_inicio,
    procesar_fomulario_autor,
    procesar_fomulario_articulo,
    procesar_fomulario_seccion,
    buscar_articulo,
    buscar_autor,
    buscar_seccion,
    MyLogin,
    MyLogout,
    register,
)


urlpatterns = [
    path("inicio/", mostrar_inicio, name="Inicio"),
    path("formulario-autor/", procesar_fomulario_autor, name="Autor"),
    path("formulario-articulo/", procesar_fomulario_articulo, name="Articulo"),
    path("formulario-seccion/", procesar_fomulario_seccion, name="Seccion"),
    path("buscar-articulo/", buscar_articulo),
    path("buscar-autor/", buscar_autor),
    path("buscar-seccion/", buscar_seccion),
    path("login/", MyLogin.as_view(), name="Login"),
    path("logout/", MyLogout.as_view(), name="Logout"),
    path("register/", register, name="Register")
]
