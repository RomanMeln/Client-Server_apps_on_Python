
"""
6. Создать текстовый файл test_file.txt, заполнить его тремя строками: «сетевое
программирование», «сокет», «декоратор». Проверить кодировку файла по умолчанию.
Принудительно открыть файл в формате Unicode и вывести его содержимое.
"""
import chardet

WORDS = ['сетевое программирование', 'сокет', 'декоратор']
FILE_NAME = 'test_file.txt'

with open(FILE_NAME, 'w', encoding='utf-8') as f:
    for i in WORDS:
        f.write(f'{i}\n')

with open(FILE_NAME, 'rb') as f_n:
    content = f_n.read()
    encoding = chardet.detect(content)['encoding']
    print(encoding)

with open(FILE_NAME, encoding=encoding) as f_n:
    content = f_n.read()
    print(content)

