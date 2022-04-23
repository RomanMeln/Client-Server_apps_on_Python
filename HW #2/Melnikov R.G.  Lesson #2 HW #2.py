
"""
2. Задание на закрепление знаний по модулю json. Есть файл orders в формате JSON с
информацией о заказах. Написать скрипт, автоматизирующий его заполнение данными. Для
этого:
    a. Создать функцию write_order_to_json(), в которую передается 5 параметров — товар
    (item), количество (quantity), цена (price), покупатель (buyer), дата (date). Функция
    должна предусматривать запись данных в виде словаря в файл orders.json. При
    записи данных указать величину отступа в 4 пробельных символа;
    b. Проверить работу программы через вызов функции write_order_to_json() с передачей
    в нее значений каждого параметра.
"""
import json


def write_order_to_json(item: str, quantity: str, price: str, buyer: str, date: str):

    with open('orders.json', 'r', encoding='utf-8') as f_out:
        data = json.load(f_out)

    with open('orders.json', 'w', encoding='utf-8') as f_in:
        orders_list = data['orders']
        order_info = {
            'item': item,
            'quantity': quantity,
            'price': price,
            'buyer': buyer,
            'date': date
        }
        orders_list.append(order_info)
        json.dump(data, f_in, indent=4, ensure_ascii=False)


write_order_to_json('Бумага', '10', '240', 'Бумагов Б.Б.', '01.04.2022')
write_order_to_json('Доллар', '1000', '50', 'Инвесторов И.И.', '22.04.2022')
write_order_to_json('Сахар', '5', '50', 'Сахаров С.С', '25.03.2022')
