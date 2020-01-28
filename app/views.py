from django.shortcuts import render
from django.http import HttpResponseRedirect, request
# Página inicial do aplicativo
def index(request):
    return render(request,'index.html')

