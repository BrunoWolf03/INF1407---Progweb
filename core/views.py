# core/views.py
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin  # ⬅️ adicionado
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView
from .models import Jogador
from .forms import JogadorForm, CustomUserCreationForm
from django.contrib.auth import views as auth_views
from django.contrib.auth import logout
from django.shortcuts import redirect, get_object_or_404
from django.conf import settings

class JogadorListView(ListView):
    model = Jogador
    template_name = "core/jogador_list.html"   # ⬅️ corrigido
    context_object_name = "jogadores"
    paginate_by = 20  # opcional

class JogadorDetailView(DetailView):
    model = Jogador
    template_name = "core/jogador_detail.html"
    context_object_name = "jogador"

class JogadorCreateView(LoginRequiredMixin, CreateView):
    model = Jogador
    form_class = JogadorForm
    template_name = "core/jogador_form.html"
    success_url = reverse_lazy("jogador_list")

# ==== Somente quem tiver permissão pode EDITAR ====
class JogadorUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = Jogador
    form_class = JogadorForm
    template_name = "core/jogador_form.html"
    success_url = reverse_lazy("jogador_list")
    permission_required = "core.change_jogador"   # app_label.change_model
    raise_exception = True  # retorna 403 em vez de redirecionar

class JogadorSelfUpdateView(LoginRequiredMixin, UpdateView):
    model = Jogador
    form_class = JogadorForm
    template_name = "core/jogador_form.html"
    success_url = reverse_lazy("jogador_list")

    def get_object(self, queryset=None):
        return get_object_or_404(Jogador, user=self.request.user)

# ==== Somente quem tiver permissão pode REMOVER ====
class JogadorDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Jogador
    template_name = "core/jogador_confirm_delete.html"
    success_url = reverse_lazy("jogador_list")
    permission_required = "core.delete_jogador"
    raise_exception = True

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
