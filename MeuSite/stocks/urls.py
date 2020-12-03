from django.urls.conf import path
from stocks import views

app_name = 'stocks'

urlpatterns = [
    path('', views.AtivoListView.as_view(), name='home-ativos'),
    path('cadastra/', views.AtivoCreateView.as_view(), name='cadastra-ativo'), # C
    path('lista/', views.AtivoListView.as_view(),   name='lista-ativos'), # R
    path('atualiza/<int:pk>/', views.AtivoUpdateView.as_view(), name='atualiza-ativo'), # U
    path('deleta/<int:pk>/', views.AtivoDeleteView.as_view(), name='remove-ativo'), # D
]

# http://www.meusite.com.br/contatos/atualiza/2134/