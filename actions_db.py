import sqlite3

def get_heroes():
    conn = sqlite3.connect('warspear_heroes.db')
    cursor = conn.cursor()

    cursor.execute('SELECT * FROM warspear_heroes')
    rows = cursor.fetchall()
    conn.close()
    return rows

def add_hero(id_hero, nickname):
    conn = sqlite3.connect('warspear_heroes.db')
    cursor = conn.cursor()

    cursor.execute('''
        INSERT INTO warspear_heroes (id_hero, nickname) VALUES (?, ?)
    ''', (id_hero, nickname))

    conn.commit()
    conn.close()

def create_update_hero(id_hero, nickname):
    conn = sqlite3.connect('warspear_heroes.db')
    cursor = conn.cursor()

    # Начинаем транзакцию
    conn.execute('BEGIN')

    cursor.execute('SELECT nickname FROM warspear_heroes WHERE id_hero = ?', (id_hero,))
    result = cursor.fetchone()

    if result:
        existing_nickname = result[0]
        if existing_nickname != nickname:
            cursor.execute('''
                UPDATE warspear_heroes
                SET nickname = ?
                WHERE id_hero = ?
            ''', (nickname, id_hero))
            print(f"Никнейм для ID {id_hero} обновлен с '{existing_nickname}' на '{nickname}'.")
        else:
            print(f"Герой с ID {id_hero} уже существует с таким же никнеймом '{nickname}'.")
    else:
        cursor.execute('''
            INSERT INTO warspear_heroes (id_hero, nickname) VALUES (?, ?)
        ''', (id_hero, nickname))
        print(f"Новый герой с ID {id_hero} и никнеймом '{nickname}' добавлен успешно.")
    conn.commit()


# add_hero("\\xe9}K", "Alangmat")
# print(get_heroes()[0][0])

# create_update_hero("\\xe9}K", "Alangmat")