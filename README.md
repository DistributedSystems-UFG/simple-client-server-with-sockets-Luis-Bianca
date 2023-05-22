[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-24ddc0f5d75046c5622901739e7c5dd533143b0c8e959d652212380cedb1ea36.svg)](https://classroom.github.com/a/pmCXrCMx)
# ClientServerBasics (2.0)
Starter code for the basic client-server assignment


Este template corresponde ao exemplo da Fig. 2.3 do livro. O exercício consiste em acrescentar funcionalidade ao servidor para torná-lo mais útil. Essa funcionalidade deve ser acessível aos clientes. Por exemplo, o servidor pode ser uma espécie de calculadora remota. O cliente passa dois valores numéricos, juntamente com o nome de uma operação (ex.: add, subtract, multiply, divide) e o servidor executa a operação respectiva e retorna seu resultado para o cliente. Você pode implementar outro tipo de servidor (diferente da calculadora). O imporante é que ele ofereça pelo menos três operações diferentes que os clientes podem utilizar remotamente, passando dados para serem processados e recebendo o resultado desse processamento como resposta.

Tarefa individual.

Incluir um Readme descritivo do sistema implementado.

#

# Calculadora com Comunicação por Socket

Este repositório contém a implementação de uma calculadora simples que se comunica por socket. A calculadora é capaz de realizar operações de soma, subtração, multiplicação e divisão.

## Funcionamento
O sistema consiste em dois arquivos principais: `client.py` e `server.py`. Esses arquivos devem ser executados em instâncias diferentes na Amazon Web Services (AWS). Além dos dois arquivos principais, temos o arquivo `constCS.py` onde estão as informações de HOST e PORT que são utilizadas tanto no cliente quanto no servidor.

### Comunicação por Socket
A comunicação por socket é uma forma de comunicação entre processos ou máquinas diferentes através de uma rede. Os sockets permitem que os processos se comuniquem trocando mensagens.

Neste sistema, utilizamos sockets para permitir a comunicação entre o cliente e o servidor. O cliente envia uma mensagem contendo a operação a ser realizada e os valores necessários, separados por espaços. Essa mensagem é enviada para o servidor, que a processa e retorna o resultado da operação para o cliente.

### Arquivos do Sistema
- `client.py`: Este arquivo é responsável por iniciar o cliente. Ele estabelece a conexão com o servidor, solicita que o usuário digite a operação e os valores, envia a mensagem para o servidor e imprime o resultado recebido.

- `server.py`: Este arquivo é responsável por iniciar o servidor. Ele aguarda a conexão do cliente, recebe a mensagem contendo a operação e os valores, realiza o cálculo correspondente e envia o resultado de volta para o cliente.

- `constCS.py`: Este arquivo contém o endereço IP e a PORTA da instância em que o servidor está sendo executado.

## Como utilizar
Para utilizar o sistema, siga as instruções abaixo:

1. Clone este repositório em seu ambiente local.

2. Execute o arquivo servidor.py em uma instância da AWS, certificando-se de fornecer o endereço IP correto no arquivo constCS.py.

3. Execute o arquivo cliente.py em outro ambiente, como sua máquina local ou outra instância da AWS. Certifique-se de ter o mesmo endereço IP da instância do servidor.

4. O cliente solicitará que você digite a operação (+, -, * e /) e os valores separados por espaços. Por exemplo, para realizar uma soma, digite: 2 + 2.

5. O servidor processará a mensagem recebida e enviará o resultado de volta para o cliente.

6. O cliente exibirá o resultado na tela.

## Considerações Finais
Este sistema de calculadora com comunicação por socket oferece uma maneira simples e eficiente de realizar operações matemáticas básicas entre um cliente e um servidor. Certifique-se de fornecer o endereço IP correto para que a comunicação ocorra corretamente.
