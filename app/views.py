from django.shortcuts import render
from django.http import HttpResponseRedirect, request
# Página inicial do aplicativo
def index(request):
    return render(request,'index.html')
def servicos(request):
    return render(request,'servicos.html')
def agenda(request):
    return render(request,'agenda.html')
def fale_conosco(request):
    return render(request,'fale_conosco.html')
def sobre(request):
    return render(request,'sobre.html')

