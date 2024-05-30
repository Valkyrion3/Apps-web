"""web URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
#from django.conf.urls import url, include
from app1.views import *


urlpatterns = [
    path('admin/', admin.site.urls),
    path('mostrar/',mostrar, name="mostrar"),
    path('',landing, name="landing"),
    path('post_agregar/',post_agregar, name="post_agregar"),
    path('calculadora/',calc, name="calculadora"),
    #Ruta del drive
    path("drive/", include("minidrive.urls")),
    path('convertidor',convertidor, name="convert"),
    path("proveedores/", include("proveedores.urls")),
    path('trycatch',include("Try_catch.urls")),
    path("xml/", include("crudXML.urls")),
]