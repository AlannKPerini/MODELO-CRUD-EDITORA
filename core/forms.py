from django import forms

from core.models import Autor
from core.models import Cliente

class AutorForm(forms.ModelForm):
    class Meta:
        model = Autor
        # fields = ('nome''data_nascimento''email')
        exclude = ()
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nome Completo', 'autofocus': ''}),
            'data_nascimento': forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'dd/mm/aaaa'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'youremail@email.com'})
        }
class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        # fields = ('nome''data_nascimento''email')
        exclude = ()
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nome Completo', 'autofocus': ''}),
            'senha': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '******', 'autofocus': ''}),
            'cpf': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'somente números', 'autofocus': ''}),
            'endereco': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Endereço Completo', 'autofocus': ''}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'youremail@email.com'}),
            'sexo': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'M ou F', 'autofocus': ''})
        }