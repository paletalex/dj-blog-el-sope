
from django.urls import path
from .views import Home, PostDetail, TagDetail, CategoryList, SearchList, PostCreate, PostUpdate, PostDelete, FailView, AuthorView
urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('post/<slug:slug>/', PostDetail.as_view(), name='post'),
    path('tag/<slug:slug>/', TagDetail.as_view(), name='tag'),
    path('category/<name>/', CategoryList.as_view(), name='category'),
    path('s/b/', SearchList.as_view(), name='search'),
    path('c/create/', PostCreate.as_view(), name='create'),
    path('u/update/<slug:slug>/', PostUpdate.as_view(), name='update'),
    path('d/delete/<slug:slug>/', PostDelete.as_view(), name='delete'),
    path('fail/denied-access/', FailView.as_view(), name='fail'),
    path('author/<username>/', AuthorView.as_view(), name='author'),
    
]
