from django.db import models

# Create your models here.

class Alumno(models.Model):

    school_controll = models.CharField(max_length=25)
    name = models.CharField(max_length=150)
    age = models.IntegerField(default=18)
    email = models.EmailField(max_length=254)

    class Meta:
        ordering = ['name']