from django.db import models

# Create your models here.
class Producto(models.Model):
    titulo = models.CharField(max_length=70)
    descripcion = models.TextField()
    precio = models.IntegerField()
    imagen = models.ImageField(upload_to='tienda/img', default='tienda/img/gato.jpg', null=True)

    def __str__(self):
        return self.titulo