# core/forms.py
from django import forms
from .models import Jogador

class JogadorForm(forms.ModelForm):
    dtNasc = forms.DateField(
        label="Data de nascimento",
        input_formats=["%d/%m/%Y", "%Y-%m-%d"],
        widget=forms.DateInput(format="%d/%m/%Y", attrs={"placeholder": "DD/MM/AAAA"})
    )

    class Meta:
        model = Jogador
        fields = ["nome", "curso", "periodo", "email", "vitorias", "derrotas", "imagem", "dtNasc"]
