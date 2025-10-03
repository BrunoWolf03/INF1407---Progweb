from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from django import forms
import re
from .models import Jogador, Partida

class JogadorForm(forms.ModelForm):
    dtNasc = forms.DateField(
        label="Data de nascimento",
        input_formats=["%d/%m/%Y", "%Y-%m-%d"],
        widget=forms.DateInput(format="%d/%m/%Y", attrs={"placeholder": "DD/MM/AAAA"})
    )

    class Meta:
        model = Jogador
        fields = ["nome", "curso", "periodo", "email", "vitorias", "derrotas", "imagem", "dtNasc"]

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True, help_text="Informe um e-mail válido.")

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def clean_email(self):
        email = self.cleaned_data.get("email")
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("Este e-mail já está em uso.")
        return email

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user




import re
from django import forms
from .models import Partida, Jogador

class PartidaForm(forms.ModelForm):
    vencedor = forms.ModelChoiceField(queryset=Jogador.objects.none(), label="Vencedor")
    perdedor = forms.ModelChoiceField(queryset=Jogador.objects.none(), label="Perdedor")
    pontos = forms.CharField(max_length=10, help_text="Formato: N x J")

    class Meta:
        model = Partida
        fields = ['vencedor', 'perdedor', 'pontos']

    def __init__(self, *args, **kwargs):
        # Recebe os dois jogadores como kwargs
        jogador1 = kwargs.pop('jogador1', None)
        jogador2 = kwargs.pop('jogador2', None)
        super().__init__(*args, **kwargs)

        if jogador1 and jogador2:
            # Limita as opções de vencedor e perdedor aos dois jogadores
            self.fields['vencedor'].queryset = Jogador.objects.filter(id__in=[jogador1.id, jogador2.id])
            self.fields['perdedor'].queryset = Jogador.objects.filter(id__in=[jogador1.id, jogador2.id])

    def clean_pontos(self):
        pontos = self.cleaned_data.get('pontos', '')
        if not re.match(r'^\d+\s*x\s*\d+$', pontos):
            raise forms.ValidationError("O formato deve ser 'N x J', por exemplo 12 x 7")
        return pontos

    def clean(self):
        cleaned_data = super().clean()
        vencedor = cleaned_data.get('vencedor')
        perdedor = cleaned_data.get('perdedor')

        if vencedor and perdedor and vencedor == perdedor:
            raise forms.ValidationError("Vencedor e perdedor não podem ser o mesmo jogador.")