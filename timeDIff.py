from datetime import datetime
import time

# Сохраняем первое время
time1 = datetime.now()

# Засыпаем на 3 секунды
time.sleep(3)

# Некоторая задержка (например, выполнение кода или ожидание)
time2 = datetime.now()

# Вычисляем разницу
difference = time2 - time1

# Получаем разницу в секундах
seconds_difference = difference.total_seconds()

print(f"Разница в секундах: {seconds_difference}")
