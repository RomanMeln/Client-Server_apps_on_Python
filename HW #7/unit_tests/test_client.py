"""Unit-тесты клиента"""

import sys
import os
import unittest
sys.path.append(os.path.join(os.getcwd(), '..')) # команда для поиска(перехода) на уровень выше
from client import msg_for_server


class TestClass(unittest.TestCase):
    """
    Класс с тестами
    """

    def test_msg_for_server(self):
        """
        Тест коректного запроса
        """
        test = msg_for_server()
        test["time"] = 1.1  # время необходимо приравнять принудительно
                          # иначе тест никогда не будет пройден
        self.assertEqual(test, {"action": "presence", "time": 1.1})


if __name__ == '__main__':
    unittest.main()
