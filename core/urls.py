from django.urls import path

from . import views


app_name = "core"
urlpatterns = [
    path("home/", views.HomeView.as_view(), name="home"),
    path("jogadores/", views.JogadorListView.as_view(), name="jogador_list"),
    path("jogadores/novo/", views.JogadorCreateView.as_view(), name="jogador_create"),
    path("jogadores/<int:pk>/", views.JogadorDetailView.as_view(), name="jogador_detail"),
    path("jogadores/<int:pk>/editar/", views.JogadorUpdateView.as_view(), name="jogador_update"),
    path("jogadores/<int:pk>/remover/", views.JogadorDeleteView.as_view(), name="jogador_delete"),
]