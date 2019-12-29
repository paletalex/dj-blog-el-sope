from django.urls import path 
from .views import PageView

urlpatterns = [
    path("<int:pk>/<slug:title>", PageView.as_view(), name="page")
]
