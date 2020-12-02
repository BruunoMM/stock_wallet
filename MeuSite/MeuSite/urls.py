"""MeuSite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.urls import include
from . import views
from django.contrib.auth.views import LoginView, LogoutView
from django.urls.base import reverse_lazy
from django.contrib.auth.views import PasswordChangeView, PasswordChangeDoneView
from django.views.generic.edit import UpdateView
from django.contrib.auth.models import User
from django.contrib.auth.views import PasswordResetView
from django.contrib.auth.views import PasswordResetConfirmView
from django.contrib.auth.views import PasswordResetDoneView

urlpatterns = [
    path('admin/', admin.site.urls),
    # incluir minhas novas URLs
    # se o endereço (URL) for do tipo www.meusite.com.br/constatos/<alguma coisa aqui>
    # exemplo: www.meusite.com.br/constatos/lista ==> lista está sendo tratado em contatos.urls
    path('contatos/', include('contatos.urls')),
    path('chat/', include('chat.urls')),
    # Caminhos para controle de acesso
    # As classas de controle de acesso usam a URL accounts
    path('', views.homeSec, name='sec-home'),
    path('accounts/', views.homeSec, name='sec-home'),
    path('accounts/registro', views.registro, name='sec-registro'),
    # login
    path('accounts/login/',
         LoginView.as_view(template_name='registro/login.html'),
         name='sec-login'),
    path('accounts/profile/', views.paginaSecreta, name='sec-paginaSecreta'),
    # logout
    path('accounts/logout/',
         LogoutView.as_view(next_page=reverse_lazy('sec-home')),
         name='sec-logout'),
    # Troca senha (depois de fazer login)
    # link para trocar a senha
    path('accounts/password-change/',
         PasswordChangeView.as_view(template_name='registro/password_change_form.html',
                                    success_url=reverse_lazy('sec-password_change_done')
         ),
         name='sec-password-change'),
    # link de sucesso de troca de senha
    path('accounts/password_change_done',
         PasswordChangeDoneView.as_view(template_name='registro/password_change_done.html'),
         name='sec-password_change_done'
    ),
    # link para o usuário terminar o seu Registro
    path('accounts/updateView/<int:pk>/',
         UpdateView.as_view(
            template_name='registro/user_form.html',
            success_url=reverse_lazy('sec-paginaSecreta'),
            model=User,
            fields=[
                'first_name',
                'last_name',
                'email',
            ]
         ),
         name='sec-updateView'
    ),
    # link para iniciar o reset da Senha
    path('accounts/password_reset/',
         PasswordResetView.as_view(
            template_name='registro/password_reset_form.html',
            success_url=reverse_lazy('sec-password_reset_done'),
            from_email='webmaster_do_site@aqui.com.br',
            subject_template_name='registro/password_reset_subject.txt',
            email_template_name='registro/password_reset_email.html',
         ),
         name='sec-password_reset'),
    path('accounts/password_reset_done/',
         PasswordResetDoneView.as_view(
            template_name='registro/password_reset_done.html'
         ),
         name='sec-password_reset_done'
    ),
    path('accounts/password_reset_confirm/<uidb64>/<token>/',
         PasswordResetConfirmView.as_view(
            template_name='registro/password_reset_confirm.html',
            success_url=reverse_lazy('sec-password_reset_complete'),
         ),
         name='password_reset_confirm'
    ),
    path('accounts/verificaUsername', views.verificaUsername, name='sec-verificaUsername'),
]
