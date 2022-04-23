
"""
2. Каждое из слов «class», «function», «method» записать в байтовом типе без преобразования в
последовательность кодов (не используя методы encode и decode) и определить тип,
содержимое и длину соответствующих переменных.
"""


def value_type_list(value_list):
    for i in value_list:
        item = eval(f"b'{i}'")
        print('тип =', type(item), '; значение = ', item, '; количество символов = ', len(item))


WORD_1 = 'class'
WORD_2 = 'function'
WORD_3 = 'method'
WORDS = [WORD_1, WORD_2, WORD_3]

value_type_list(WORDS)
