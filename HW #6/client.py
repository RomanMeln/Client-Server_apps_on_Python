# Программа клиента для отправки приветствия серверу и получения ответа
import time
from socket import *
import sys
import json
import logging
import logs.client_log_config
from utils import send_message, get_message
from decorator_log import log

ACTIONS = "presence"
DEFAULT_IP_ADDRESS = '127.0.0.1'
DEFAULT_PORT = 7777


# Создаем новый объект класса Logger с помощью следующей функции:
CLIENT_LOGGER = logging.getLogger('client')


@log
def msg_for_server():
    message = {
        "action": ACTIONS,
        "time": time.time(),
    }
    CLIENT_LOGGER.debug(f'Формирование сообщения на сервер: {message}')
    return message


def main():
    """Загружаем параметы коммандной строки"""
    try:
        server_address = sys.argv[1]
        server_port = int(sys.argv[2])
        CLIENT_LOGGER.info(f'адрес: {server_address}, порт: {server_port}')
        if server_port < 1024 or server_port > 65535:
            CLIENT_LOGGER.critical(f'Попытка запуска сервера с указанием неподходящего порта '
                                   f'{server_port}. Допустимы адреса с 1024 до 65535.')
            raise ValueError
    except IndexError:
        server_address = DEFAULT_IP_ADDRESS
        server_port = DEFAULT_PORT
    except ValueError:
        CLIENT_LOGGER.critical('В качестве порта может быть указано только число в диапазоне от 1024 до 65535.')
        # print('В качестве порта может быть указано только число в диапазоне от 1024 до 65535.')
        sys.exit(1)

    client_socket = socket(AF_INET, SOCK_STREAM) # Создать сокет TCP
    client_socket.connect((server_address, server_port))  # Соединиться с сервером
    message = msg_for_server() # создание сообщения
    send_message(client_socket, message)  # используем функцию для отправки сообщения

    try:
        answer = get_message(client_socket) # получаем сообщение
        print('Сообщение от сервера: ', answer['response'], ':', answer['alert']) # выводим ответ
    except (ValueError, json.JSONDecodeError):
        CLIENT_LOGGER.error('Не удалось декодировать сообщение сервера.')
        # print('Не удалось декодировать сообщение сервера.')


if __name__ == '__main__':
    main()
