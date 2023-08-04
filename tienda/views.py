from django.shortcuts import render
from django.views import generic
from .models import Producto


# Create your views here.
class ProductoIndex(generic.ListView):
    model = Producto
    template_name = 'tienda/index.html'

class ProductoDetails(generic.DetailView):
    model = Producto
    template_name = 'tienda/producto_details.html'