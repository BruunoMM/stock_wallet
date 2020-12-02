onload = function() {
  console.log('onload')
  // deveria ser change ou blur
  document.getElementById('id_username').addEventListener('keyup', verificaUsername);
}

function verificaUsername(e) {
  console.log('verificaUsername')
  // Recupera o campo username
  var campoUsername = document.getElementById('id_username');
  valorUsername = campoUsername.value;
  console.log('Campo username = ' + valorUsername)
  // prepara o pedido para o servidor
  // xmlhttp tem que ser variável global (nesse caso)
  // use uma função anônima no call back na próxima vez para evitar esse problema
  xmlhttp = new XMLHttpRequest();
  xmlhttp.open('GET',
    '/accounts/verificaUsername' + "?username=" + encodeURIComponent(valorUsername),
    true);
  xmlhttp.onreadystatechange = verificaUsernameCallBack;
  xmlhttp.send(null);
}

function verificaUsernameCallBack() {
  console.log("call back")
  if(xmlhttp.readyState == 4 && xmlhttp.status == 200) {
    var resposta = JSON.parse(xmlhttp.responseText)
    /*
    if(resposta.existe) {
      // username existe
      console.log('existe')
      document.
        getElementById('idErro').
        replaceChild(
          document.createTextNode("Esse usuário, " + valorUsername + ", já existe"),
          document.getElementById('idErro').firstChild);
      document.getElementById('id_username').style='border: 2px solid #FF0000;';
    }
    else {
      // username não existe
      console.log('não existe')
      document.
        getElementById('idErro').
        replaceChild(
          document.createTextNode("Esse usuário, " + valorUsername + ", não existe"),
          document.getElementById('idErro').firstChild);
    }
    */
    document.
      getElementById('idErro').
      replaceChild(
        document.createTextNode(resposta.mensagem),
        document.getElementById('idErro').firstChild);
    document.getElementById('id_username').style =
      'border: 2px solid ' + resposta.cor;
  }
}
