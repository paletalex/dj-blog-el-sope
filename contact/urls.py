from django.urls import path 
from .views import ContactView

urlpatterns = [
    path('c/', ContactView.as_view(), name='contact'),
]