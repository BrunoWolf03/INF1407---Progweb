from django.urls import path
from django.contrib.auth.views import LogoutView
from . import views

urlpatterns = [
    path("", views.HomeView.as_view(), name="home"),   # agora "/" abre a Home
    path("home/", views.HomeView.as_view(), name="home_redirect"),  # opcional: /home/ também abre a Home
    path("jogadores/", views.JogadorListView.as_view(), name="jogador_list"),
    path("jogadores/novo/", views.JogadorCreateView.as_view(), name="jogador_create"),
    path("jogadores/<int:pk>/", views.JogadorDetailView.as_view(), name="jogador_detail"),
    path("jogadores/<int:pk>/editar/", views.JogadorUpdateView.as_view(), name="jogador_update"),
    path("jogadores/<int:pk>/remover/", views.JogadorDeleteView.as_view(), name="jogador_delete"),
    # Auth
    path("accounts/login/", views.LoginView.as_view(), name="login"),
    path("accounts/signup/", views.SignUpView.as_view(), name="signup"),
    path("accounts/logout/", LogoutView.as_view(next_page="home"), name="logout"),
]
