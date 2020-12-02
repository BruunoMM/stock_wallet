from django.db import models
import threading

# Create your models here.

'''
Representa UMA mensagem
'''
class Mensagem(models.Model):
    nick = models.CharField(max_length=30, help_text='Entre com o seu nickname')
    texto = models.CharField(max_length=100, help_text='Digite a mensagem')
    ipAddress = models.GenericIPAddressField()

'''
Representa uma lista de mensagens
Lista global de mensagens (para toda a aplicação, a mesma lista)
'''
class Mensagens(models.Model):
    # variável de classe que *NÃO* deve ser utilizada fora da classe
    _listaMensagens = list()
    _listaMensagens_lock = threading.Lock()

    # Esse é um método de classe
    # ele pode ser usado sem que eu precise criar um objeto dessa classe
    @classmethod
    def addMensagem(self, mensagem):
        # sempre que uma variável global for modificada,
        # os comandos de modificação devem ficar dentro de uma região crítica
        self._listaMensagens_lock.acquire()
        self._listaMensagens.append(mensagem)
        self._listaMensagens_lock.release()
        return

    # Esse é um método de classe
    # ele pode ser usado sem que eu precise criar um objeto dessa classe
    @classmethod
    def getMensagens(self):
        return self._listaMensagens
