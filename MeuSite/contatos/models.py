from django.db import models

# Create your models here.

class Pessoa(models.Model):
    nome = models.CharField(max_length=100, help_text='Entre com o nome')
    idade = models.IntegerField(help_text='Entre com a idade')
    salario = models.DecimalField(decimal_places=2, max_digits=10, help_text='Entre com o salário')
    email = models.EmailField(max_length=100, help_text='Entre com o email')
    telefone = models.CharField(max_length=25, help_text='Entre com o telefone no formato +DDI (DDD) NNNNN-NNNN')
    dtNasc = models.DateField(verbose_name='Data de nascimento', help_text='Entre com a data de nascimento no formato DD/MM/AAAA')
    
