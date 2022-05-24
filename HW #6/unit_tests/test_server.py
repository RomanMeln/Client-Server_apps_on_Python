"""Unit-тесты сервера"""

import sys
import os
import unittest
sys.path.append(os.path.join(os.getcwd(), '..'))  # команда для поиска(перехода) на уровень выше
from server import answer_from_server, choice_response


class TestServer(unittest.TestCase):
    """
    Тест коректного ответа
    """

    def test_answer_from_server(self):
        test = answer_from_server(('200', 'Succesful'))
        self.assertEqual(test, {"response": '200', "alert": 'Succesful'})

    def test_choice_response_good(self):
        """
        Тест функции выбора соответствующего
        ответа на сообщение от клиента
        """
        message = {
            "action": "presence",
            "time": 1.1,
        }

        test = choice_response(message)
        self.assertEqual(test, ('200', 'Succesful'))

    def test_choice_response_bed(self):
        """
        Тест функции выбора соответствующего
        ответа на сообщение от клиента
        """
        message = {
            "action": "error",
            "time": 1.1,
        }

        test = choice_response(message)
        self.assertEqual(test, ('400', 'Bad Request'))


if __name__ == '__main__':
    unittest.main()
