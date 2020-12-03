from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Ativo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    ticker = models.CharField(max_length=10, help_text='Digite o ticker do ativo')
    amount = models.IntegerField(help_text='Digite a quantidade a ser adicionada')
    price = models.DecimalField(decimal_places=2, max_digits=10, help_text='Digite o preço de compra')
    date = models.DateField(verbose_name='Data de Compra', help_text='Digite a data de compra DD/MM/AAAA', auto_now=False, auto_now_add=False)
    
