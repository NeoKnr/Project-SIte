#mycollection/urls.py
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:tel_id>/', views.detail, name='detail'),
    path('<int:contact_id>/', views.detail, name='detail'),
]