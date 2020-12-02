from django.urls.conf import path
from contatos import views

app_name = 'contatos'

urlpatterns = [
    path('apaga/<int:pk>/', views.ContatoDeleteView.as_view(), name='apaga-contato'),
    # http://www.meusite.com.br/contatos/atualiza/2134/
    path('atualiza/<int:pk>/', views.ContatoUpdateView.as_view(), name='atualiza-contato'),
    path('lista/', views.ContatoListView.as_view(),   name='lista-contato'),
    path('cria/',  views.ContatoCreateView.as_view(), name='cria-contato'),
    path('',       views.ContatoListView.as_view(),   name='home-contato'),
]
