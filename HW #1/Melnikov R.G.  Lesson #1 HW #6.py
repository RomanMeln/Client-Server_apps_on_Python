
"""
6. Создать текстовый файл test_file.txt, заполнить его тремя строками: «сетевое
программирование», «сокет», «декоратор». Проверить кодировку файла по умолчанию.
Принудительно открыть файл в формате Unicode и вывести его содержимое.
"""
import chardet

file_name = 'test_file.txt'
with open(file_name, 'rb') as f_n:
    content = f_n.read()
encoding = chardet.detect(content)['encoding']
print(encoding)

with open(file_name, encoding='utf-8') as f_n:
    for el_str in f_n:
        print(el_str)

