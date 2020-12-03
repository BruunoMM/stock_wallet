from django import forms
from stocks.models import Ativo

class Ativo2Form(forms.ModelForm):
    date = forms.DateField(input_formats=['%d/%m/%Y'], label='Data da compra')
    class Meta:
        model = Ativo

        fields = ('ticker', 'amount', 'price', 'date')
