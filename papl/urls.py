from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('main', views.main, name='main'),
    path('upload', views.upload, name='upload'),
]