from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import JsonResponse

# Homepage de controle de acesso
def homeSec(request):
    return render(request, "registro/homeSec.html")

'''
Permite criar um usuário
Se o método for GET, cria o formulário para criar o usuário
Se o método for POST, pega os dados do formulário e cria um usuário
'''
def registro(request):
    if request.method == 'POST':
        # cria um usuário
        formulario = UserCreationForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect('sec-home')
        else:
            context = {'form' : formulario, }
            return render(request, 'registro/registro.html', context)
    else:
        # mostra o formulário
        formulario = UserCreationForm()
        context = {'form' : formulario, }
        return render(request, 'registro/registro.html', context)

# Pagina pagina
# Somente usuários autenticados podem ver
@login_required
def paginaSecreta(request):
    return render(request, 'registro/paginaSecreta.html')

'''
Recebe um pedido de verificacã́o com um username
Procurar no banco de dados o username
Retorna:
    - verdadeiro se o username existir no bd
'''
def verificaUsername(request):
        # obtem o username do formulário (o campo é 'username')
        # GET -> dicionário com todos os campos do formulário (HTTP)
        # get -> método usado para acessar uma entrada de qualquer dicionário
        username = request.GET.get('username', None)
        # consultar o banco de dados
        # preciso saber se o username está no banco
        # username= -> parâmetro de filter
        # =username -> variável criada algumas linhas antes
        existe = User.objects.filter(username__iexact=username).exists()
        # prepara uma resposta
        resposta = {
            # 'existe' -> chave do dicionário da resposta
            # : existe -> variável criada algumas linhas antes (verdadeiro ou falso)
            'existe' : existe,
            'mensagem' : "Esse usuário já existe" if existe else "Esse usário ainda não existe",
            'cor' : "#ff0000" if existe else "#000000",
        }
        # envia a resposta ao cliente (browser)
        return JsonResponse(resposta)
