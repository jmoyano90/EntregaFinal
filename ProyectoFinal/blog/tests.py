from datetime import datetime
from django.test import TestCase
from blog.models import Articulo


class ViewTestCase(TestCase):

    def test_crear_curso(self):
        Articulo.objects.create(titulo="test 1234")
        todos_los_articulos = Articulo.objects.all()
        assert len(todos_los_articulos) == 1
        assert todos_los_articulos[0].titulo == "test 1234"


    def test_crear_articulo_sin_fecha(self):
        Articulo.objects.create(titulo="test 1234")
        todos_los_articulos = Articulo.objects.all()
        assert todos_los_articulos[0].fecha is None


    def test_crear_4_articulos(self):
        Articulo.objects.create(titulo="articulo 01")
        Articulo.objects.create(titulo="articulo 02")
        Articulo.objects.create(titulo="articulo 03")
        Articulo.objects.create(titulo="articulo 04")
        #Articulo.objects.create(titulo="articulo 05")
        todos_los_articulos = Articulo.objects.all()
        assert len(todos_los_articulos) == 4



