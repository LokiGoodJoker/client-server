#Модуль socket для сетевого программирования
from socket import *
import re
import matplotlib.pyplot as plt
#данные сервера
host = 'localhost'
port = 777
addr = (host,port)

#socket - функция создания сокета 
#первый параметр socket_family может быть AF_INET или AF_UNIX
#второй параметр socket_type может быть SOCK_STREAM(для TCP) или SOCK_DGRAM(для UDP)
tcp_socket = socket(AF_INET, SOCK_STREAM)
#bind - связывает адрес и порт с сокетом
tcp_socket.bind(addr)
#listen - запускает прием TCP
tcp_socket.listen(1)

#Бесконечный цикл работы программы
while True:
    
    #Если мы захотели выйти из программы
    question = input('Do you want to quit? y\\n: ')
    if question == 'y': break
    
   #print('wait connection...')
    
    #accept - принимает запрос и устанавливает соединение, (по умолчанию работает в блокирующем режиме)
    #устанавливает новый сокет соединения в переменную conn и адрес клиента в переменную addr
    conn, addr = tcp_socket.accept()
    print('client addr: ', addr)
    
    #recv - получает сообщение TCP
    data = conn.recv(1024)
    datax = bytes.decode(data)
    
    x = re.findall('(\d+)', datax)
    a = x
    i=0
    print (x[1])
    while i<20:
        a[i]=int(x[i])
        print ('x ',a[i])
        
        i=i+1

    X=a[0:10]
    Y=a[10:20]
    print('x= ',X,'y= ',Y)
    fig = plt.figure()   # Создание объекта Figure
    print (fig.axes)   # Список текущих областей рисования пуст
    print (type(fig))   # тип объекта Figure
    plt.scatter(X, Y)   
    plt.xlabel('X axes');
    plt.ylabel('Y axes');
# После нанесения графического элемента в виде маркера
# список текущих областей состоит из одной области
    print (fig.axes)

# смотри преамбулу
    plt.savefig('example.png', fmt='png')
    data = open('example.png','rb+')
    #datan = png.encode(data)
    #plt.show()
    
    #если ничего не прислали, завершим программу
    if not data:
        print('EROR')
        conn.close()
       
        break
    else:
        #print('output: ',data)
        #send - передает сообщение TCP
        conn.sendfile(data)
        #close - закрывает сокет
        conn.close()
    data.close()
tcp_socket.close()

