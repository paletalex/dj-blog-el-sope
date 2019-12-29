from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from .forms import ContactForm
from django.views.generic.edit import FormView
from django.core.mail import EmailMessage

# Create your views here.
class ContactView(FormView):
    template_name = 'contact/contact.html'
    form_class = ContactForm
    success_url = reverse_lazy('contact')

    def form_valid(self, form):
        name = form.cleaned_data['name']
        message = form.cleaned_data['message']
        email = form.cleaned_data['email']
        email = EmailMessage(
                    'El sope!: nuevo mensaje',
                    'de: {} <{}>\nMensaje: \n\n {}'.format(name, email, message),
                    'no-reply@gmail.com',
                    ['ilovedjaneiro@gmail.com'],
                    reply_to=[email]
                )
        try:
            email.send()
            return redirect(reverse('contact')+'?ok')
        except:
            return redirect(reverse('contact')+'?fail')
        
        return render(self.get_success_url())

