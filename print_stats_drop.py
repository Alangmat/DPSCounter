import json
import os
import mailing
import items
import matplotlib.pyplot as plt


# Путь к JSON файлу
json_file_path = 'drops_count.json'

# Загрузка словаря из JSON файла или создание нового, если файл отсутствует
if os.path.exists(json_file_path):
    with open(json_file_path, 'r') as f:
        try:
            drops_count = json.load(f)
        except:
            drops_count = {}
else:
    drops_count = {}

cat_flag = False

sm = sum(drops_count.values())
sorted_dict = dict(sorted(drops_count.items(), key=lambda item: item[1], reverse=True))

if cat_flag:
    print(sorted_dict)
    drops = {
        "bars": 0,
        "predel_consumables_32": 0,
        "crafting_resourses" : 0,
        "amplification": 0,
        "predel_weapons_32" : 0,
        "predel_weapons_34": 0,
        "predel_armor_32": 0,
        "predel_armor_34": 0,
        "predel_accessories_32": 0,
        "predel_accessories_34": 0,
        "great_relics": 0,
        "other": 0,
    }

    for key in sorted_dict.keys():
        if key in items.bars.keys():
           drops["bars"] += sorted_dict[key]
        elif key in items.predel_consumables_32.keys():
            drops["predel_consumables_32"] += sorted_dict[key]
        elif key in items.crafting_resourses.keys():
            drops["crafting_resourses"] += sorted_dict[key]
        elif key in items.amplification.keys():
            drops["amplification"] += sorted_dict[key]
        elif key in items.predel_weapons_32.keys():
            drops["predel_weapons_32"] += sorted_dict[key]
        elif key in items.predel_weapons_34.keys():
            drops["predel_weapons_34"] += sorted_dict[key]
        elif key in items.predel_armor_32.keys():
            drops["predel_armor_32"] += sorted_dict[key]
        elif key in items.predel_armor_34.keys():
            drops["predel_armor_34"] += sorted_dict[key]
        elif key in items.predel_accessories_32.keys():
            drops["predel_accessories_32"] += sorted_dict[key]
        elif key in items.predel_accessories_34.keys():
            drops["predel_accessories_34"] += sorted_dict[key]
        elif key in items.great_relics.keys():
            drops["great_relics"] += sorted_dict[key]
        else: 
            drops["other"] += sorted_dict[key]
    # print(drops)

    sorted_drops = dict(sorted(drops.items(), key=lambda item: item[1], reverse=True))

    labels = sorted_drops.keys()
    values = [x/sm * 100 for x in sorted_drops.values()]


else:
    dict_str_byte_drop = {}
    for key in items.drops.keys() :
        key_parse = mailing.parse_packet(key)
        str_key = "".join(key_parse[2:len(key_parse)])
        dict_str_byte_drop[str_key] = items.drops[key]


    values = [x/sm * 100 for x in sorted_dict.values()]
    labels = []
    for x in sorted_dict.keys():
        if x in items.all_data:labels.append(items.all_data[x])
        # if x in dict_str_byte_drop.keys(): labels.append(dict_str_byte_drop[x])
        else: labels.append(x)

    print(labels)

plt.figure(figsize=(18, 10))  # Размер фигуры
    # plt.bar(labels, values, color=plt.cm.tab20.colors)  # Столбчатая диаграмма

bars = plt.bar(labels, values, color=plt.cm.tab20.colors)  # Столбчатая диаграмма

    # Добавление подписей значений над каждым столбиком
for bar in bars:
    height = bar.get_height()  # Высота столбика
    plt.text(
        bar.get_x() + bar.get_width() / 2,  # Координата X текста (центр столбика)
        height + 0.5,  # Координата Y текста (чуть выше столбика)
        f'{height:.1f}',  # Текст подписи с одним знаком после запятой
        ha='center',  # Горизонтальное выравнивание
        va='bottom',  # Вертикальное выравнивание
        fontsize=8  # Размер шрифта
    )

plt.yticks(range(0,80 if cat_flag else 30))
plt.title(f'Распределение значений, кол-во записей: {sm}', fontsize=14)  # Заголовок
plt.xlabel("Дроп", fontsize=12)  # Подпись оси X
plt.ylabel("Вероятность дропа, %", fontsize=12)  # Подпись оси Y
plt.xticks(rotation=45, ha="right")  # Поворот меток оси X
plt.grid(axis='y', linestyle='--', alpha=0.7)  # Сетка только для оси Y

plt.tight_layout()  # Уменьшение пустого пространства
plt.show()  







