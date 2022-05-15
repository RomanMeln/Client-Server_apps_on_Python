# Программа сервера для получения приветствия от клиента и отправки ответа
from socket import *
import json
import sys
import logging
import logs.server_log_config
from utils import send_message, get_message
from decorator_log import log

DEFAULT_PORT = 7777
MAX_CONNECTIONS = 5

# Создаем новый объект класса Logger с помощью следующей функции:
SERVER_LOGGER = logging.getLogger('server')


@log
def answer_from_server(responses):
    """
    Функция формирования сообщения от сервера
    """
    SERVER_LOGGER.debug('Формирования сообщения от сервера')
    msg = {
        "response": responses[0],
        "alert": responses[1],
    }
    return msg


@log
def choice_response(msg):
    """
    Функция выбора соответствующего
    ответа на сообщение от клиента
    """
    SERVER_LOGGER.debug(f'Выбор ответа на сообщение клиента : {msg}')
    if msg['action'] == 'presence':
        answer = '200'
        alert = 'Succesful'
    else:
        answer = '400'
        alert = 'Bad Request'
    return answer, alert


def main():
    """
    Загрузка параметров командной строки, если нет параметров, то задаём значения по умолчанию.
    Сначала обрабатываем порт:
    server.py -p 8888 -a 127.0.0.1
    """

    try:
        if '-p' in sys.argv:
            listen_port = int(sys.argv[sys.argv.index('-p') + 1]) # слушает указзанный порт
            SERVER_LOGGER.info(f'Слушаем порт : {listen_port}')
        else:
            listen_port = DEFAULT_PORT # слушает порт 7777
            SERVER_LOGGER.info(f'Слушаем порт по умолчанию : {listen_port}')
        if listen_port < 1024 or listen_port > 65535: # проверка на доступные порты
            SERVER_LOGGER.critical(f'Попытка запуска сервера с указанием неподходящего порта '
                                   f'{listen_port}. Допустимы адреса с 1024 до 65535.')
            raise ValueError
    except IndexError:
        SERVER_LOGGER.warning('Внимание! После параметра "-p" необходимо обязательно указать номер порта.')
        # print('После параметра -\'p\' необходимо обязательно указать номер порта.') # обязательное указание после -p порта
        sys.exit(1)
    except ValueError:
        SERVER_LOGGER.warning('Номер порта может быть указан только в диапазоне от 1024 до 65535.')
        # print('Номер порта может быть указано только в диапазоне от 1024 до 65535.')
        sys.exit(1)

    try:
        if '-a' in sys.argv:
            listen_address = sys.argv[sys.argv.index('-a') + 1] # слушает адрес указанный с параметрах
            SERVER_LOGGER.info(f'Слушаем адрес указанный с параметрах : {listen_address}')
        else:
            listen_address = '' # слушает все адреса
            SERVER_LOGGER.info('Слушаем все доступные адреса')

    except IndexError:
        SERVER_LOGGER.warning('После параметра "-a" - необходимо указать адрес, который будет слушать сервер.')
        # print(
        #     'После параметра \'-a\'- необходимо указать адрес, который будет слушать сервер.')
        sys.exit(1)

    socket_server = socket(AF_INET, SOCK_STREAM) # Создает сокет TCP
    socket_server.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    socket_server.bind((listen_address, listen_port)) # Присваивает порт указанный в параметре либо DEFAULT_PORT
    socket_server.listen(MAX_CONNECTIONS) # Переходит в режим ожидания запросов;
            # Одновременно обслуживает не более MAX_CONNECTIONS запросов

    while True:
        client, addr = socket_server.accept()
        try:
            data = get_message(client)
            response_msg = choice_response(data) # получаем кортеж данных для ответа
            answer_msg = answer_from_server(response_msg) # формируем ответ для клиента
            send_message(client, answer_msg) # используем функцию для отправки сообщения
            client.close()
        except(ValueError, json.JSONDecodeError):
            SERVER_LOGGER.error('Принято некорректное сообщение от клиента.')
            # print('Принято некорректное сообщение от клиента.')
            client.close()


if __name__ == '__main__':
    main()

