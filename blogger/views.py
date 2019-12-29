from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.db.models import Q
from django.urls import reverse_lazy
from .models import Post, Tag, Category
from .forms import PostForm
from django.views.generic.base import TemplateView
from django.views.generic.list import ListView 
from django.views.generic.detail import DetailView 
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.admin.views.decorators import staff_member_required
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import permission_required
from django.contrib.auth.models import User
import random

# Create your views here.

class Home(ListView):
    template_name = 'blogger/home.html'
    model = Post
    paginate_by = 10

class PostDetail(DetailView):
    template_name = 'blogger/post.html'
    model = Post

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        #obtenemos una lista con los ids de los post
        posts = list(Post.objects.filter().values_list('id',flat = True))

        #removemos el post que obtiene el detail
        posts.remove(self.object.id)

        #Generamos guardamos en una variables ids random y los vamos borrando
        try:
            post1 = random.choice(posts)
            posts.remove(post1)
            post2 = random.choice(posts)
            posts.remove(post2)
            post3 = random.choice(posts)
            posts.remove(post3)
        except:
            post1=post2=post3 = None
        
        #obtenemos los post con los ids randoms generados
        context['post1'] = get_object_or_404(Post, id = post1)
        context['post2'] = get_object_or_404(Post, id = post2)
        context['post3'] = get_object_or_404(Post, id = post3)
        return context


class TagDetail(DetailView):
    template_name = 'blogger/tag.html'
    model = Tag

class AuthorView(DetailView):
    template_name = 'blogger/author.html'

    def get_object(self):
        return get_object_or_404(User, username=self.kwargs['username'])

class CategoryList(ListView):
    template_name = 'blogger/category.html'
    paginate_by = 10
    
    def get_queryset(self):
       
        category = get_object_or_404(Category, name = self.kwargs['name'])
        # posts = get_list_or_404(Post, category = category)
        posts = Post.objects.filter(category = category)
        return  posts
        
    #Regresa como contexto la categoria
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category'] = get_object_or_404(Category, name = self.kwargs['name'])
        return context

class SearchList(ListView):
    model = Post
    template_name = 'blogger/search.html'

    def get_queryset(self): # new
        queryset = self.request.GET.get('buscar')
        posts = Post.objects.filter(
            Q(title__icontains=queryset) | Q(content__icontains=queryset)
        ).distinct()
        return posts
    # def get(self, request, *args, **kwargs):
    #     queryset = request.GET.get('buscar')
    #     posts = Post.objects.filter(
    #                 Q(title__icontains = queryset) |
    #                 Q(content__icontains = queryset),
    #             ).distinct()
   
    #     return render(request, 'blogger/search.html', {'posts': posts, 'queryset': queryset})

class FailView(TemplateView):
    template_name = 'blogger/fail.html'

######## CRUD
@method_decorator(permission_required('blogger.add_post'), name='dispatch')
class PostCreate(CreateView):
    model = Post
    form_class = PostForm
    success_url = reverse_lazy('home')
    template_name = 'blogger/create_post.html'

@method_decorator(permission_required('blogger.change_post', reverse_lazy('fail')), name='dispatch')
class PostUpdate(UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'blogger/update_post.html'
    def get_success_url(self):
        return reverse_lazy('update', args=[self.object.slug]) + '?ok'

@method_decorator(permission_required('blogger.delete_post', reverse_lazy('fail')), name='dispatch')
class PostDelete(DeleteView):
    model = Post
    form_class = PostForm
    success_url = reverse_lazy('home')
    template_name = 'blogger/delete_post.html'




 
    


