from django.urls import path
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
    path("accounts/logout/", views.LogoutView.as_view(next_page="home"), name="logout"),
    path('accounts/password_reset/',views.PasswordResetView.as_view(), name='password_reset'),

    path('accounts/password_reset/done/', views.PasswordResetDoneView.as_view(),name='password_reset_done'),

    path('accounts/reset/<uidb64>/<token>/',views.PasswordResetConfirmView.as_view(),name='password_reset_confirm'),

    path('accounts/reset/done/',views.PasswordResetCompleteView.as_view(),name='password_reset_complete'),
    path("jogadores/me/editar/", views.JogadorSelfUpdateView.as_view(), name="jogador_update_self"),

    path("partidas/escolher/", views.PartidaEscolherJogadorView, name="partida_escolher_jogador"),
    path("partidas/nova/", views.PartidaDetalhesView, name="partida_detalhes"),
    path("partidas/", views.PartidaListView, name="lista_partidas"),
    path("partida/<int:pk>/editar/", views.PartidaUpdateView.as_view(), name="partida_update"),
    path("partida/<int:pk>/apagar/", views.PartidaDeleteView.as_view(), name="partida_delete"),


]

