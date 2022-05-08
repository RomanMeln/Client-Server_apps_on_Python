"""
3. Определить, какие из слов «attribute», «класс», «функция», «type» невозможно записать в
байтовом типе.
"""


def value_type_list(value_list):
    for i in value_list:
        try:
            print(f'Слово "{i}" в байтовом типе: {i.encode("ASCII")}')
        except UnicodeEncodeError:
            print(f'Слово "{i}" невозможно записать в байтовом типе')


WORD_1 = 'attribute'
WORD_2 = 'класс'
WORD_3 = 'функция'
WORD_4 = 'type'
WORDS = [WORD_1, WORD_2, WORD_3, WORD_4]

value_type_list(WORDS)
