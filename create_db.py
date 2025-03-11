import sqlite3

conn = sqlite3.connect('Warspear_heroes.db')
cursor = conn.cursor()

# Создаем таблицу heroes с двумя столбцами: id_hero и nickname
cursor.execute('''
    CREATE TABLE IF NOT EXISTS warspear_heroes (
        id_hero varchar(15) PRIMARY KEY,
        nickname varchar(10) NOT NULL
    )
''')

# Сохраняем изменения
conn.commit()

# Закрываем соединение
conn.close()