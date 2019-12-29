from django.db import models

# Create your models here.

class Social(models.Model):
    key = models.SlugField('Clave', unique=True)
    name = models.CharField('Nombre', max_length=200)
    link = models.URLField('Enlace', max_length=200)
    created = models.DateTimeField('Fecha de creacion', auto_now=True, auto_now_add=False)
    updated = models.DateTimeField('Fecha de modificacion', auto_now=False, auto_now_add=True)

    class Meta:
        verbose_name = 'Red Social'
        verbose_name_plural = 'Redes Sociales'

    def __str__(self):
        return self.name
