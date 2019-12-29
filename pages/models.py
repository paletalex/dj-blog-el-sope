from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.
class Page(models.Model):
    title = models.CharField('Titulo', max_length=200)
    content = RichTextField('Contenido')
    created = models.DateTimeField('Fecha de creacion', auto_now=True, auto_now_add=False)
    updated = models.DateTimeField('Fecha de modificacion', auto_now=False, auto_now_add=True)

    class Meta:
        verbose_name = 'Pagina'
        verbose_name_plural = 'Paginas'
        ordering = ['title']

    def __str__(self):
        return self.title