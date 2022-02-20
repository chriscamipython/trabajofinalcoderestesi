from django.db.models import Model
from django.db import models
from django.db.models.fields import CharField, IntegerField, EmailField, BooleanField, DateField
from django.template.defaultfilters import slugify
# Create your models here.

class Lugar(models.Model):
    nombre= models.CharField(max_length=40)
    grupo = models.IntegerField()

class Compradores(models.Model):
    
    nombre =models.CharField(max_length=50)
    apellido= models.CharField(max_length=30)
    email= models.EmailField()
    profesion= models.CharField(max_length=30)
    
class Vendedores(models.Model):
    nombre= models.CharField(max_length=30)
    apellido= models.CharField(max_length=30)
    email= models.EmailField()
    profesion= models.CharField(max_length=30)

class Objetos(models.Model):
    nombre= models.CharField(max_length=40)
    fechaDeEntrega = models.DateField()
    entregado = models.BooleanField()
    
    