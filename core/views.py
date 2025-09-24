# core/views.py
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin

from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView
from .models import Jogador
from .forms import JogadorForm
from django.contrib.auth import views as auth_views


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
    success_url = reverse_lazy("jogador_list")

class JogadorUpdateView(UpdateView):
    model = Jogador
    form_class = JogadorForm
    template_name = "core/jogador_form.html"
    success_url = reverse_lazy("jogador_list")

class JogadorDeleteView(DeleteView):
    model = Jogador
    template_name = "core/jogador_confirm_delete.html"
    success_url = reverse_lazy("jogador_list")


class HomeView(TemplateView):
    template_name = "core/home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        # Pega as últimas 5 partidas (se existir model Partida)
        #context["ultimas_partidas"] = Partida.objects.order_by("-data")[:5]

        # Ranking de jogadores (ordenado por vitórias, por exemplo)
        context["ranking"] = Jogador.objects.order_by("-vitorias")[:5]

        return context

class HomeView(LoginRequiredMixin, TemplateView):
    template_name = "core/home.html"  # precisa existir

class SignUpView(CreateView):
    form_class = UserCreationForm
    template_name = "core/registration/signup.html"
    success_url = reverse_lazy("login")  # ou faça login automático pós-cadastro

class LoginView(auth_views.LoginView):
    template_name = "core/registration/login.html"
    redirect_authenticated_user = True

    def form_valid(self, form):
        response = super().form_valid(form)
        remember = self.request.POST.get("remember")
        self.request.session.set_expiry(60*60*24*14 if remember else 0)
        return response
