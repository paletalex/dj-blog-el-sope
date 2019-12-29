from .models import Page

def ctx_pages(request):
    pages = Page.objects.all()
    return ({'pages':pages})