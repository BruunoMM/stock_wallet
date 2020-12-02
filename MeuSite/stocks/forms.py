from django import forms
from stocks.models import Ativo

# Formulário para inserir um contato (no banco de dados)
class Ativo2Form(forms.ModelForm):
    date = forms.DateField(input_formats=['%d/%m/%Y'], label='Data da compra')
    class Meta:
        # usando o modelo Pessoa
        model = Ativo
        # criar um formulário usando TODOS os campos
        fields = '__all__'
