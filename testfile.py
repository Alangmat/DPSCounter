import os
from datetime import datetime
import re

# Пример словаря
data = {
    "player1": {
        "\\xe1<R": ["20:35:40 - 500 урон", "20:36:10 - 300 урон"],
        "\\xe2>P": ["20:40:00 - 700 урон"]
    },
    "player2": {
        "\\xe3?Q": ["20:50:00 - 600 урон"]
    }
}

# Функция для безопасного имени файла
def sanitize_filename(filename):
    # Заменяем недопустимые символы на "_"
    return re.sub(r'[\\/:*?"<>|]', '_', filename)

# Функция для создания файла и записи данных
def save_data_to_files(data, damage_dict, time, base_folder="logs"):
    # Создаем подпапку с текущей датой внутри папки logs
    current_date = datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
    date_folder = os.path.join(base_folder, current_date)

    # Проверяем, существует ли папка, если нет — создаем её
    if not os.path.exists(date_folder):
        os.makedirs(date_folder)

    for nicname, ids in data.items():
        for player_id, records in ids.items():
            # Безопасное имя файла
            safe_player_id = sanitize_filename(player_id)
            filename = f"{nicname}-{safe_player_id}-{current_date}.txt"
            
            # Полный путь к файлу
            file_path = os.path.join(date_folder, filename)
            

            dpm = calc_dpm(records)
            # Создаем и записываем данные в файл
            with open(file_path, "w", encoding="utf-8") as file:
                file.write(f"ДПМ в данную цель = {dpm}\n")
                file.write("\n".join(records))
            
            print(f"Данные записаны в файл: {file_path}")

def calc_dpm(records):
    i = 0
    # print("начало calc_dpm")
    time_str1 = None
    time_str2 = None
    sum_damage = 0
    for r in records:
        time, sp, damage = r.split()
        # Преобразуем строки во время
        if (i == 0): time_str1 = time
        if (i == len(records) - 1): time_str2 = time
        i += 1
        sum_damage += int(damage)
    # print("прошел цикл")
    time1 = datetime.strptime(time_str1, "%H:%M:%S")
    time2 = datetime.strptime(time_str2, "%H:%M:%S")
    # print("прошел перевод времени")

    # Вычисляем разницу
    difference = time2 - time1
    # print("прошла разница")
    # Получаем разницу в секундах
    seconds_difference = difference.total_seconds()
    # print("прошел перевод")
    if seconds_difference >= 1:
        dpm = sum_damage / seconds_difference * 60
        print("прошел расчет дпм")
        return dpm
    return sum_damage





# Сохранение данных
# save_data_to_files(data)