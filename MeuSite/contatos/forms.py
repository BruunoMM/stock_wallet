from django import forms
from contatos.models import Pessoa


# Formulário para inserir um contato (no banco de dados)
class ContatoModel2Form(forms.ModelForm):
    dtNasc = forms.DateField(input_formats=['%d/%m/%Y'], label='Data do nascimento')
    class Meta:
        # usando o modelo Pessoa
        model = Pessoa
        # criar um formulário usando TODOS os campos
        fields = '__all__'
