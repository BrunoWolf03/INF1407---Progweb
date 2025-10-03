# core/views.py
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin  # ⬅️ adicionado
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView
from .models import Jogador, Partida
from .forms import JogadorForm, CustomUserCreationForm, PartidaForm
from django.contrib.auth import views as auth_views
from django.contrib.auth import logout
from django.shortcuts import redirect, get_object_or_404
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect


class JogadorListView(ListView):
    model = Jogador
    template_name = "core/jogador_list.html"   # ⬅️ corrigido
    context_object_name = "jogadores"
    paginate_by = 20  # opcional

class JogadorDetailView(DetailView):
    model = Jogador
    template_name = "core/jogador_detail.html"
    context_object_name = "jogador"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        jogador = self.object
        # Pega todas as partidas do jogador
        partidas = Partida.objects.filter(jogador1=jogador) | Partida.objects.filter(jogador2=jogador)
        partidas = partidas.order_by('-id')  # mais recentes primeiro
        context['partidas'] = partidas
        return context

class JogadorCreateView(CreateView):
    model = Jogador
    form_class = JogadorForm
    template_name = "core/jogador_form.html"
    success_url = reverse_lazy("jogador_list") 

class JogadorSelfUpdateView(LoginRequiredMixin, UpdateView):
    model = Jogador
    form_class = JogadorForm
    template_name = "core/jogador_form.html"
    success_url = reverse_lazy("jogador_list")

    def get_object(self, queryset=None):
        # sempre edita só o jogador logado
        return get_object_or_404(Jogador, user=self.request.user)

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        # remove do form (não aparece no HTML)
        form.fields.pop("vitorias", None)
        form.fields.pop("derrotas", None)
        return form

    def form_valid(self, form):
        # proteção extra: mesmo se tentarem mandar vitorias/derrotas via POST
        jogador = form.save(commit=False)
        jogador.vitorias = self.get_object().vitorias
        jogador.derrotas = self.get_object().derrotas
        jogador.save()
        return super().form_valid(form)

# ==== Somente quem tiver permissão pode REMOVER ====
class JogadorDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Jogador
    template_name = "core/jogador_confirm_delete.html"
    success_url = reverse_lazy("jogador_list")
    permission_required = "core.delete_jogador"
    raise_exception = True



@login_required
def PartidaEscolherJogadorView(request):
    jogador1 = request.user.jogador

    if request.method == "POST":
        jogador2_id = request.POST.get("jogador2")
        try:
            jogador2 = Jogador.objects.get(id=jogador2_id)
            if jogador2 == jogador1:
                raise ValueError("Não pode escolher você mesmo como Jogador 2")
        except (Jogador.DoesNotExist, ValueError):
            return render(request, "core/erro.html", {"mensagem": "Jogador inválido."})
        
        # Salva temporariamente na sessão
        request.session['jogador2_id'] = jogador2.id
        return redirect("partida_detalhes")  # próxima tela
    
    # Lista apenas jogadores válidos (exceto o jogador1)
    jogadores = Jogador.objects.exclude(id=jogador1.id)
    return render(request, "core/escolher_jogador.html", {"jogadores": jogadores})

@login_required
def PartidaDetalhesView(request):
    jogador1 = request.user.jogador
    jogador2_id = request.session.get("jogador2_id")
    if not jogador2_id:
        return redirect("partida_escolher_jogador")
    
    jogador2 = Jogador.objects.get(id=jogador2_id)

    if request.method == "POST":
        form = PartidaForm(request.POST, jogador1=jogador1, jogador2=jogador2)
        if form.is_valid():
            partida = form.save(commit=False)
            partida.jogador1 = jogador1
            partida.jogador2 = jogador2
            partida.save()
            del request.session['jogador2_id']
            return redirect("jogador_list")
    else:
        form = PartidaForm(request.POST or None, jogador1=jogador1, jogador2=jogador2)

    return render(request, "core/escolher_detalhes.html", {
        "form": form,
        "jogador1": jogador1,
        "jogador2": jogador2
    })



@login_required
def PartidaListView(request):
    partidas = Partida.objects.all().order_by("-data")
    return render(request, "lista_partidas.html", {"partidas": partidas})


class PartidaDeleteView(DeleteView):
    model = Partida
    template_name = "core/partida_confirm_delete.html"

    def get_success_url(self):
        jogador = self.object.jogador1  
        return reverse_lazy("jogador_detail", kwargs={"pk": jogador.pk})

class PartidaUpdateView(UpdateView):
    model = Partida
    fields = ["jogador1", "jogador2", "vencedor", "perdedor", "pontos"]  
    template_name = "core/partida_form.html"
    success_url = reverse_lazy("home")


class HomeView(TemplateView):
    template_name = "core/home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["ranking"] = Jogador.objects.order_by("-vitorias")[:5]
        return context

class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    template_name = "core/registration/signup.html"
    success_url = reverse_lazy("login")


class LoginView(auth_views.LoginView):
    template_name = "core/registration/login.html"
    redirect_authenticated_user = True

    def form_valid(self, form):
        response = super().form_valid(form)
        remember = self.request.POST.get("remember")
        self.request.session.set_expiry(60*60*24*14 if remember else 0)
        return response

class LogoutView(auth_views.LogoutView):
    next_page = reverse_lazy("home")

# ====== Password Reset (4 telas) ======
class PasswordResetView(auth_views.PasswordResetView):
    template_name = "core/registration/password_reset_form.html"
    email_template_name = "core/registration/password_reset_email.html"
    subject_template_name = "core/registration/password_reset_subject.txt"
    success_url = reverse_lazy("password_reset_done")
    from_email = getattr(settings, "DEFAULT_FROM_EMAIL", None)

class PasswordResetDoneView(auth_views.PasswordResetDoneView):
    template_name = "core/registration/password_reset_done.html"

class PasswordResetConfirmView(auth_views.PasswordResetConfirmView):
    template_name = "core/registration/password_reset_confirm.html"
    success_url = reverse_lazy("password_reset_complete")

class PasswordResetCompleteView(auth_views.PasswordResetCompleteView):
    template_name = "core/registration/password_reset_complete.html"

