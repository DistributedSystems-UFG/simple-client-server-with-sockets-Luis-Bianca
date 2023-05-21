from socket import *
from constCS import *  # -

s = socket(AF_INET, SOCK_STREAM)
s.connect((HOST, PORT))  # connect to server (block until accepted)
print('Informe uma operação com dois numeros (soma, sub, mult e div. obs.: separando por espaço) ou digite "fim" para finalizar: ')
while True:
    msg = input()
    if msg == "fim":
        break
    s.send(str.encode(msg))  # send some data
    data = s.recv(1024)  # receive the response
    print(bytes.decode(data))  # print the result
s.close()  # close connection
