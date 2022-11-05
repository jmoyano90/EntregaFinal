from multiprocessing import context
from django.http import HttpResponse
from django.shortcuts import render
from blog.models import Articulo, Autor, Seccion
from blog.forms import ArticuloForm, AutorForm, SeccionForm
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import UserCreationForm

def buscar_articulo(request):
    if request.method == "GET":
        return render(request, "blog/formulario-de-busqueda-articulo.html")
    
    if request.method == "POST":
        titulo_para_buscar = request.POST.get("titulo")
        resultados_de_busqueda = Articulo.objects.filter(titulo=titulo_para_buscar)
        
        contexto = {"resultados":resultados_de_busqueda}
        return render(request, "blog/resultado-de-la-busqueda-articulo.html", context=contexto)

def buscar_autor(request):
    if request.method == "GET":
        return render(request, "blog/formulario-de-busqueda-autor.html")
    
    if request.method == "POST":
        nombre_para_buscar = request.POST.get("nombre")
        resultados_de_busqueda_autor = Autor.objects.filter(nombre=nombre_para_buscar)
        
        contexto = {"resultados":resultados_de_busqueda_autor}
        return render(request, "blog/resultado-de-la-busqueda-autor.html", context=contexto)

def buscar_seccion(request):
    if request.method == "GET":
        return render(request, "blog/formulario-de-busqueda-seccion.html")
    
    if request.method == "POST":
        nombre_para_buscar = request.POST.get("nombre")
        resultados_de_busqueda_autor = Seccion.objects.filter(nombre=nombre_para_buscar)
        
        contexto = {"resultados":resultados_de_busqueda_autor}
        return render(request, "blog/resultado-de-la-busqueda-seccion.html", context=contexto) 


def mostrar_inicio(request):
    return render(request, "blog/inicio.html")


def procesar_fomulario_autor(request):

    if request.method == "GET":
        mi_formulario = AutorForm()
        contexto = {"formulario": mi_formulario}
        return render(request, "blog/formulario-autor.html", context=contexto)

    if request.method == "POST":
        mi_formulario = AutorForm(request.POST)
        if mi_formulario.is_valid():
            datos_ingresados_por_usuario = mi_formulario.cleaned_data
            nuevo_modelo = Autor(
                nombre=datos_ingresados_por_usuario["nombre"],
                apellido=datos_ingresados_por_usuario["apellido"],
                profesion=datos_ingresados_por_usuario["profesion"],
            )
        nuevo_modelo.save()

    contexto = {"formulario": mi_formulario}
    return render(request, "blog/formulario-autor.html", context=contexto)


def procesar_fomulario_articulo(request):

    if request.method == "GET":
        mi_formulario = ArticuloForm()
        contexto = {"formulario": mi_formulario}
        return render(request, "blog/formulario-articulo.html", context=contexto)

    if request.method == "POST":

        mi_formulario = ArticuloForm(request.POST)
        if mi_formulario.is_valid():
            datos_ingresados_por_usuario = mi_formulario.cleaned_data
            nuevo_modelo = Articulo(
                titulo=datos_ingresados_por_usuario["titulo"],
                texto=datos_ingresados_por_usuario["texto"],
                fecha=datos_ingresados_por_usuario["fecha"],
            )
        nuevo_modelo.save()

    contexto = {"formulario": mi_formulario}
    return render(request, "blog/formulario-articulo.html", context=contexto)


def procesar_fomulario_seccion(request):

    if request.method == "GET":
        mi_formulario = SeccionForm()
        contexto = {"formulario": mi_formulario}
        return render(request, "blog/formulario-seccion.html", context=contexto)

    if request.method == "POST":

        mi_formulario = SeccionForm(request.POST)
        if mi_formulario.is_valid():
            datos_ingresados_por_usuario = mi_formulario.cleaned_data
            nuevo_modelo = Seccion(
                nombre=datos_ingresados_por_usuario["nombre"],
            )
        nuevo_modelo.save()

    contexto = {"formulario": mi_formulario}
    return render(request, "blog/formulario-seccion.html", context=contexto)

class MyLogin(LoginView):
    template_name = "blog/login.html"

class MyLogout(LogoutView):
    template_name = "blog/logout.html"

def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            username_capturado = form.cleaned_data["username"]
            form.save()
            return render(request, "blog/inicio.html", {"mensaje": f"Usuario: {username_capturado}"})
    else:
        form = UserCreationForm()
    return render(request, "blog/register.html", {"form": form})


