"""
URL configuration for User project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('Landing.urls')),
    path('iUser/', include('iUser.urls')),
    path('iUsers/', include('iUsers.urls')),
    path('iUserForm/',include('iUserForm.urls')),
    path('iUserLogin/', include('iUserLogin.urls')),
    path('Main/', include('Main.urls')),
    path('Clips/', include('Clips.urls')),
    path('businessSuites/', include('businessSuites.urls')),
]
