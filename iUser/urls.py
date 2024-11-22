from django.urls import path
from . import views

urlpatterns = [
    path('', views.iForm, name='iForm'),
    path('iFormNav/', views.iFormNav, name='iFormNav'),
    path('iCoreForm/', views.iCoreForm, name='iCoreForm'),
    path('imainForm/', views.imainForm, name='imainForm'),
    path('imainPortfolioForm/', views.imainPortfolioForm, name='imainPortfolioForm'),
]