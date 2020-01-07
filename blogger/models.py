from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now
from ckeditor.fields import RichTextField

# Create your models here.
class Tag(models.Model):
    slug = models.SlugField('Nombre', unique=True)
    created = models.DateTimeField('Fecha de creacion', auto_now=True, auto_now_add=False)
    updated = models.DateTimeField('Fecha de modificacion', auto_now=False, auto_now_add=True)

    class Meta:
        verbose_name = 'Tag'
        verbose_name_plural = 'Tags'

    def __str__(self):
        return self.slug

class Category(models.Model):
    name = models.CharField('Clave', max_length=200)
    slug = models.SlugField('Nombre', unique=True)
    created = models.DateTimeField('Fecha de creacion', auto_now=True, auto_now_add=False)
    updated = models.DateTimeField('Fecha de modificacion', auto_now=False, auto_now_add=True)

    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'

    def __str__(self):
        return self.slug

class Post(models.Model):
    title = models.CharField('Titulo', max_length=200, unique=True)
    slug = models.SlugField('Slug', unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name = 'get_posts', verbose_name='Autor')
    tags = models.ManyToManyField(Tag, related_name = 'get_posts', verbose_name='Tags')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name = 'get_posts', verbose_name='Categoria')
    published = models.DateTimeField('Fecha de publicacion', default=now)
    content = RichTextField('Contenido')
    img = models.URLField('Imagen', max_length=200)
    public = models.BooleanField('Estado', default=False)
    created = models.DateTimeField('Fecha de creacion', auto_now=True, auto_now_add=False)
    updated = models.DateTimeField('Fecha de modificacion', auto_now=False, auto_now_add=True)

    class Meta:
        verbose_name = 'Entrada'
        verbose_name_plural = 'Entradas'

    def __str__(self):
        return self.title

    

