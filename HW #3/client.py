# Программа клиента для отправки приветствия серверу и получения ответа
import time
from socket import *
import sys
import json

ACTIONS = "presence"
DEFAULT_IP_ADDRESS = '127.0.0.1'
DEFAULT_PORT = 7777

# s = socket(AF_INET, SOCK_STREAM) # Создать сокет TCP
# s.connect(('localhost', DEFAULT_PORT)) # Соединиться с сервером
# msg = {
#     "action": ACTIONS,
#     "time": time.time(),
#     }
#
#
# s.send(json.dumps(msg).encode('utf-8')) # отправка сообщения json в строке с кодировкой
# data = s.recv(1000000) # прием данных от сервера в байтах
# data_utf = data.decode('utf-8') # декодирование данных с сервера
# print(type(data_utf))
# data_json = json.loads(data_utf) # перевод данных из строки в словарь
# print(type(data_json))
# print('Сообщение от сервера: ', data_json)
# s.close() # закрыть соединение

def main():
    """Загружаем параметы коммандной строки"""
    try:
        server_address = sys.argv[1]
        server_port = int(sys.argv[2])
        if server_port < 1024 or server_port > 65535:
            raise ValueError
    except IndexError:
        server_address = DEFAULT_IP_ADDRESS
        server_port = DEFAULT_PORT
    except ValueError:
        print('В качестве порта может быть указано только число в диапазоне от 1024 до 65535.')
        sys.exit(1)

    s = socket(AF_INET, SOCK_STREAM) # Создать сокет TCP
    s.connect((server_address, server_port))  # Соединиться с сервером
    msg = {
        "action": ACTIONS,
        "time": time.time(),
    }
    s.send(json.dumps(msg).encode('utf-8'))  # отправка сообщения json в строке с кодировкой
    try:
        data = s.recv(1000000)  # прием данных от сервера в байтах
        data_utf = data.decode('utf-8')  # декодирование данных с сервера
        data_json = json.loads(data_utf)  # перевод данных из строки в словарь
        print('Сообщение от сервера: ', data_json)
        s.close()  # закрыть соединение
    except (ValueError, json.JSONDecodeError):
        print('Не удалось декодировать сообщение сервера.')


if __name__ == '__main__':
    main()
