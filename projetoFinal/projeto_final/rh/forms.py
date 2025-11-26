# contato/forms.py
from django import forms
from .models import MensagemContato, Carrinhos

class ContatoModelForm(forms.ModelForm):
    class Meta:
        model = MensagemContato
        fields = ['nome', 'email', 'assunto', 'mensagem']
        widgets = {
            'nome': forms.TextInput(attrs={'placeholder': 'Seu nome completo', 'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'placeholder': 'seu-email@exemplo.com', 'class': 'form-control'}),
            'assunto': forms.TextInput(attrs={'placeholder': 'Assunto da mensagem', 'class': 'form-control'}),
            'mensagem': forms.Textarea(attrs={'rows': 5, 'placeholder': 'Digite sua mensagem...', 'class': 'form-control'}),
        }
        labels = {
            'nome': 'Nome Completo',
            'email': 'Seu E-mail',
        }


    
class CarrinhoModelForm(forms.ModelForm):
    
    class Meta:
        model = Carrinhos
        
        fields = ['nome', 'email', 'tel', 'cpf', 'endereco']

        widgets = {
            'nome': forms.TextInput(attrs={'placeholder': 'Seu nome completo', 'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'placeholder': 'seu-email@exemplo.com', 'class': 'form-control'}),
            'tel': forms.TextInput(attrs={'placeholder': 'Seu telefone', 'class': 'form-control'}),
            'cpf': forms.TextInput(attrs={'placeholder': 'Seu cpf', 'class': 'form-control'}),
            'endereco': forms.TextInput(attrs={'placeholder': 'Seu endereço', 'class': 'form-control'})
        }
        
        labels = {
            'nome': 'Nome Completo',
            'email': 'Seu E-mail',
            'tel': 'DDD + número',
            'cpf' : 'CPF',
            'endereco' : 'Endereço'
        }


