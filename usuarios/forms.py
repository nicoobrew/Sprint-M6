from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

class RegistroUsuarioForm(UserCreationForm):
    campos = (
        ('admin', 'administrador'),
        ('usuario_comun', 'usuario comun')
    )
    email = forms.EmailField(required=False)
    tipo_usuario = forms.ChoiceField(choices=campos) 
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'tipo_usuario']