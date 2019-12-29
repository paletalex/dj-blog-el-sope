from django.shortcuts import render, get_object_or_404
from django.views.generic.detail import DetailView
from .models import Page
# Create your views here.

class PageView(DetailView):
    template_name = 'pages/sample.html'
    model = Page

    # def get_object(self):
    #     return get_object_or_404(Page, title=self.kwargs['title'])