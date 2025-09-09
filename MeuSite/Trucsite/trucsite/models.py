from django.db import models
class Jogador(models.Model):
    
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100, help_text='Entre o nome')
    curso = models.CharField(max_length=100, help_text='Entre o curso')
    periodo = models.IntegerField(help_text='Informe o período do curso')
    email = models.EmailField(help_text='Informe o email', max_length=254)
    vitorias = models.IntegerField(help_text='Número de vitórias')
    derrotas = models.IntegerField(help_text='Número de derrotas')
    imagem = models.ImageField(upload_to='jogadores/', null=True, blank=True)
    dtNasc = models.DateField(help_text='Nascimento no formato DD/MM/AAAA',verbose_name='Data de nascimento')

    def __str__(self):
        return self.nome

