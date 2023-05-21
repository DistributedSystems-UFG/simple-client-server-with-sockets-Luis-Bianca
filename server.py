from socket import *
from constCS import *  # -

s = socket(AF_INET, SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(1)
msg = ''
print('Servidor Iniciado')
(conn, addr) = s.accept()  # returns new socket and addr. client
while True:  # forever
    data = conn.recv(1024)  # receive data from client
    msg = data.decode()
    if not data: break  # stop if client stopped
    if msg == "fim":
        print("Fim da conexao")
        break
    tipo = msg.split()
    result = 0
    if tipo[1] == "+":
        result = float(tipo[0]) + float(tipo[2])
    elif tipo[1] == "-":
        result = float(tipo[0]) - float(tipo[2])
    elif tipo[1] == "*":
        result = float(tipo[0]) * float(tipo[2])
    elif tipo[1] == "/":
        result = float(tipo[0]) / float(tipo[2])
    else:
        result = 'Tipo Invalido'
    print('Enviando Resposta')
    output = str(result)
    conn.send(str.encode(output))  # return sent data plus an "*"
conn.close()  # close the connection
