from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

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