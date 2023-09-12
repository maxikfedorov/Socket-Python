import socket

def is_power_of_four(n):
    if n == 0:
        return False
    while n != 1:
        if n % 4 != 0:
            return False
        n = n // 4
    return True

HOST = '127.0.0.1'  # Локальный адрес
PORT = 65432        # Произвольный порт (можно выбрать любой свободный порт)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    with conn:
        print('Подключение клиента:', addr)
        while True:
            data = conn.recv(1024)
            if not data:
                break
            n = int(data.decode())
            result = is_power_of_four(n)
            conn.sendall(str(result).encode())
