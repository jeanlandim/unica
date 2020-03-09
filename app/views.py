from django.shortcuts import render
from django.http import HttpResponseRedirect, request
from rest_framework import generics
from .models import AppTextos, AppServicos
from .serializers import *
# Página inicial do aplicativo
def index(request):
    titulo = AppTextos.objects.get(pagina__startswith='index/').titulo
    texto = AppTextos.objects.get(pagina__startswith='index/').texto
    return render(request,'index.html',{'titulo':titulo,'texto':texto})
def servicos(request):
    duracoes, descricoes, servicos = list(), list(), list()
    ids = AppServicos.objects.count()	
    for id_ in range(1,ids+1):  
        servicos.append(AppServicos.objects.get(pk=id_).servico)
        descricoes.append(AppServicos.objects.get(pk=id_).descricao)
        duracoes.append(AppServicos.objects.get(pk=id_).duracao)
    return render(request,'servicos.html',{'servicos':servicos,'descricoes':descricoes,'duracoes':duracoes})
def agenda(request):
    return render(request,'agenda.html')
def sobre(request):
    titulo = AppTextos.objects.get(pagina__startswith='sobre/').titulo
    texto = AppTextos.objects.get(pagina__startswith='sobre/').texto
    return render(request,'sobre.html',{'titulo':titulo,'texto':texto})
# API 
class AppTextosList(generics.ListCreateAPIView):
    queryset = AppTextos.objects.all()
    serializer_class = TextosSerializer
class AppServicosList(generics.ListCreateAPIView):
    queryset = AppServicos.objects.all()
    serializer_class = ServicosSerializer
class AppTextosListItems(generics.RetrieveUpdateDestroyAPIView):
    queryset = AppTextos.objects.all()
    serializer_class = TextosSerializer
class AppServicosListItems(generics.RetrieveUpdateDestroyAPIView):
    queryset = AppServicos.objects.all()
    serializer_class = ServicosSerializer





