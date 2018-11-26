from django.db import models

# Create your models here.
class categoriaProducto(models.Model):
  	nombre = models.CharField(max_length=50)
  	descripcion = models.TextField(max_length=400)
class producto(models.Model):
	nombre      = models.CharField(max_length=100)
	descripcion = models.TextField(max_length=300)
	status      = models.BooleanField(default=True)
	precio      = models.DecimalField(max_digits=6,decimal_places=2)
	stock       = models.IntegerField()
	categorias  = models.ForeignKey(categoriaProducto,null=True,blank=True, on_delete=models.DO_NOTHING)