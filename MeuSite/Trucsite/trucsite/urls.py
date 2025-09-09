from django.urls import path

from . import views

urlpatterns = [
    
    path("JogadorListView", views.JogadorListView.as_view(), name="lista-jogadores"),

]