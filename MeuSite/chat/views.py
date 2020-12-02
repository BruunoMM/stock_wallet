from django.shortcuts import render
from django.views.generic.base import View
from chat.forms import WelcomeForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.urls.base import reverse_lazy
from chat.forms import MensagemForm
from chat.models import Mensagem, Mensagens
import json
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

# Create your views here.
def verificaCookies(request):
    request.session.set_test_cookie()
    return render(request, 'chat/paginaTemporaria.html', context=None)

'''
Verifica se o navegador aceita cookies
'''
class ChatInicio(LoginRequiredMixin, View):
    '''
    Verifica se o cookie de teste voltou
    Se voltou, então redireciona para o chat
    caso contrário, exibe uma página explicando ao usuário
    que ele deve habilitar os cookies
    '''
    def get(self, request, *args, **kwargs):
        if request.session.test_cookie_worked():
            # cookie habilitado
            # não preciso mais do cookie de teste
            request.session.delete_test_cookie()
            # exibir o formulário para obter o nickname...
            context = {'form' : WelcomeForm,}
            return render(request, 'chat/nickname.html', context=context)
        else:
            # sem cookie
            return render(request, 'chat/semCookies.html', context=None)

    def post(self, request, *args, **kwargs):
        form = WelcomeForm(request.POST)
        if form.is_valid():
            # aqui começa a sessão do chat
            request.session['nick'] = form.cleaned_data['nick']
            return HttpResponseRedirect(reverse_lazy('chat-conversacao'))
        else:
            # algum problema com o nickname
            context = {'form' : form,}
            return render(request, 'chat/nickname.html', context=context)

'''
Implementa a conversação do chat
Exibe as mensagens
Recebe a mensagem do usuário
Inclui a nova mensagem do usuário na lista de mensagens
'''
class ChatConversacao(LoginRequiredMixin, View):
    '''
    Apenas exibe as mensagens
    e o formulário para o usuário entrar com um novo texto
    '''
    def get(self, request, *args, **kwargs):
        form = MensagemForm
        nick = request.session.get('nick', 'Sem nickname')
        context = {
            'form' : form,
            'nick' : nick,
        }
        return render(request, 'chat/chat.html', context=context)

    '''
    Recebe o formulário com o novo texto
    Inclui o novo texto na lista de mensagens
    Exibe as mensagens e o formulário de texto
    '''
    def post(self, request, *args, **kwargs):
        '''
        Recebe a mensagem via post
        Validar a mensagem (o formulário)
        Criar um objeto Mensagem com nick, texto, ip
        Colocar o objeto Mensagem em uma lista de Mensagens
        onde Mensagens é um objeto global de toda a aplicação!!!
        '''
        form = MensagemForm(request.POST)
        if form.is_valid():
            # o nickname vem da sessão
            nick = request.session.get('nick', 'Sem nickname')
            # o texto vem do formulário
            texto = form.cleaned_data['texto']
            # o endereço IP do cliente vem junto com o pedido
            ip = request.META['REMOTE_ADDR']
            mensagem = Mensagem()
            mensagem.nick = nick
            mensagem.texto = texto
            mensagem.ipAddress = ip
            Mensagens.addMensagem(mensagem)
        context = {'form' : MensagemForm, 'nick' : nick,}
        return render(request, 'chat/chat.html', context=context)

@login_required
def pegaMensagens(request):
    # texto em formato JSON com a lista de mensagens
    mensagens = json.dumps(Mensagens.getMensagens(), default=lambda obj: obj.__dict__)
    print("Mensagens =", mensagens)
    return HttpResponse(mensagens)
