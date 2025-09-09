from django.shortcuts import render
from trucsite.models import Jogador
from django.views.generic.base import View

class JogadorListView(View):
    def get(self, request, *args, **kwargs):
        jogadores = Jogador.objects.all()
        contexto = { 'jogador': jogadores, }
        return render(request,'trucsite/listaJogadores.html', contexto)   