# Программа клиента для отправки приветствия серверу и получения ответа
import time
from socket import *
import sys
import json
from utils import send_message, get_message


ACTIONS = "presence"
DEFAULT_IP_ADDRESS = '127.0.0.1'
DEFAULT_PORT = 7777


def msg_for_server():
    message = {
        "action": ACTIONS,
        "time": time.time(),
    }
    return message


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

    client_socket = socket(AF_INET, SOCK_STREAM) # Создать сокет TCP
    client_socket.connect((server_address, server_port))  # Соединиться с сервером
    message = msg_for_server() # создание сообщения
    send_message(client_socket, message)  # используем функцию для отправки сообщения

    try:
        answer = get_message(client_socket) # получаем сообщение
        print('Сообщение от сервера: ', answer['response'], ':', answer['alert']) # выводим ответ
    except (ValueError, json.JSONDecodeError):
        print('Не удалось декодировать сообщение сервера.')


if __name__ == '__main__':
    main()
