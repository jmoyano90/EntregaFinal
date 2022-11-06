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
    AutorList,
    AutorDetalle,
    AutorCreacion,
    AutorUpdateView,
    AutorDelete,
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
    path("seccion-detalle/<int:pk>/", SeccionDetalle.as_view(), name="SeccionDetail"),
    path("seccion-nuevo/", SeccionCreacion.as_view(), name="SeccionNew"),
    path("secccion-editar/<pk>", SecccionUpdateView.as_view(), name="SeccionUpdate"),
    path("secccion-borrar/<pk>", SeccionDelete.as_view(), name="SeccionDelete"),
    #ARTTICULO
    path("articulo/list", ArticuloList.as_view(), name="ArticuloList"),
    path("r'(?P<pk>\d+)^$'", ArticuloDetalle.as_view(), name="ArticuloDetail"),
    path("articulo-nuevo/", ArticuloCreacion.as_view(), name="ArticuloNew"),
    path("articulo-editar/<pk>", ArticuloUpdateView.as_view(), name="ArticuloUpdate"),
    path("articulo-borrar/<pk>", ArticuloDelete.as_view(), name="ArticuloDelete"),
    #AUTOR
    path("autor/list", AutorList.as_view(), name="AutorList"),
    path("seccion-autor/<int:pk>/", AutorDetalle.as_view(), name="AutorDetail"),
    path("autor-nuevo/", AutorCreacion.as_view(), name="AutorNew"),
    path("autor-editar/<pk>", AutorUpdateView.as_view(), name="AutorUpdate"),
    path("autor-borrar/<pk>", AutorDelete.as_view(), name="AutorDelete"),
    ]
