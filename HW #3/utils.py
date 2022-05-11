"""Утилиты"""

import json


def get_message(client):
    """
    Утилита приёма и декодирования сообщения.
    Принимает байты, выдаёт словарь, если принято что-то
    другое возвращает ValueError (ошибку значения)
    """

    encoded_response = client.recv(1024) # прием данных
    if isinstance(encoded_response, bytes): # проверка принадлежности
        json_response = encoded_response.decode("utf-8") # декодирование байтов в кодировку utf-8. Строка.
        if isinstance(json_response, str): # проверка принадлежности
            response = json.loads(json_response) # загрузка словаря json
            if isinstance(response, dict): # проверка принадлежности
                return response
            raise ValueError
        raise ValueError
    raise ValueError


def send_message(sock, message):
    """
    Утилита кодирования и отправки сообщения:
    принимает для отправки словарь, получает из него строку,
    далее превращает строку в байты и отправляет.
    """
    if not isinstance(message, dict):
        raise TypeError
    js_message = json.dumps(message)
    encoded_message = js_message.encode("utf-8")
    sock.send(encoded_message)
