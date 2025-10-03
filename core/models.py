from django.db import models
from django.contrib.auth.models import User
from django.templatetags.static import static

class Jogador(models.Model):
    id = models.AutoField(primary_key=True)

    user = models.OneToOneField(
        User,
        on_delete=models.SET_NULL,
        null=True, blank=True,
        related_name="jogador",
        help_text="Usuário associado a este jogador (opcional)",
    )

    nome = models.CharField(max_length=100, help_text='Entre o nome', blank=True, default="")
    curso = models.CharField(max_length=100, help_text='Entre o curso', blank=True, default="")
    periodo = models.IntegerField(help_text='Informe o período do curso', default=0)
    email = models.EmailField(help_text='Informe o email', max_length=254, blank=True, default="")
    vitorias = models.IntegerField(help_text='Número de vitórias', default=0)
    derrotas = models.IntegerField(help_text='Número de derrotas', default=0)
    imagem = models.ImageField(upload_to='jogadores/', null=True, blank=True)

    # “Em branco” para data = permitir nulo
    dtNasc = models.DateField(
        help_text='Nascimento no formato DD/MM/AAAA',
        verbose_name='Data de nascimento',
        null=True, blank=True,
    )

    def __str__(self):
        return self.nome or (self.user.get_username() if self.user else f"Jogador #{self.id}")

    @property
    def imagem_url(self) -> str:
        try:
            if self.imagem and self.imagem.name:
                return self.imagem.url
        except ValueError:
            pass
        return static('img/defaultavatar.png')