"""unica URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path,include
from .views import *

urlpatterns = [
    path('',index,name='index'),
    path('servicos/',servicos,name='servicos'),
    path('agenda/',agenda,name='agenda'),
    path('fale-conosco/',fale_conosco,name='fale_conosco'),
    path('sobre/',sobre,name='sobre'),
    path('api-textos',AppTextosList.as_view(), name='api-textos'),
    path('api-textos/<pk>',AppTextosListItems.as_view(), name='api-textos'),
    path('api-servicos',AppServicosList.as_view(),name='api-servicos'),
    path('api-servicos/<pk>',AppServicosListItems.as_view(),name='api-servicos')

]
