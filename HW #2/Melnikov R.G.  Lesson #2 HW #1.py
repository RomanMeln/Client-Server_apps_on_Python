
"""
1. Задание на закрепление знаний по модулю CSV. Написать скрипт, осуществляющий выборку
определенных данных из файлов info_1.txt, info_2.txt, info_3.txt и формирующий новый
«отчетный» файл в формате CSV. Для этого:
    a. Создать функцию get_data(), в которой в цикле осуществляется перебор файлов с
    данными, их открытие и считывание данных. В этой функции из считанных данных
    необходимо с помощью регулярных выражений извлечь значения параметров
    «Изготовитель системы», «Название ОС», «Код продукта», «Тип системы». Значения
    каждого параметра поместить в соответствующий список. Должно получиться четыре
    списка — например, os_prod_list, os_name_list, os_code_list, os_type_list. В этой же
    функции создать главный список для хранения данных отчета — например, main_data
    — и поместить в него названия столбцов отчета в виде списка: «Изготовитель
    системы», «Название ОС», «Код продукта», «Тип системы». Значения для этих
    столбцов также оформить в виде списка и поместить в файл main_data (также для
    каждого файла);
    b. Создать функцию write_to_csv(), в которую передавать ссылку на CSV-файл. В этой
    функции реализовать получение данных через вызов функции get_data(), а также
    сохранение подготовленных данных в соответствующий CSV-файл;
    c. Проверить работу программы через вызов функции write_to_csv().
"""
import chardet
import csv
import re

FILES = ['info_1.txt', 'info_2.txt', 'info_3.txt']
HEADERS = ['Изготовитель системы', 'Название ОС', 'Код продукта', 'Тип системы']


def get_data():

    os_prod_list = []
    os_name_list = []
    os_code_list = []
    os_type_list = []
    main_data = []

    for i in FILES:
        with open(i, 'rb') as f:
            content = f.read()
            result = chardet.detect(content)
            data = content.decode(result['encoding'])

        made_by_prod = re.compile(r'Изготовитель ОС:\s*\S*')
        os_prod_list.append(made_by_prod.findall(data)[0].split()[2])

        os_name_reg = re.compile(r'Windows\s\S*')
        os_name_list.append(os_name_reg.findall(data)[0])

        os_code_reg = re.compile(r'Код продукта:\s*\S*')
        os_code_list.append(os_code_reg.findall(data)[0].split()[2])

        os_type_reg = re.compile(r'Тип системы:\s*\S*')
        os_type_list.append(os_type_reg.findall(data)[0].split()[2])

    main_data.append(HEADERS)
    data_for_rows = [os_prod_list, os_name_list, os_code_list, os_type_list]

    for idx in range(len(data_for_rows[0])):
        line = [row[idx] for row in data_for_rows]
        main_data.append(line)

    return main_data


def write_to_csv(out_file):
    main_data = get_data()
    with open(out_file, 'w', encoding='utf-8') as file:
        writer = csv.writer(file)
        for row in main_data:
            writer.writerow(row)


write_to_csv('report.csv')
