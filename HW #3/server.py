# Программа сервера для получения приветствия от клиента и отправки ответа
from socket import *
import time
import json
import sys

DEFAULT_PORT = 7777
MAX_CONNECTIONS = 5


# s = socket(AF_INET, SOCK_STREAM) # Создает сокет TCP
# s.bind(('', DEFAULT_PORT)) # Присваивает порт 7777
# s.listen(5) # Переходит в режим ожидания запросов;
#             # Одновременно обслуживает не более
#             # 5 запросов.

# answer = ''
# alert = 'Успешно'
# while True:
#     client, addr = s.accept() # Принять запрос на соединение
#     print(client)
#     print(addr)
#     print('-*-' * 20)
#     data = client.recv(1000000) # прием данных от клиента
#     print(data)
#     print(type(data))
#     print('-**-' * 15)
#     data_utf = data.decode('utf-8')
#     print(type(data_utf))
#     print('-***-' * 11)
#     data_json = json.loads(data_utf)
#     print(data_json)
#     print('-****-' * 8)
#     if data_json['action'] == 'presence':
#         answer = '200'
#     else:
#         answer = '400'
#         alert = 'Bad Request'
#
#     answer_msg = {
#         "response": answer,
#         "alert": alert,
#         }
#
#     # print('Сообщение: ', data, ', было отправлено клиентом: ', addr)
#     client.send(json.dumps(answer_msg).encode('utf-8')) # отправка сообщения клиенту
#     client.close() # закрытие соединения

def main():
    """
    Загрузка параметров командной строки, если нет параметров, то задаём значения по умолчанию.
    Сначала обрабатываем порт:
    server.py -p 8888 -a 127.0.0.1
    """

    try:
        if '-p' in sys.argv:
            listen_port = int(sys.argv[sys.argv.index('-p') + 1]) # слушает указзанный порт
        else:
            listen_port = DEFAULT_PORT # слушает порт 7777
        if listen_port < 1024 or listen_port > 65535: # проверка на доступные порты
            raise ValueError
    except IndexError:
        print('После параметра -\'p\' необходимо указать номер порта.') # обязательное указание после -p порта
        sys.exit(1)
    except ValueError:
        print('Номер порта может быть указано только в диапазоне от 1024 до 65535.')
        sys.exit(1)

    try:
        if '-a' in sys.argv:
            listen_address = sys.argv[sys.argv.index('-a') + 1] # слушает адрес указанный с параметрах
        else:
            listen_address = '' # слушает все адреса

    except IndexError:
        print(
            'После параметра \'a\'- необходимо указать адрес, который будет слушать сервер.')
        sys.exit(1)

    s = socket(AF_INET, SOCK_STREAM) # Создает сокет TCP
    s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    s.bind((listen_address, listen_port)) # Присваивает порт указанный в параметре либо DEFAULT_PORT
    s.listen(MAX_CONNECTIONS) # Переходит в режим ожидания запросов;
            # Одновременно обслуживает не более MAX_CONNECTIONS запросов

    while True:
        client, addr = s.accept()
        try:
            data = client.recv(1000000) # прием данных от клиента
            data_utf = data.decode('utf-8') # декодирование байтов в кодировку utf-8
            data_json = json.loads(data_utf) # загрузка словаря json

            if data_json['action'] == 'presence':
                answer = '200'
                alert = 'Succesful'
            else:
                answer = '400'
                alert = 'Bad Request'

            answer_msg = {
                "response": answer,
                "alert": alert,
            }

            # print('Сообщение: ', data, ', было отправлено клиентом: ', addr)
            client.send(json.dumps(answer_msg).encode('utf-8'))  # отправка сообщения клиенту
            client.close()
        except(ValueError, json.JSONDecodeError):
            print('Принято некорректное сообщение от клиента.')
            client.close()


if __name__ == '__main__':
    main()

