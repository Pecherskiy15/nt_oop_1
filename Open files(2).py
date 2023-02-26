import os
from pprint import pprint

cook_book = {}

with open(r'/Users/aleksanderpecherskiy/Desktop/open_files/recipes.txt', 'r') as text:
    for line in text:
        menu_position = line.strip()
        counters = int(text.readline())
        cooking = []
        for _ in range(counters):
            x = text.readline().strip()
            ingredient_name, quantity, measure = x.split(' | ')
            cooking.append(
                {'ingredient_name': ingredient_name,
                 'quantity': quantity,
                 'measure': measure}
            )
        cook_book[menu_position] = cooking
        text.readline()



def get_shop_list_by_dishes(dishes, person_count):
    total = {}
    for dish in dishes:
        if dish in cook_book:
            for exist in cook_book[dish]:
                if dish not in total:
                    total[exist['ingredient_name']] = {'measure': exist['measure'],
                                                       'quantity': int(exist['quantity']) * person_count}


def files():
    total_files = {}
    for name in range(1, 4):
        f = open(rf'/Users/aleksanderpecherskiy/Desktop/py-homework-basic-files/2.4.files/sorted/{name}.txt', 'r')
        total_files[name] = len(f.readlines())
        f.close()

    sorted_values = sorted(total_files.values())
    sorted_dict = {}
    for i in sorted_values:
        for k in total_files.keys():
            if total_files[k] == i:
                sorted_dict[k] = total_files[k]
                break

    for i in sorted_dict:
        c = open(r'/Users/aleksanderpecherskiy/Desktop/open_files/common_file.txt', 'a')
        s = open(rf'/Users/aleksanderpecherskiy/Desktop/py-homework-basic-files/2.4.files/sorted/{i}.txt', 'r')
        c.write(s.read())
        c.close(), s.close()
