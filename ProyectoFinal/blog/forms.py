from django import forms


class ArticuloForm(forms.Form):
    titulo = forms.CharField(max_length=30)
    texto = forms.CharField(max_length=1000)
    fecha = forms.DateTimeField()


class AutorForm(forms.Form):
    nombre = forms.CharField(max_length=30)
    apellido = forms.CharField(max_length=30)
    profesion = forms.CharField(max_length=30)


class SeccionForm(forms.Form):
    nombre = forms.CharField(max_length=30)
