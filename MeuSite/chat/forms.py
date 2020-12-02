from django import forms
from chat.models import Mensagem

class WelcomeForm(forms.ModelForm):
    class Meta():
        model = Mensagem
        fields = ['nick',]

class MensagemForm(forms.ModelForm):
    class Meta():
        model = Mensagem
        fields = ["texto",]
        
