
"""
1. Каждое из слов «разработка», «сокет», «декоратор» представить в строковом формате и
проверить тип и содержание соответствующих переменных. Затем с помощью
онлайн-конвертера преобразовать строковые представление в формат Unicode и также
проверить тип и содержимое переменных.
"""


def value_type_list(value_list):
    for i in value_list:
        print(i, type(i))


WORD_1 = 'разработка'
WORD_2 = 'сокет'
WORD_3 = 'декоратор'
WORDS = [WORD_1, WORD_2, WORD_3]

value_type_list(WORDS)

WORD_UNICODE_1 = '\u0440\u0430\u0437\u0440\u0430\u0431\u043e\u0442\u043a\u0430'
WORD_UNICODE_2 = '\u0441\u043e\u043a\u0435\u0442'
WORD_UNICODE_3 = '\u0434\u0435\u043a\u043e\u0440\u0430\u0442\u043e\u0440'

WORDS_UNICODE = [WORD_UNICODE_1, WORD_UNICODE_2, WORD_UNICODE_3]

value_type_list(WORDS_UNICODE)
