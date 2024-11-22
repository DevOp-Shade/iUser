from django.urls import path
from . import views

urlpatterns = [
    path('', views.Client, name='Client'),
]