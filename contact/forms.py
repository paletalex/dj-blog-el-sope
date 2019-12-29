from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(label='Nombre', max_length=200, required=True)
    email = forms.EmailField(label='Email', required=True)
    message = forms.CharField(label="Contenido", required=True)

