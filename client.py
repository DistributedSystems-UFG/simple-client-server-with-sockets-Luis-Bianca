from socket import *
from constCS import *  # -

s = socket(AF_INET, SOCK_STREAM)
s.connect((HOST, PORT))  # connect to server (block until accepted)
print('Informe uma equação (soma, sub, mult e div) de dois números ou digite "fim" para finalizar: ')
while True:
    msg = input()
    if msg == "fim" or msg == "FIM" or msg == "Fim":
        break
    s.send(str.encode(msg))  # send some data
    data = s.recv(1024)  # receive the response
    print(bytes.decode(data))  # print the result
s.close()  # close connection
