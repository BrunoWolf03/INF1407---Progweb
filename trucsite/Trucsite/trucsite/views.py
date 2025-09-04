from django.shortcuts import render
from contatos.models import Pessoa
from django.views.generic.base import View

class ContatoListView(View):
    def get(self, request, *args, **kwargs):
        pessoas = Pessoa.objects.all()
        contexto = { 'pessoas': pessoas, }
        return render(request,'contatos/listaContatos.html', contexto)   