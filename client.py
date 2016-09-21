from socket import *
import sys
import openpyxl
import matplotlib.pyplot as plt

wb = openpyxl.load_workbook(filename = 'obj.xlsx')
sheet = wb['1']
#считываем значение определенной ячейки
val = sheet['A2'].value
#считываем заданный диапазон
X = [v[0].value for v in sheet.range('A1:A10')]
Y = [v[0].value for v in sheet.range('C1:C10')]

host = 'localhost'
port = 777
addr = (host,port)

tcp_socket = socket(AF_INET, SOCK_STREAM)
tcp_socket.connect(addr)

data = str(X+Y)
print ('output: ',data)

#encode - перекодирует введенные данные в байты, decode - обратно
data = str.encode(data)
tcp_socket.send(data)
data = bytes.decode(data)
data = tcp_socket.recv(10240)
#print('input: ',data)
plt = open('graf.png','wb')
plt.write(data)
plt.close()
#plt.show()


tcp_socket.close()
