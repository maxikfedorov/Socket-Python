import socket
import threading
import math

# Функция для обработки каждого нового подключения в отдельном потоке
def handle_client(client_socket):
    # Уведомляем о подключении клиента
    print(f"Подключился клиент {client_socket.getpeername()}")

    # Отправляем клиенту список задач
    tasks = ["1. Определить, является ли натуральное N степенью числа 4 или нет.",
             "2. Вывести на печать положительные значения функции y=sin(x)+5cos(x-2) для x изменяющегося на отрезке [-5, 12] с шагом 1,2.",
             "3. Вывести на печать значения функции z=ln(x)+tg(2x), большие 1, для x изменяющегося на отрезке [3, 8] с шагом 0,9.",
             "4. Напечатать значения функции y=ln(x-1/x),где значения x вводятся с клавиатуры. При вводе числа,не входящего в область определения функции, вычисления прекратить.",
             "5. Дано натуральное число N. Получить наименьшее число вида 4k, большее N"]
    client_socket.sendall(str.encode("\n".join(tasks)))

    # Бесконечный цикл для обработки нескольких задач подряд
    while True:
        # Получаем выбор задачи от клиента
        try:
            task_choice = int(client_socket.recv(1024).decode())
        except ValueError:
            # Если клиент закрыл соединение, то выходим из цикла
            break

        # Обрабатываем выбор задачи и отправляем ответ клиенту
        if task_choice == 1:
            n = int(client_socket.recv(1024).decode())
            is_power_of_4 = False
            while n % 4 == 0:
                n //= 4
                if n == 1:
                    is_power_of_4 = True
                    break
            client_socket.sendall(str.encode(str(is_power_of_4)))
            # Уведомляем об успешном решении задачи
            print(f"Клиент {client_socket.getpeername()} решил задачу 1")
        elif task_choice == 2:
            x = -5
            result = []
            while x <= 12:
                y = round(math.sin(x) + 5 * math.cos(x - 2), 2)
                if y > 0:
                    result.append(str(y))
                x += 1.2
            client_socket.sendall(str.encode("\n".join(result)))
            # Уведомляем об успешном решении задачи
            print(f"Клиент {client_socket.getpeername()} решил задачу 2")
        elif task_choice == 3:
            x = 3
            result = []
            while x <= 8:
                z = math.log(x) + math.tan(2 * x)
                if z > 1:
                    result.append(str(z))
                x += 0.9
            client_socket.sendall(str.encode("\n".join(result)))
            # Уведомляем об успешном решении задачи
            print(f"Клиент {client_socket.getpeername()} решил задачу 3")
        elif task_choice == 4:
            while True:
                try:
                    x = float(client_socket.recv(1024).decode())
                except ValueError:
                    # Если клиент закрыл соединение, то выходим из цикла
                    break
                if x <= 1:
                    client_socket.sendall(str.encode("Число не входит в область определения функции."))
                else:
                    y = math.log(x - 1 / x)
                    client_socket.sendall(str.encode(str(y)))
                    # Уведомляем об успешном решении задачи
                    print(f"Клиент {client_socket.getpeername()} решил задачу 4")
                if x <= 1:
                    break            
        elif task_choice == 5:
            n = int(client_socket.recv(1024).decode())
            k = 1
            while True:
                if 4 * k > n:
                    client_socket.sendall(str.encode(str(4 * k)))
                    break
                k += 1
            # Уведомляем об успешном решении задачи
            print(f"Клиент {client_socket.getpeername()} решил задачу 5")

    # Уведомляем об отключении клиента
    print(f"Клиент {client_socket.getpeername()} отключился")

    # Закрываем соединение
    client_socket.close()

# Создаем сокет
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Получаем имя хоста и порт
host = socket.gethostname()
port = 12345

# Привязываем сокет к хосту и порту
server_socket.bind((host, port))

# Слушаем входящие соединения
server_socket.listen(5)

# Уведомляем об успешном запуске сервера
print(f"Сервер запущен на {host}:{port}")

# Бесконечный цикл для обработки каждого нового подключения в отдельном потоке
while True:
    # Ожидаем подключения клиента
    client_socket, addr = server_socket.accept()

    # Создаем новый поток для обработки подключения
    client_thread = threading.Thread(target=handle_client, args=(client_socket,))
    client_thread.start()
