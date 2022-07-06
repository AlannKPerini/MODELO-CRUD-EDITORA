from django import forms

from core.models import Autor


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
