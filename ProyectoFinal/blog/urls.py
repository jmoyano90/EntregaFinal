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
    SeccionList,
    SeccionDetalle,
    SeccionCreacion,
    SecccionUpdateView,
    SeccionDelete,
)


urlpatterns = [
    path("inicio/", mostrar_inicio, name="Inicio"),
    #FORMULARIOS
    path("formulario-autor/", procesar_fomulario_autor, name="Autor"), 
    path("formulario-articulo/", procesar_fomulario_articulo, name="Articulo"),
    path("formulario-seccion/", procesar_fomulario_seccion, name="Seccion"),
    #BUSCADOR
    path("buscar-articulo/", buscar_articulo),
    path("buscar-autor/", buscar_autor),
    path("buscar-seccion/", buscar_seccion),
    #LOGIN
    path("login/", MyLogin.as_view(), name="Login"),
    path("logout/", MyLogout.as_view(), name="Logout"),
    path("register/", register, name="Register"),
    #SECCION
    path("seccion/list", SeccionList.as_view(), name="SeccionList"),
    path("r'(?P<pk>\d+)^$'", SeccionDetalle.as_view(), name="SeccionDetail"),
    path("seccion-nuevo/", SeccionCreacion.as_view(), name="SeccionNew"),
    path("r'editar/(?P<pk>\d+)^$'", SecccionUpdateView.as_view(), name="SeccionUpdate"),
    path("r'borrar/(?P<pk>\d+)^$'", SeccionDelete.as_view(), name="SeccionDelete"),
    
    ]
