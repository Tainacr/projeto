from django.shortcuts import render,redirect,get_object_or_404
from .models import *
from django.views import View
from django.contrib import messages

class IndexView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'index.html')
    def post(self, request):
        pass

class ViewOcupacao(View):
    def get(self, request, *args, **kwargs):
        ocupacao = Ocupacao.objects.all()
        return render(request, 'ocupacao.html', {'ocupacao':ocupacao})

class ViewOcupacao(View):
    def get(self, request, *args, **kwargs):
        ocupacao = Ocupacao.objects.all()
        return render(request, 'ocupacao.html', {'ocupacao':ocupacao})
    
class ViewOcupacao(View):
    def get(self, request, *args, **kwargs):
        ocupacao = Ocupacao.objects.all()
        return render(request, 'ocupacao.html', {'ocupacao':ocupacao})

class ViewOcupacao(View):
    def get(self, request, *args, **kwargs):
        ocupacao = Ocupacao.objects.all()
        return render(request, 'ocupacao.html', {'ocupacao':ocupacao})

class ViewOcupacao(View):
    def get(self, request, *args, **kwargs):
        ocupacao = Ocupacao.objects.all()
        return render(request, 'ocupacao.html', {'ocupacao':ocupacao})
