from django.shortcuts import render,redirect,get_object_or_404
from .models import * 
from django.views import View
from django.contrib import messages

# Create your views here.

class IndesView(View):
    def get(self,request, *args, **kwargs):
        return render (request, 'index.html')
    def post(self, request):
        pass

class AtendimentoView(View):
    def get(self, request, *argas, **kwargs):
        return render (request, 'atendimento.html')
    def post(self, request):
        pass 

class GaleriaDePlantaView(View):
    def get(self,request, *args, **kwargs):
        return render (request, 'galeriadeplanta.gtml')
    def post(self, request):
        pass 

