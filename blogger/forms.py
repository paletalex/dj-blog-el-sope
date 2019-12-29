from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title','slug', 'author','tags', 'category', 'content', 'img']
        widgets = {
            'title':forms.TextInput(attrs={'class':'form-control','placeholder':'Titulo'}),
            'slug':forms.TextInput(attrs={'class':'form-control','placeholder':'ejemplo: Titulo-de-la-publicacion'}),
            'author':forms.Select(attrs={'class':'form-control'}),
            'tags':forms.SelectMultiple(attrs={'class':'form-control', 'size':15}),
            'category':forms.Select(attrs={'class':'form-control'}),
            'content':forms.Textarea(attrs={'class':'form-control','placeholder':'Ingresa tu contenido'}),
            'img':forms.URLInput(attrs={'class':'form-control','placeholder':'Ingresa enlace de la imagen'})
            
        }
        labels = {
            'title':'',
            'slug':'',
            'author':'Autor',
            'tags':'Tags',
            'category':'Categoria',
            'content':'',
            'img':''
        }