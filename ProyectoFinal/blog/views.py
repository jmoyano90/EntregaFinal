from multiprocessing import context
from django.http import HttpResponse
from django.shortcuts import render
from blog.models import Articulo, Autor, Seccion, Avatar
from blog.forms import ArticuloForm, AutorForm, SeccionForm
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.views.generic import ListView 
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from blog.forms import AvatarForm, UserEditionForm



#SECCION############################################################################################
class SeccionList(LoginRequiredMixin, ListView):    
    model = Seccion
    template_name = "blog/secciones_list.html"

class SeccionDetalle(LoginRequiredMixin, DetailView):
    model: Seccion
    template_name = "blog/secciones_detalle.html"

class SeccionCreacion(LoginRequiredMixin, CreateView):
    model = Seccion
    fields = ["nombre"]
    success_url = "/blog/seccion/list"
    

class SecccionUpdateView(LoginRequiredMixin, UpdateView):
    model = Seccion
    success_url = "/blog/seccion/list"
    fields = ["nombre"]

class SeccionDelete(LoginRequiredMixin, DeleteView):
    model = Seccion
    success_url = "/blog/seccion/list"

#ARTICULO#############################################################################################
class ArticuloList(LoginRequiredMixin, ListView):    
    model = Articulo
    template_name = "blog/articulos_list.html"

class ArticuloDetalle(LoginRequiredMixin, DetailView):
    model: Articulo
    template_name = "blog/articulos_detalle.html"

class ArticuloCreacion(LoginRequiredMixin, CreateView):
    model = Articulo
    fields = ["titulo", "texto", "fecha"]
    success_url = "/blog/articulo/list"

class ArticuloUpdateView(LoginRequiredMixin, UpdateView):
    model = Articulo
    success_url = "/blog/articulo/list"
    fields = ["titulo", "texto", "fecha"]

class ArticuloDelete(LoginRequiredMixin, DeleteView):
    model = Articulo
    success_url = "/blog/articulo/list"

#AUTOR#############################################################################################
class AutorList(LoginRequiredMixin, ListView):    
    model = Autor
    template_name = "blog/autores_list.html"

class AutorDetalle(LoginRequiredMixin, DetailView):
    model: Autor
    template_name = "blog/autores_detalle.html"

class AutorCreacion(LoginRequiredMixin, CreateView):
    model = Autor
    fields = ["nombre", "apellido", "profesion"]
    success_url = "/blog/autor/list"
    
class AutorUpdateView(LoginRequiredMixin, UpdateView):
    model = Autor
    success_url = "/blog/autor/list"
    fields = ["nombre", "apellido", "profesion"]

class AutorDelete(LoginRequiredMixin, DeleteView):
    model = Autor
    success_url = "/blog/autor/list"



@login_required
def buscar_articulo(request):
    if request.method == "GET":
        return render(request, "blog/formulario-de-busqueda-articulo.html")
    
    if request.method == "POST":
        titulo_para_buscar = request.POST.get("titulo")
        resultados_de_busqueda = Articulo.objects.filter(titulo=titulo_para_buscar)
        
        contexto = {"resultados":resultados_de_busqueda}
        return render(request, "blog/resultado-de-la-busqueda-articulo.html", context=contexto)

@login_required
def buscar_autor(request):
    if request.method == "GET":
        return render(request, "blog/formulario-de-busqueda-autor.html")
    
    if request.method == "POST":
        nombre_para_buscar = request.POST.get("nombre")
        resultados_de_busqueda_autor = Autor.objects.filter(nombre=nombre_para_buscar)
        
        contexto = {"resultados":resultados_de_busqueda_autor}
        return render(request, "blog/resultado-de-la-busqueda-autor.html", context=contexto)

@login_required
def buscar_seccion(request):
    if request.method == "GET":
        return render(request, "blog/formulario-de-busqueda-seccion.html")
    
    if request.method == "POST":
        nombre_para_buscar = request.POST.get("nombre")
        resultados_de_busqueda_autor = Seccion.objects.filter(nombre=nombre_para_buscar)
        
        contexto = {"resultados":resultados_de_busqueda_autor}
        return render(request, "blog/resultado-de-la-busqueda-seccion.html", context=contexto) 

@login_required
def mostrar_inicio(request):
    avatar = Avatar.objects.filter(user=request.user).first()
    if avatar is not None:
        context = {"avatar": avatar.imagen.url}
    else:
        context = {}
    return render(request, "blog/inicio.html", context)

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

@login_required
def editar_perfil(request):
    user = request.user
    avatar = Avatar.objects.filter(user=request.user).first()
    if request.method != "POST":
        form = UserEditionForm(initial={"email": user.email})
    else:
        form = UserEditionForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user.email = data["email"]
            user.first_name = data["first_name"]
            user.last_name = data["last_name"]
            user.set_password(data["password1"])
            user.save()
            return render(request, "blog/inicio.html", {"avatar": avatar.imagen.url})

    contexto = {
        "user": user,
        "form": form,
        "avatar": avatar.imagen.url
    }
    return render(request, "blog/editar_perfil.html", contexto)

@login_required
def agregar_avatar(request):
    if request.method != "POST":
        form = AvatarForm()
    else:
        form = AvatarForm(request.POST, request.FILES)
        if form.is_valid():
            Avatar.objects.filter(user=request.user).delete()
            form.save()
            return render(request, "blog/inicio.html")

    contexto = {"form": form}
    return render(request, "blog/avatar_form.html", contexto)

@login_required
def about(request):
    return render(request, "blog/about.html", {})