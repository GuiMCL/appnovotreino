

from django import forms
from django.db import models
from django.forms import fields, widgets
from django.forms.models import ModelForm
from django.utils.regex_helper import Choice

from .models import DepartamentoModel,FuncionarioModel

class FuncionarioCadastroForm(forms.ModelForm):

    class Meta:

        fields = ['departamento','nome','sobrenome','usuario','senha','superusuario']
        model = FuncionarioModel

    



class FuncionarioEdicaoForm(forms.ModelForm):

    
    """
        Verificamos que ao editar uma chave primaria, no caso é a senha do usuario, não é editado a senha
        mas é criado um novo usuario, por isso não colocamos a opcao de edição senha no formulario          
    """
    class Meta:

        fields = ['departamento','nome','sobrenome','usuario','superusuario']
        model = FuncionarioModel  

     

class LoginForm(forms.Form):

    usuario = forms.CharField(label='Usuário', max_length=100)
    senha = forms.CharField(label='Senha', max_length=12, widget=forms.PasswordInput())
  


class CadastrarDepartamentoForm(forms.ModelForm):

    class Meta:

        fields = ['sigla','nome']
        model = DepartamentoModel


