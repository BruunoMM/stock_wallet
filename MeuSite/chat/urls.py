from chat import views
from django.urls.conf import path

urlpatterns = [
    # home page do chat
    path('', views.verificaCookies, name='chat-home'),
    path('inicio/', views.ChatInicio.as_view(), name='chat-inicio'),
    path('conversacao/', views.ChatConversacao.as_view(), name='chat-conversacao'),
    path('pegaMensagens/', views.pegaMensagens, name='chat-pegaMensagens'),
]
