from django.shortcuts import render
from django.views.generic.base import View
from contatos.models import Pessoa
from contatos.forms import ContatoModel2Form
from django.http.response import HttpResponseRedirect
from django.urls.base import reverse_lazy
from django.shortcuts import get_object_or_404

# Create your views here.

class ContatoDeleteView(View):
    # Pergunta se vai apagar mesmo
    def get(self, request, pk, *args, **kwargs):
        pessoa = Pessoa.objects.get(pk=pk)
        context = {'pessoa' : pessoa,}
        return render(request, 'contatos/apagaContato.html', context)

    # Apaga mesmo!
    def post(self, request, pk, *args, **kwargs):
        pessoa = Pessoa.objects.get(pk=pk)
        pessoa.delete()
        return HttpResponseRedirect(reverse_lazy('contatos:lista-contato'))

class ContatoUpdateView(View):
    # o get recebe como parâmetro a chave primária pk
    # o pk identifica unicamente um registro no BD
    # Cria um formulário preenchido com os dados do BD
    def get(self, request, pk, *args, **kwargs):
        # pk=pk:
        # o 1o pk de pk=pk é o nome do parâmetro do método Pessoa.objects.get
        # o 2o pk de pk=pk é o nome do parâmetro que esse método get recebeu
        pessoa = Pessoa.objects.get(pk=pk)
        # cria um objeto formulário preenchido com os dados da pessoa do BD
        formulario = ContatoModel2Form(instance=pessoa)
        context = {'formulario' : formulario,}
        return render(request, 'contatos/atualizaContato.html', context)

    # Recebe um formulário preenchido e salva no BD, atualizando
    # Não pode criar um novo contato
    def post(self, request, pk, *args, **kwargs):
        pessoa = get_object_or_404(Pessoa, pk=pk)
        formulario = ContatoModel2Form(request.POST, instance=pessoa)
        if formulario.is_valid():
            pessoa = formulario.save()
            pessoa.save()
            return HttpResponseRedirect(reverse_lazy('contatos:lista-contato'))
        else:
            context = {'formulario' : formulario,}
            return render(request, 'contatos/atualizaContato.html', context)

class ContatoListView(View):
    def get(self, request, *args, **kwargs):
        # buscar todas as pessoas do banco de dados
        pessoas = Pessoa.objects.all()
        # dicionário de variáveis para o template
        context = {
            'pessoas': pessoas,
        }
        '''
        o template vai estar dentro do diretório contatos
        o template vai se chamar listaContatos.html
        '''
        return render(request, 'contatos/listaContatos.html', context)

# Exibe e salva um contato
class ContatoCreateView(View):
    # Exibe um formulário
    def get(self, request, *args, **kwargs):
        context = {'formulario' : ContatoModel2Form}
        return render(request, 'contatos/criaContatos.html', context)

    # Cria um contato com os dados do formulário no banco de dados
    def post(self, request, *args, **kwargs):
        # formulário representa os dados do formulário vindos via POST
        formulario = ContatoModel2Form(request.POST)
        if formulario.is_valid():
            # criar uma variável que representa o contato
            contato = formulario.save()
            # o contato ainda está somente em memória
            # vou salvar no banco de dados
            contato.save()
            # eu NÃO vou desviar para um template e sim para outro view
            # vai desviar para a URL lista-contato definida em contatos
            return HttpResponseRedirect(reverse_lazy('contatos:lista-contato'))
        else:
            return HttpResponseRedirect(reverse_lazy('contatos:cria-contato'))
