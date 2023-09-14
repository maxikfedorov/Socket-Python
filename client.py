import socket

# Создаем сокет
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Получаем имя хоста и порт
host = socket.gethostname()
port = 12345

# Подключаемся к серверу
client_socket.connect((host, port))

# Получаем список задач от сервера
tasks = client_socket.recv(1024).decode()
print(tasks)

# Выбираем задачу
task_choice = int(input("Выберите задачу: "))

# Отправляем выбор задачи серверу
client_socket.sendall(str.encode(str(task_choice)))

# Обрабатываем выбор задачи и получаем ответ от сервера
if task_choice == 1:
    n = int(input("Введите натуральное число N: "))
    client_socket.sendall(str.encode(str(n)))
    result = client_socket.recv(1024).decode()
    print(result)
elif task_choice == 2:
    result = client_socket.recv(1024).decode()
    print(result)
elif task_choice == 3:
    result = client_socket.recv(1024).decode()
    print(result)

elif task_choice == 4:
    while True:
        x = float(input("Введите число x: "))
        client_socket.sendall(str.encode(str(x)))
        result = client_socket.recv(1024).decode()
        print(result)
        if result == "Число не входит в область определения функции.":
            break

elif task_choice == 5:
    n = int(input("Введите натуральное число N: "))
    client_socket.sendall(str.encode(str(n)))
    result = client_socket.recv(1024).decode()
    print(result)

# Закрываем соединение
client_socket.close()
