# Программа сервера для получения приветствия от клиента и отправки ответа
from socket import *
import json
import sys
from utils import send_message, get_message

DEFAULT_PORT = 7777
MAX_CONNECTIONS = 5


def answer_from_server(responses):
    """
    Функция формирования сообщения от сервера
    """

    msg = {
        "response": responses[0],
        "alert": responses[1],
    }
    return msg


def choice_response(msg):
    """
    Функция выбора соответствующего
    ответа на сообщение от клиента
    """

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
            print('Принято некорректное сообщение от клиента.')
            client.close()


if __name__ == '__main__':
    main()

