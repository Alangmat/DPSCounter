drops = {
   b"\x02;": "дф",
   b"\x01;": "урон",
   b"\x8d\xa9": "хп-отраж",
   b"\x94\xa9": "мана-отраж",
   b"Tn": "мана-пронза",
   b"Mn": "хп-пронза",
   b"\x0b*": "медь",
   b"\x0c*": "серебро",
   b"\r*": "золото",
   b"\x0e*": "платина",
   b"\x0f*": "мифрил",
   b"\xf27": "эфкат",
   b"\x1f:": "эфэсс",
   b"i\\": "эфмат",
}

bars = {
   "\\x0b*": "[Медный слиток]",
   "\\x0c*": "[Серебряный слиток]",
   "\\r*": "[Золотой слиток]",
   "\\x0e*": "[Платиновый слиток]",
   "\\x0f*": "[Мифриловый слиток]",
}

predel_consumables_32 = {
   "\\x8d\\xa9": "[Жгучая настойка экспедиторов]",
   "\\x94\\xa9": "[Вулканическая настойка экспедиторов]",
   "Tn": "[Будоражащая настойка полярников]",
   "Mn": "[Заводящая настойка полярников]",
   '\\xa8x': "[Ключ от Ледяного сундука]",
}

crafting_resourses = {
   "\\xf27": "[Эфирный катализатор]",
   "\\x1f:": "[Эфирная эссенция]",
   "i\\\\": "[Эфирная материя]",
   '\\x1e:': "[Энергетическая эссенция]",
   'h\\\\': "[Энергетическая материя]",
   '\\xf17': "[Энергетический катализатор]",
   'g\\\\': "[Сложная материя]",
   '\\xf07': "[Усиленный катализатор]",
   '\\x1d:': "[Сложная эссенция]",
   '\\xef7': "[Обычный катализатор]",
   '\\x1c:': "[Обычная эссенция]",
   'f\\\\': "[Обычная материя]"
}

amplification = {
   "\\x02;": "[Сфера усиления защиты lll]",
   "\\x01;": "[Сфера усиления урона lll]",
}

predel_weapons_32 = {
   "\\x8b\\x83": "[Штурмовой щит Властелина севера]",
   '\\x8a\\x83': "[Боевой щит Властелина севера]",
   'k\\x83': "[Щит Безудержного урагана]",
   '\\x86\\x83': "[Балестра Властелина севера]",
   'g\\x83': "[Арбалет Безудержного урагана]",
   '\\x85\\x83': "[Лук Властелина севера]",
   '\\x84\\x83': "[Боевой лук Властелина севера]",
   'f\\x83': "[Лук Безудержного урагана]",
   '\\x89\\x83': "[Скипетр Властелина севера]",
   '\\x88\\x83': "[Клюка Властелина севера]",
   '\\x87\\x83': "[Посох Властелина севера]",
   'j\\x83': "[Жезл Безудержного урагана]",
   'i\\x83': "[Скипетр Безудержного урагана]",
   'h\\x83': "[Посох Безудержного урагана]",
   '\\x83\\x83': "[Гизарма Властелина севера]",
   'e\\x83': "[Копьё Безудержного урагана]",
   '\\x82\\x83': "[Моргенштерн Властелина севера]",
   '\\x81\\x83': "[Молот Властелина севера]",
   'd\\x83': "[Молот Безудержного урагана]",
   '~\\x83': "[Магическая булава Властелина севера]",
   '}\\x83': "[Палица Властелина севера]",
   '|\\x83': "[Булава Властелина севера]",
   'a\\x83': "[Магическая булава Безудержного урагана]",
   '`\\x83': "[Палица Безудержного урагана]",
   '_\\x83': "[Булава Безудержного урагана]",
   '\\x80\\x83': "[Секира Властелина севера]",
   'c\\x83': "[Секира Безудержного урагана]",
   '{\\x83': "[Топор Властелина севера]",
   '^\\x83': "[Топор Безудержного урагана]",
   '\\x7f\\x83': "[Эспадон Властелина севера]",
   'b\\x83': "[Меч Безудержного урагана]",
   'z\\x83': "[Фалчион Властелина севера]",
   ']\\x83': "[Клинок Безудержного урагана]",
   'y\\x83': "[Кинжал Властелина севера]",
   'x\\x83': "[Крис Властелина севера]",
   '\\\\\\x83': "[Кинжал Безудержного урагана]",
}

predel_weapons_34 = {
   '?\\xa8': "[Щит Трескучего мороза]",
   '/\\xa8': "[Штурмовой щит Хозяина гор]",
   '.\\xa8': "[Боевой щит Хозяина гор]",
   ';\\xa8': "[Арбалет Трескучего мороза]",
   '*\\xa8': "[Балестра Хозяина гор]",
   ':\\xa8': "[Лук Трескучего мороза]",
   ')\\xa8': "[Лук Хозяина гор]",
   '(\\xa8': "[Боевой лук Хозяина гор]",
   '>\\xa8': "[Жезл Трескучего мороза]",
   '=\\xa8': "[Скипетр Трескучего мороза]",
   '<\\xa8': "[Посох Трескучего мороза]",
   '-\\xa8': "[Скипетр Хозяина гор]",
   ',\\xa8': "[Клюка Хозяина гор]",
   '+\\xa8': "[Посох Хозяина гор]",
   '9\\xa8': "[Копьё Трескучего мороза]",
   "\\'\\xa8": "[Гизарма Хозяина гор]",
   '8\\xa8': "[Молот Трескучего мороза]",
   '&\\xa8': "[Моргенштерн Хозяина пьр]",
   '%\\xa8': "[Молот Хозяина гор]",
   '5\\xa8': "[Магическая булава Трескучего мороза]",
   '4\\xa8': "[Палица Трескучего мороза]",
   '3\\xa8': "[Булава Трескучего мороза]",
   '"\\xa8': "[Магическая булава Хозяина гор]",
   '!\\xa8': "[Палица Хозяина гор]",
   ' \\xa8': "[Булава Хозяина гор]",
   '7\\xa8': "[Секира Трескучего мороза]",
   '$\\xa8': "[Секира Хозяина гор]",
   '2\\xa8': "[Топор Трескучего мороза]",
   '\\x1f\\xa8': "[Топор Хозяина гор]",
   '6\\xa8': "[Меч Трескучего мороза]",
   '#\\xa8': "[Эспадон Хозяина гор]",
   '1\\xa8': "[Клинок Трескучего мороза]",
   '\\x1e\\xa8': "[Фалчион Хозяина гор]",
   '0\\xa8': "[Кинжал Трескучего мороза]",
   '\\x1d\\xa8': "[Кинжал Хозяина гор]",
   '\\x1c\\xa8': "[Крис Хозяина гор]",
}

predel_armor_32 = {
   'L\\x84': "[Зимние сабатоны Титана]",
   'H\\x84': "[Зимние ботфорты Титана]",
   'D\\x84': "[Зимние сапоги Титана]",
   '@\\x84': "[Зимние ботинки Титана]",
   '<\\x84': "[Зимние башмаки Титана]",
   '8\\x84': "[Зимние туфли Титана]",
   'K\\x84': "[Зимние рукавицы Титана]",
   'G\\x84': "[Зимние наручи Титана]",
   'C\\x84': "[Зимние краги Титана]",
   '?\\x84': "[Зимние поручи Титана]",
   ';\\x84': "[Зимние варежки Титана]",
   '7\\x84': "[Зимние перчатки Титана]",
   '\\x16\\x84': "[Портупея Властелина севера]",
   '\\x15\\x84': "[Ремень Властелина севера]",
   '\\x11\\x84': "[Гурт Властелина севера]",
   '\\x10\\x84': "[Пояс Властелина севера]",
   '\\x0c\\x84': "[Кушак Властелина севера]",
   '\\x0b\\x84': "[Перевязь Властелина севера]",
   'I\\x84': "[Зимняя бармица Титана]",
   'E\\x84': "[Зимний топхельм Титана]",
   'A\\x84': "[Зимняя шапка Титана]",
   '=\\x84': "[Зимний шлем Титана]",
   '9\\x84': "[Зимний клобук Титана]",
   '5\\x84': "[Зимний капюшон Титана]",
   'J\\x84': "[Зимняя броня Титана]",
   'F\\x84': "[Зимний хауберк Титана]",
   'B\\x84': "[Зимний дублет Титана]",
   '>\\x84': "[Зимняя бригантина Титана]",
   ':\\x84': "[Зимний балахон Титана]",
   '6\\x84': "[Зимнее облачение Титана]",
}

predel_armor_34 = {
   '\\x86\\xa8': "[Зимние сабатоны Тороса]",
   '\\x82\\xa8': "[Зимние ботфорты Тороса]",
   '~\\xa8': "[Зимние сапоги Тороса]",
   'z\\xa8': "[Зимние ботинки Тороса]",
   'v\\xa8': "[Зимние башмаки Тороса]",
   'r\\xa8': "[Зимние туфли Тороса]",
   '\\x85\\xa8': "[Зимние рукавицы Тороса]",
   '\\x81\\xa8': "[Зимние наручи Тороса]",
   '}\\xa8': "[Зимние краги Тороса]",
   'y\\xa8': "[Зимние поручи Тороса]",
   'u\\xa8': "[Зимние варежки Тороса]",
   'q\\xa8': "[Зимние перчатки Тороса]",
   'k\\xa8': "[Портупея Хозяина гор]",
   'j\\xa8': "[Ремень Хозяина гор]",
   'f\\xa8': "[Гурт Хозяина гор]",
   'e\\xa8': "[Пояс Хозяина гор]",
   'a\\xa8': "[Кушак Хозяина гор]",
   '`\\xa8': "[Перевязь Хозяина гор]",
   '\\x83\\xa8': "[Зимняя бармица Тороса]",
   '\\x7f\\xa8': "[Зимний топхельм Тороса]",
   '{\\xa8': "[Зимняя шапка Тороса]",
   'w\\xa8': "[Зимний шлем Тороса]",
   's\\xa8': "[Зимний клобук Тороса]",
   'o\\xa8': "[Зимний капюшон Тороса]",
   '\\x84\\xa8': "[Зимняя броня Тороса]",
   '\\x80\\xa8': "[Зимний хауберк Тороса]",
   '|\\xa8': "[Зимний дублет Тороса]",
   'x\\xa8': "[Зимняя бригантина Тороса]",
   't\\xa8': "[Зимний балахон Тороса]",
   'p\\xa8': "[Зимнее облачение Тороса]",
}

predel_accessories_32 = {
   '\\x99\\x9d': "[Штормовой обод Титана]",
   '\\x98\\x9d': "[Лютый обод Титана]",
   '\\x97\\x9d': "[Штормовой браслет Титана]",
   '\\x96\\x9d': "[Лютый браслет Титана]",
   '\\x95\\x9d': "[Штормовой кафф Титана]",
   '\\x94\\x9d': "[Лютый кафф Титана]",
   '\\x93\\x9d': "[Штормовой обруч Титана]",
   '\\x92\\x9d': "[Лютый обруч Титана]",
   '\\x85\\x8f': "[Штормовой лимб Титана]",
   'x\\x8f': "[Штормовая печатка Титана]",
   '\\x91\\x83': "[Лютый лимб Титана]",
   '\\x90\\x83': "[Штормовой перстень Титана]",
   '\\x8f\\x83': "[Лютый перстень Титана]",
   '\\x8e\\x83': "[Лютая печатка Титана]",
   '\\x8d\\x83': "[Штормовое кольцо Титана]",
   '\\x8c\\x83': "[Лютое кольцо Титана]",
   '\\x9f\\x8f': "[Штормовой кулон Титана]",
   '\\x92\\x8f': "[Штормовое ожерелье Титана]",
   '\\x97\\x83': "[Лютый кулон Титана]",
   '\\x96\\x83': "[Штормовой амулет Титана]",
   '\\x95\\x83': "[Лютый амулет Титана]",
   '\\x94\\x83': "[Лютое ожерелье Титана]",
   '\\x93\\x83': "[Штормовой медальон Титана]",
   '\\x92\\x83': "[Лютый медальон Титана]",
   '\\xb9\\x8f': "[Штормовой хитон Титана]",
   '\\xac\\x8f': "[Штормовая хламида Титана]",
   '\\x9d\\x83': "[Лютый хитон Титана]",
   '\\x9c\\x83': "[Штормовой плащ Титана]",
   '\\x9b\\x83': "[Лютый плащ Титана]",
   '\\x9a\\x83': "[Лютая хламида Титана]",
   '\\x99\\x83': "[Штормовая накидка Титана]",
   '\\x98\\x83': "[Лютая накидка Титана]",
}

predel_accessories_34 = {
   '_\\xa8': "[Штормовой обод Тороса]",
   '^\\xa8': "[Лютый обод Тороса]",
   ']\\xa8': "[Штормовой браслет Тороса]",
   '\\\\\\xa8': "[Лютый браслет Тороса]",
   '[\\xa8': "[Штормовой кафф Тороса]",
   'Z\\xa8': "[Лютый кафф Тороса]",
   'Y\\xa8': "[Штормовой обруч Тороса]",
   'X\\xa8': "[Лютый обруч Тороса]",
   'G\\xa8': "[Штормовой лимб Тороса]",
   'F\\xa8': "[Штормовая печатка Тороса]",
   'E\\xa8': "[Лютый лимб Тороса]",
   'D\\xa8': "[Штормовой перстень Тороса]",
   'C\\xa8': "[Лютый перстень Тороса]",
   'B\\xa8': "[Лютая печатка Тороса]",
   'A\\xa8': "[Штормовое кольцо Тороса]",
   '@\\xa8': "[Лютое кольцо Тороса]",
   'O\\xa8': "[Штормовой кулон Тороса]",
   'N\\xa8': "[Штормовое ожерелье Тороса]",
   'M\\xa8': "[Лютый кулон Тороса]",
   'L\\xa8': "[Штормовой амулет Тороса]",
   'K\\xa8': "[Лютый амулет Тороса]",
   'J\\xa8': "[Лютое ожерелье Тороса]",
   'I\\xa8': "[Штормовой медальон Тороса]",
   'H\\xa8': "[Лютый медальон Тороса]",
   'W\\xa8': "[Штормовой хитон Тороса]",
   'V\\xa8': "[Штормовая хламида Тороса]",
   'U\\xa8': "[Лютый хитон Тороса]",
   'T\\xa8': "[Штормовой плащ Тороса]",
   'S\\xa8': "[Лютый плащ Тороса]",
   'R\\xa8': "[Лютая хламида Тороса]",
   'Q\\xa8': "[Штормовая накидка Тороса]",
   'P\\xa8': "[Лютая накидка Тороса]",
}

great_relics = {
   '\\xf8R': "[Великая реликвия энергетической стабильности]",
   '\\xb2L': "[Великая реликвия убийственного озарения]",
   '\\xb1L': "[Великая реликвия снятия проклятия]",
   '\\xb0L': "[Великая реликвия развеивания чар]",
   'ML': "[Великая реликвия продолжительного действия]",
   'LL': "[Великая реликвия спасительного исцеления]",
   'KL': "[Великая реликвия угрозы]",
   'JL': "[Великая реликвия множественного заклинания]",
   'IL': "[Великая реликвия обновления духа]",
   'HL': "[Великая реликвия массовой кары]",
   'GL': "[Великая реликвия восстановления сил]",
   'FL': "[Великая реликвия неукротимого удара]",
   'EL': "[Великая реликвия внезапной силы]",
   'DL': "[Великая реликвия игнорирования защиты]",
   'CL': "[Великая реликвия карающего умения]",
   'BL': "[Великая реликвия энергетической эффективности]",
   'AL': "[Великая реликвия энергетического наказания]",
   '@L': "[Великая реликвия сосредоточенности]",
   '?L': "[Великая реликвия высшего мастерства]",
   "\\'L": "[Великая реликвия недосягаемости]",
}


all_data = {**amplification, **bars, **predel_consumables_32, **crafting_resourses, **predel_weapons_32, **predel_weapons_34, **predel_armor_32, **predel_armor_34, **predel_accessories_32, **predel_accessories_34}

merman_pets = {
    'Lg': "[Призыв Элементаля воды]",
    'Mg': "[Призыв Хранителя Морской Пучины]",
}

merman_consumables = {
    '\\x03s': "[Смертоносное зелье воинов-водолазов]",
    '\\x04s': "[Смертоносное зелье магов-водолазов]",
    '\\x05s': "[Прошибающее зелье воинов-водолазов]",
    '\\x06s': "[Прошибающее зелье магов-водолазов]",
    '\\x07s': "[Свиток мощи тритонов]",
    '\\x08s': "[Свиток магии тритонов]",
    'lf': "[Ключ от Пиратского сундука]",
    '--': "[Знак единства]",
}

merman_armor = {
    '\\xdar': "[Балахон сакрального знамения]",
    '\\xder': "[Балахон незримых знаний]",
    '\\xe2r': "[Дублет искажения времени]",
    '\\xe6r': "[Дублет фатального возмездия]",
    '\\xear': "[Броня воплощения могущества]",
    '\\xeer': "[Броня веления рока]",
    '\\xd9r': "[Капюшон сакрального знамения]",
    '\\xddr': "[Капюшон незримых знаний]",
    '\\xe1r': "[Шлем искажения времени]",
    '\\xe5r': "[Шлем фатального возмездия]",
    '\\xe9r': "[Топхельм воплощения могущества]",
    '\\xedr': "[Топхельм веления рока]",
    '\\xdbr': "[Перчатки сакрального знамения]",
    '\\xdfr': "[Перчатки незримых знаний]",
    '\\xe3r': "[Краги искажения времени]",
    '\\xe7r': "[Краги фатального возмездия]",
    '\\xebr': "[Рукавицы воплощения могущества]",
    '\\xefr': "[Рукавицы веления рока]",
    '\\xdcr': "[Башмаки сакрального знамения]",
    '\\xe0r': "[Башмаки незримых знаний]",
    '\\xe4r': "[Сапоги искажения времени]",
    '\\xe8r': "[Сапоги фатального возмездия]",
    '\\xecr': "[Ботфорты воплощения могущества]",
    '\\xf0r': "[Ботфорты веления рока]",
}

merman_data = {**bars, **crafting_resourses, **amplification, **great_relics, **merman_pets,
               **merman_consumables, **merman_armor }


spring_consumables_32 = {
    '\\x05r': "[Ведовское зелье магистров]",
    '\\x0cr': "[Чародейское зелье магистров]",
    'h\\xac': "[Зачарованное зелье наставников]",
    'o\\xac': "[Заколдованное зелье наставников]",
}

spring_costumes = {
    '\\x9bI': "[Страж Древа жизни]",
}

spring_pets = {
    ']I': "[Призыв Ядовитой жабы]",
}

spring_weapons_34_unique = {
    '\\xc9\\xaa': "[Кинжал Королевства Правосудия]",
    '\\xca\\xaa': "[Клинок Королевства Правосудия]",
    '\\xcf\\xaa': "[Меч Королевства Правосудия]",
    '\\xcb\\xaa': "[Топор Королевства Правосудия]",
    '\\xd0\\xaa': "[Секира Королевства Правосудия]",
    '\\xcc\\xaa': "[Булава Королевства Правосудия]",
    '\\xcd\\xaa': "[Палица Королевства Правосудия]",
    '\\xce\\xaa': "[Магическая булава Королевства Правосудия]",
    '\\xd1\\xaa': "[Молот Королевства Правосудия]",
    '\\xd2\\xaa': "[Моргенштерн Королевства Правосудия]",
    '\\xd3\\xaa': "[Копьё Королевства Правосудия]",
    '\\xd6\\xaa': "[Посох Королевства Правосудия]",
    '\\xd7\\xaa': "[Скипетр Королевства Правосудия]",
    '\\xd8\\xaa': "[Жезл Королевства Правосудия]",
    '\\xd4\\xaa': "[Лук Королевства Правосудия]",
    '\\xd5\\xaa': "[Арбалет Королевства Правосудия]",
    '\\xd9\\xaa': "[Щит Королевства Правосудия]"
}
spring_weapons_34_unique = {
    '\\xdc\\x86': "[Кинжал Королевства Несокрушимости]",
    '\\xdd\\x86': "[Клинок Королевства Несокрушимости]",
    '\\xe2\\x86': "[Меч Королевства Несокрушимости]",
    '\\xe1\\x86': "[Магическая булава Королевства Несокрушимости]",
    '\\xe4\\x86': "[Молот Королевства Несокрушимости]",
    '\\xe5\\x86': "[Моргенштерн Королевства Несокрушимости]",
    '\\xe6\\x86': "[Копьё Королевства Несокрушимости]",
    '\\xe9\\x86': "[Посох Королевства Несокрушимости]",
    '\\xea\\x86': "[Скипетр Королевства Несокрушимости]",
    '\\xeb\\x86': "[Жезл Королевства Несокрушимости]",
    '\\xe7\\x86': "[Лук Королевства Несокрушимости]",
    '\\xe8\\x86': "[Арбалет Королевства Несокрушимости]",
    '\\xec\\x86': "[Щит Королевства Несокрушимости]",
}
spring_weapons_34_rare = {
    '\\xf2\\xaa': "[Кинжал Загадочного магистериума]",
    '\\xf3\\xaa': "[Клинок Загадочного магистериума]",
    '\\xfa\\xaa': "[Меч Загадочного магистериума]",
    '\\xf4\\xaa': "[Топор Загадочного магистериума]",
    '\\xf5\\xaa': "[Чекан Загадочного магистериума]",
    '\\xfb\\xaa': "[Секира Загадочного магистериума]",
    '\\xfc\\xaa': "[Лабрис Загадочного магистериума]",
    '\\xf6\\xaa': "[Булава Загадочного магистериума]",
    '\\xf7\\xaa': "[Палица Загадочного магистериума]",
    '\\xf8\\xaa': "[Магическая булава Загадочного магистериума]",
    '\\xf9\\xaa': "[Магическая палица Загадочного магистериума]",
    '\\xfd\\xaa': "[Молот Загадочного магистериума]",
    '\\xfe\\xaa': "[Моргенштерн Загадочного магистериума]",
    '\\xff\\xaa': "[Кувалда Загадочного магистериума]",
    '\\x00\\xab': "[Копьё Загадочного магистериума]",
    '\\x05\\xab': "[Посох Загадочного магистериума]",
    '\\x06\\xab': "[Трость Загадочного магистериума]",
    '\\x07\\xab': "[Жезл Загадочного магистериума]",
    '\\x08\\xab': "[Скипетр Загадочного магистериума]",
    '\\x01\\xab': "[Пробивной лук Загадочного магистериума]",
    '\\x02\\xab': "[Убойный лук Загадочного магистериума]",
    '\\x03\\xab': "[Арбалет Загадочного магистериума]",
    '\\x04\\xab': "[Балестра Загадочного магистериума]",
    '\\t\\xab': "[Щит Загадочного магистериума]",
}

spring_weapons_32_rare = {
    '\\x0b\\x87': "[Кинжал Магического бастиона]",
    '\\x0c\\x87': "[Клинок Магического бастиона]",
    '\\x11\\x87': "[Меч Магического бастиона]",
    '\\r\\x87': "[Топор Магического бастиона]",
    '7\\x91': "[Чекан Магического бастиона]",
    '\\x12\\x87': "[Секира Магического бастиона]",
    'Q\\x91': "[Лабрис Магического бастиона]",
    '\\x0e\\x87': "[Булава Магического бастиона]",
    '\\x0f\\x87': "[Палица Магического бастиона]",
    '\\x10\\x87': "[Магическая булава Магического бастиона]",
    'D\\x91': "[Магическая палица Магического бастиона]",
    '\\x13\\x87': "[Молот Магического бастиона]",
    '\\x14\\x87': "[Моргенштерн Магического бастиона]",
    '^\\x91': "[Кувалда Магического бастиона]",
    '\\x15\\x87': "[Копьё Магического бастиона]",
    '\\x19\\x87': "[Посох Магического бастиона]",
    '\\x1a\\x87': "[Трость Магического бастиона]",
    '\\x1b\\x87': "[Жезл Магического бастиона]",
    'x\\x91': "[Скипетр Магического бастиона]",
    '\\x16\\x87': "[Пробивной лук Магического бастиона]",
    '\\x17\\x87': "[Убойный лук Магического бастиона]",
    '\\x18\\x87': "[Арбалет Магического бастиона]",
    'k\\x91': "[Балестра Магического бастиона]",
    '\\x1c\\x87': "[Щит Магического бастиона]",
}

spring_accessories_34 = {
    '\\x1e\\xab': "[Волшебная накидка Правосудия]",
    '\\x1f\\xab': "[Чарующая накидка Правосудия]",
    ' \\xab': "[Дивная накидка Правосудия]",
    '!\\xab': "[Волшебная хламида Правосудия]",
    '"\\xab': "[Чарующая хламида Правосудия]",
    '#\\xab': "[Волшебный плащ Правосудия]",
    '$\\xab': "[Чарующий плащ Правосудия]",
    '%\\xab': "[Волшебный хитон Правосудия]",
    '&\\xab': "[Чарующий хитон Правосудия]",
    "\\'\\xab": "[Дивный хитон Правосудия]",

    '\\x14\\xab': "[Волшебный медальон Правосудия]",
    '\\x15\\xab': "[Чарующий медальон Правосудия]",
    '\\x16\\xab': "[Дивный медальон Правосудия]",
    '\\x17\\xab': "[Волшебное ожерелье Правосудия]", 
    '\\x18\\xab': "[Чарующее ожерелье Правосудия]",
    '\\x19\\xab': "[Волшебный амулет Правосудия]",
    '\\x1a\\xab': "[Чарующий амулет Правосудия",
    '\\x1b\\xab': "[Волшебный кулон Правосудия]",
    '\\x1c\\xab': "[Чарующий кулон Правосудия]",
    '\\x1d\\xab': "[Дивный кулон Правосудия]",

    '\\n\\xab': "[Волшебное кольцо Правосудия]",
    '\\x0b\\xab': "[Чарующее кольцо Правосудия]",
    '\\x0c\\xab': "[Дивное кольцо Правосудия]",
    '\\r\\xab': "[Волшебная печатка Правосудия]",
    '\\x0e\\xab': "[Чарующая печатка Правосудия]",
    '\\x0f\\xab': "[Волшебный перстень Правосудия]",
    '\\x10\\xab': "[Чарующий перстень Правосудия]",
    '\\x11\\xab': "[Волшебный лимб Правосудия]",
    '\\x12\\xab': "[Чарующий лимб Правосудия]",
    '\\x13\\xab': "[Дивный лимб Правосудия]",
    
    '(\\xab': "[Волшебный обруч Правосудия]",
    ')\\xab': "[Чарующий обруч Правосудия]",
    '*\\xab': "[Дивный обруч Правосудия]",
    '+\\xab': "[Волшебный кафф Правосудия]",
    ',\\xab': "[Чарующий кафф Правосудия]",
    '-\\xab': "[Волшебный браслет Правосудия]",
    '.\\xab': "[Чарующий браслет Правосудия]",
    '/\\xab': "[Волшебный обод Правосудия]",
    '0\\xab': "[Чарующий обод Правосудия]",
    '1\\xab': "[Дивный обод Правосудия]",
}

spring_accessories_32 = {
    '-\\x87': "[Волшебная накидка Несокрушимости]",
    '.\\x87': "[Чарующая накидка Несокрушимости]",
    '/\\x87': "[Волшебная хламида Несокрушимости]",
    '0\\x87': "[Чарующая хламида Несокрушимости]",
    '1\\x87': "[Волшебный плащ Несокрушимости]",
    '2\\x87': "[Чарующий плащ Несокрушимости]",
    '3\\x87': "[Волшебный хитон Несокрушимости]",
    '4\\x87': "[Чарующий хитон Несокрушимости]",
    '\\xc5\\x91': "[Дивная накидка Несокрушимости]",
    '\\xc6\\x91': "[Дивный хитон Несокрушимости]",

    '%\\x87': "[Волшебный медальон Несокрушимости]",
    '&\\x87': "[Чарующий медальон Несокрушимости]",
    "\\'\\x87": "[Волшебное ожерелье Несокрушимости]",
    '(\\x87': "[Чарующее ожерелье Несокрушимости]",
    ')\\x87': "[Волшебный амулет Несокрушимости]",
    '*\\x87': "[Чарующий амулет Несокрушимости]",
    '+\\x87': "[Волшебный кулон Несокрушимости]",
    ',\\x87': "[Чарующий кулон Несокрушимости]",
    '\\xc3\\x91': "[Дивный медальон Несокрушимости]",
    '\\xc4\\x91': "[Дивный кулон Несокрушимости]",
    '\\x1d\\x87': "[Волшебное кольцо Несокрушимости]",
    '\\x1e\\x87': "[Чарующее кольцо Несокрушимости]",
    '\\x1f\\x87': "[Волшебная печатка Несокрушимости]",
    ' \\x87': "[Чарующая печатка Несокрушимости]",
    '!\\x87': "[Волшебный перстень Несокрушимости]",
    '"\\x87': "[Чарующий перстень Несокрушимости]",
    '#\\x87': "[Волшебный лимб Несокрушимости]",
    '$\\x87': "[Чарующий лимб Несокрушимости]",
    '\\xc1\\x91': "[Дивное кольцо Несокрушимости]",
    '\\xc2\\x91': "[Дивный лимб Несокрушимости]",

    'z\\x9f': "[Волшебный обруч Несокрушимости]",
    '{\\x9f': "[Чарующий обруч Несокрушимости]",
    '|\\x9f': "[Волшебный кафф Несокрушимости]",
    '}\\x9f': "[Чарующий кафф Несокрушимости]",
    '~\\x9f': "[Волшебный браслет Несокрушимости]",
    '\\x7f\\x9f': "[Чарующий браслет Несокрушимости]",
    '\\x80\\x9f': "[Волшебный обод Несокрушимости]",
    '\\x81\\x9f': "[Чарующий обод Несокрушимости]",
    'J\\xab': "[Дивный обруч Несокрушимости]",
    'K\\xab': "[Дивный обод Несокрушимости]",
}
