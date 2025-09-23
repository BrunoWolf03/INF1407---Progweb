# core/views.py
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView
from .models import Jogador
from .forms import JogadorForm

class JogadorListView(ListView):
    model = Jogador
    template_name = "core/jogador_list.html.html"
    context_object_name = "jogadores"
    paginate_by = 20  # opcional

class JogadorDetailView(DetailView):
    model = Jogador
    template_name = "core/jogador_detail.html"
    context_object_name = "jogador"

class JogadorCreateView(CreateView):
    model = Jogador
    form_class = JogadorForm
    template_name = "core/jogador_form.html"
    success_url = reverse_lazy("core:jogador_list")

class JogadorUpdateView(UpdateView):
    model = Jogador
    form_class = JogadorForm
    template_name = "core/jogador_form.html"
    success_url = reverse_lazy("core:jogador_list")

class JogadorDeleteView(DeleteView):
    model = Jogador
    template_name = "core/jogador_confirm_delete.html"
    success_url = reverse_lazy("core:jogador_list")


class HomeView(TemplateView):
    template_name = "core/home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        # Pega as últimas 5 partidas (se existir model Partida)
        #context["ultimas_partidas"] = Partida.objects.order_by("-data")[:5]

        # Ranking de jogadores (ordenado por vitórias, por exemplo)
        context["ranking"] = Jogador.objects.order_by("-vitorias")[:5]

        return context