from .models import Social
from django.shortcuts import get_list_or_404

def ctx_redes(request):
    ctx = dict()
    #redes = get_list_or_404(Social)
    redes= Social.objects.all()
    for r in redes:
        ctx[r.key]=r.link
    return ctx