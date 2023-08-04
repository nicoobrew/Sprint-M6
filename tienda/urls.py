from django.urls import path
from . import views

app_name = 'tienda'

urlpatterns = [
    path("", views.ProductoIndex.as_view(), name='home'),
    path("details/<int:pk>", views.ProductoDetails.as_view(), name='detalle'),
    
]
