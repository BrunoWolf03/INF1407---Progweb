# core/signals.py
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import Jogador

@receiver(post_save, sender=User)
def criar_jogador(sender, instance, created, **kwargs):
    if created:
        # cria “perfil” com campos em branco/default
        Jogador.objects.create(
            user=instance,
            nome=(instance.get_full_name() or instance.username or ""),
            email=(instance.email or ""),
            # demais campos já têm default no model
        )
