# core/admin.py
from django.contrib import admin
from .models import Jogador

@admin.register(Jogador)
class JogadorAdmin(admin.ModelAdmin):
    list_display = ("nome", "curso", "periodo", "email", "vitorias", "derrotas")
    search_fields = ("nome", "email", "curso")
    list_filter = ("curso", "periodo")
