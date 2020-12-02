onload = function(e) {
  console.log("onload");
  // Pega mensagens a cada 5 segundos
  setInterval(pegaMensagens, 5000);
}

function pegaMensagens() {
    console.log("Buscando mensagens")
    var xmlhttp;
    xmlhttp = new XMLHttpRequest();
    xmlhttp.open('GET', '/chat/pegaMensagens', true);
    xmlhttp.onreadystatechange = function(e) {
      if(xmlhttp.readyState == 4 && xmlhttp.status == 200) {
        // TODO: terminar isso aqui
        console.log("Resposta = ", xmlhttp.responseText)
        var mensagens = JSON.parse(xmlhttp.responseText);
        // Verifica se existem mensagens, se não houver, nada a fazer...
        if(mensagens.length == 0) return;
        // Se eu estou aqui, é porque existem mensagens
        // Remover o texto "Sem mensagens"
        // E criar uma tabela com 3 colunas: Nick, Texto, IP
        var tabela = document.getElementById('idTableChat');
        var novaTabela = document.createElement('table');
        novaTabela.setAttribute('id', 'idTableChat');
        var tr, th, td;
        tr = document.createElement('tr');
        th = document.createElement('th');
        th.appendChild(document.createTextNode('Nickname'));
        tr.appendChild(th);
        th = document.createElement('th');
        th.appendChild(document.createTextNode('Texto'));
        tr.appendChild(th);
        th = document.createElement('th');
        th.appendChild(document.createTextNode('IP'));
        tr.appendChild(th);
        tabela.parentNode.replaceChild(novaTabela, tabela);
        novaTabela.appendChild(tr);
        for(var i in mensagens) {
          var mensagem = mensagens[i];
          tr = document.createElement('tr');
          // incluindo o nickname de uma mensagem
          td = document.createElement('td');
          td.appendChild(document.createTextNode(mensagem.nick));
          tr.appendChild(td);
          // incluindo o texto de uma mensagem
          td = document.createElement('td');
          td.appendChild(document.createTextNode(mensagem.texto));
          tr.appendChild(td);
          // incluindo o IP de uma mensagem
          td = document.createElement('td');
          td.appendChild(document.createTextNode(mensagem.ipAddress));
          tr.appendChild(td);
          novaTabela.appendChild(tr);
        }
      }
    };
    xmlhttp.send(null);
}
