import socket

HOST = '127.0.0.1'  # Локальный адрес сервера
PORT = 65432        # Тот же порт, что и у сервера

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    n = input('Введите число: ')
    s.sendall(n.encode())
    data = s.recv(1024)
    print('Ответ сервера:', data.decode())
