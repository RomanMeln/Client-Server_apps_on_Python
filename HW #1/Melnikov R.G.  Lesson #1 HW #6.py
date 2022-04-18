
"""
6. Создать текстовый файл test_file.txt, заполнить его тремя строками: «сетевое
программирование», «сокет», «декоратор». Проверить кодировку файла по умолчанию.
Принудительно открыть файл в формате Unicode и вывести его содержимое.
"""


def value_type_list(value_list):
    for i in value_list:
        item = i.encode('utf-8')
        print(f'Слово "{i}" \n в методе encode(utf-8): {item},'
              f'\n и обратном методе decode(utf-8): {item.decode("utf-8")}')


WORD_1 = 'разработка'
WORD_2 = 'администрирование'
WORD_3 = 'protocol'
WORD_4 = 'standard'
WORDS = [WORD_1, WORD_2, WORD_3, WORD_4]

value_type_list(WORDS)
