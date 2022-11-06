from django.contrib import admin
from django.urls import path, include

from blog.views import (
    mostrar_inicio,
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
    ArticuloList,
    ArticuloDetalle,
    ArticuloCreacion,
    ArticuloUpdateView,
    ArticuloDelete,
)


urlpatterns = [
    path("inicio/", mostrar_inicio, name="Inicio"),
    #BUSCADOR
    path("buscar-articulo/", buscar_articulo, name="Articulo"),
    path("buscar-autor/", buscar_autor, name="Autor"),
    path("buscar-seccion/", buscar_seccion, name="Seccion"),
    #LOGIN
    path("login/", MyLogin.as_view(), name="Login"),
    path("logout/", MyLogout.as_view(), name="Logout"),
    path("register/", register, name="Register"),
    #SECCION
    path("seccion/list", SeccionList.as_view(), name="SeccionList"),
    path("r'(?P<pk>\d+)^$'", SeccionDetalle.as_view(), name="SeccionDetail"),
    path("seccion-nuevo/", SeccionCreacion.as_view(), name="SeccionNew"),
    path("secccion-editar/<pk>", SecccionUpdateView.as_view(), name="SeccionUpdate"),
    path("secccion-borrar/<pk>", SeccionDelete.as_view(), name="SeccionDelete"),
    #ARTTICULO
    path("articulo/list", ArticuloList.as_view(), name="ArticuloList"),
    path("r'(?P<pk>\d+)^$'", ArticuloDetalle.as_view(), name="ArticuloDetail"),
    path("articulo-nuevo/", ArticuloCreacion.as_view(), name="ArticuloNew"),
    path("articulo-editar/<pk>", ArticuloUpdateView.as_view(), name="ArticuloUpdate"),
    path("articulo-borrar/<pk>", ArticuloDelete.as_view(), name="ArticuloDelete"),
    ]
