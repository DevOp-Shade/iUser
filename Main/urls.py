from django.urls import path
from . import views

urlpatterns = [
    path('', views.iMain, name='iMain'),
    path('iCore/', views.iCore, name='iCore'),
    path('imainHome/', views.imainHome, name='imainHome'),
    path('imainPortfolio/', views.imainPortfolio, name='imainPortfolio'),
]