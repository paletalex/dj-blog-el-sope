from .models import Tag
from django.shortcuts import get_list_or_404

def ctx_tags(request):
    # tags = get_list_or_404(Tag)
    tags = Tag.objects.all()
    return {'tags':tags}


