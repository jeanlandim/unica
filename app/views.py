from django.shortcuts import render
from django.http import HttpResponseRedirect, request
from .models import AppTextos, AppServicos
# Página inicial do aplicativo
def index(request):
    titulo = AppTextos.objects.get(pagina__startswith='index/').titulo
    texto = AppTextos.objects.get(pagina__startswith='index/').texto
    return render(request,'index.html',{'titulo':titulo,'texto':texto})
def servicos(request):
    titulos = list()
    textos = list()
    duracoes = list() 
    ids = AppServicos.objects.count()

    for id_ in range(1,ids+1):  
        titulos = AppTextos.objects.get(pk=id_).titulo
        textos = AppTextos.objects.get(pk=id_).texto
        duracoes = AppTextos.objects.get(pk=id_).duracao
    return render(request,'servicos.html',{'titulos':titulos,'textos':textos,'duracoes':duracoes})
def agenda(request):
    return render(request,'agenda.html')
def fale_conosco(request):
    titulo = AppTextos.objects.get(pagina__startswith='fale-conosco/').titulo
    texto = AppTextos.objects.get(pagina__startswith='fale-conosco/').texto
    return render(request,'fale_conosco.html',{'titulo':titulo,'texto':texto})
def sobre(request):
    titulo = AppTextos.objects.get(pagina__startswith='sobre/').titulo
    texto = AppTextos.objects.get(pagina__startswith='sobre/').texto
    return render(request,'sobre.html',{'titulo':titulo,'texto':texto})

