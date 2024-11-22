from django.urls import path
from . import views

urlpatterns = [
    path('', views.Index, name='Index'),
    path('iRegister/', views.iRegister, name='iRegister'),
    path('iLogin/', views.iLogin, name='iLogin'),
    
]