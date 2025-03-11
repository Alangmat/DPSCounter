from mapping import arabic, cyrillic, items
from datetime import datetime


def time_now():
    return datetime.now().strftime("%H:%M:%S")

# def parse_packet(data_str):
#     decoded = ""
#     byte_counter = 0
#     counter = 0
#     data_str = str(data_str)
#     for i in range(len(data_str) - 1):
#         if counter:
#             if counter == 1:
#                 decoded += data_str[i]
#                 decoded += "ц"
#                 counter -= 1
#             else:
#                 decoded += data_str[i]
#                 counter -= 1
#         elif data_str[i] == "x" and (((not data_str[i + 1].isalpha()) and data_str[i-1].isalpha() and data_str[i-2].isalpha()) or ((data_str[i + 1].isalpha()) and (data_str[i + 2].isalpha()) and data_str[i-1].isalpha() and data_str[i-2].isalpha())):
#             decoded += data_str[i]
#             decoded += "ц"
#             byte_counter += 1
#         elif data_str[i] == "\\":
#             if data_str[i + 1] == "x" and data_str[i+2] != '\\' and data_str[i+3] != '\\':
#                 counter += 3
#                 decoded += data_str[i]
#                 byte_counter += 1
#             else:
#                 decoded += data_str[i]
#                 counter += 1
#                 byte_counter += 1
#         elif data_str[i] == "x" and data_str[i+1] != '\\' and data_str[i+2] != '\\':
#             counter += 2
#             decoded += data_str[i]
#             byte_counter += 1
#         else:
#             decoded += data_str[i]
#             decoded += "ц"
#     decoded = decoded.split("ц")
#     if "'" in decoded:
#         decoded = decoded[decoded.index("'"):]
#     return decoded

def parse_packet(data_str):
    decoded = ""
    byte_counter = 0
    counter = 0
    data_str = str(data_str)
    
    for i in range(len(data_str) - 1):
        if counter:
            if counter == 1:
                decoded += data_str[i]
                decoded += "ц"
                counter -= 1
            else:
                decoded += data_str[i]
                counter -= 1
        elif data_str[i] == "x" and (((not data_str[i + 1].isalpha()) and data_str[i-1].isalpha() and data_str[i-2].isalpha()) or ((data_str[i + 1].isalpha()) and (data_str[i + 2].isalpha()) and data_str[i-1].isalpha() and data_str[i-2].isalpha())):
            decoded += data_str[i]
            decoded += "ц"
            byte_counter += 1
        elif data_str[i] == "\\":
            if data_str[i + 1] == "x"  and data_str[i+2] != '\\' and data_str[i+3] != '\\':
                counter += 3
                decoded += data_str[i]
                byte_counter += 1
            else:
                decoded += data_str[i]
                counter += 1
                byte_counter += 1
        elif data_str[i] == "x" and i + 2 < len(data_str) and data_str[i+1] != '\\' and data_str[i+2] != '\\':
            counter += 2
            decoded += data_str[i]
            byte_counter += 1
        else:
            # Добавляем экранирование для одинарной кавычки
            if data_str[i] == "'":
                decoded += "\\'"  # Экранируем кавычку
            else:
                decoded += data_str[i]
            decoded += "ц"
            # decoded += data_str[i]
            # decoded += "ц"
    
    # Разделяем строку по "ц"
    decoded = decoded.split("ц")
    
    # Убираем логику удаления данных при встрече с кавычкой
    # Просто возвращаем разобранный массив
    return decoded

# def parse_packet(data_str):
#     decoded = ""
#     byte_counter = 0
#     counter = 0
#     data_str = str(data_str)
    
#     for i in range(len(data_str) - 1):
#         if counter:
#             if counter == 1:
#                 decoded += data_str[i]
#                 decoded += "ц"
#                 counter -= 1
#             else:
#                 decoded += data_str[i]
#                 counter -= 1
#         elif data_str[i] == "x" and (((not data_str[i + 1].isalpha()) and data_str[i-1].isalpha() and data_str[i-2].isalpha()) or ((data_str[i + 1].isalpha()) and (data_str[i + 2].isalpha()) and data_str[i-1].isalpha() and data_str[i-2].isalpha())):
#             decoded += data_str[i]
#             decoded += "ц"
#             byte_counter += 1
#         elif data_str[i] == "\\":
#             if data_str[i + 1] == "x" and data_str[i+2] != '\\' and data_str[i+3] != '\\':
#                 counter += 3
#                 decoded += data_str[i]
#                 byte_counter += 1
#             else:
#                 # Проверяем, чтобы экранирование не происходило дважды
#                 if data_str[i + 1] != "\\":
#                     decoded += "\\\\"  # Преобразуем один слэш в два
#                 else:
#                     decoded += "\\"  # Если уже экранирован, просто добавляем слэш
#                 counter += 1
#                 byte_counter += 1
#         elif data_str[i] == "x" and data_str[i+1] != '\\' and data_str[i+2] != '\\':
#             counter += 2
#             decoded += data_str[i]
#             byte_counter += 1
#         else:
#             # Экранирование одинарной кавычки только при необходимости
#             if data_str[i] == "'":
#                 decoded += "\\'"  # Экранируем кавычку
#             else:
#                 decoded += data_str[i]
#             decoded += "ц"
    
#     # Разделяем строку по "ц"
#     decoded = decoded.split("ц")
    
#     return decoded


def chat_struct(packet):
    struct = info_struct(packet)[0]
    info = info_struct(packet)[1]
    last_id_index = info_struct(packet)[2]

    try:
        struct["text_len"] = arabic[info[last_id_index+3+struct["nick_len"]+6:][0]]
    except:
        struct["text_len"] = arabic[info[last_id_index+3+struct["nick_len"]+6:][0]]+3
    text = ''
    for i in range(last_id_index+2+struct["nick_len"]+8,last_id_index+2+struct["nick_len"]+8+struct["text_len"]*2,2):
        if 'x04' in info[i]+info[i+1]:
            try:
                text += cyrillic[info[i]+info[i+1]]
            except:
                text += info[i]+info[i+1]
        elif 'x00' in info[i]+info[i+1]:
            try:
                text += (info[i]+info[i+1]).replace('\\x00', '')
            except:
                text += info[i]+info[i+1]
    struct["text"] = text
    return struct



def money_struct(packet):
    struct = info_struct(packet)[0]
    info = info_struct(packet)[1]
    last_id_index = info_struct(packet)[2]

    struct["text_len"] = arabic[info[last_id_index + struct["nick_len"] + 9:][0]]
    amount = ''
    for i in range(last_id_index + struct["nick_len"] + 8, last_id_index + struct["nick_len"] + 9 + struct["text_len"] * 2, 2):
        if 'x00' in info[i] + info[i + 1]:
            try:
                amount += (info[i] + info[i + 1]).replace('\\x00', '')
            except:
                amount += info[i] + info[i + 1]
    struct["amount"] = amount
    return struct


def item_struct(packet):
    struct = info_struct(packet)[0]
    info = info_struct(packet)[1]
    last_id_index = info_struct(packet)[2]

    last_text_index = 0
    for i in range(len(info[last_id_index + 1 + struct["nick_len"] + 8:])):
        if info[last_id_index + 1 + struct["nick_len"] + 8:][i] == "\\x00":
            last_text_index = last_id_index + 1 + struct["nick_len"] + 8 + i
            break

    count = ''
    for i in range(last_id_index + 1 + struct["nick_len"] + 9, len(info), 2):
        try:
            if 'x00' in info[i] + info[i + 1]:
                count += (info[i] + info[i + 1]).replace('\\x00', '')
            else:
                break
        except:
            break
    struct["count"] = int(count)
    item_name = ''
    for i in range(last_id_index + 1 + struct["nick_len"] + 9 + len(count)*2, last_id_index + 1 + struct["nick_len"] + 9 + 2 + len(count)*2, 2):
        item_name += info[i] + info[i + 1] + info[i + 2]
    try:
        struct["item_name"] = items[item_name]
    except:
        print(f"Нет ID предмета [{item_name}]")
    return struct


def info_struct(packet):

    info = parse_packet(packet)
    info.pop(-1)
    if info[0] == "'" or info[0] == '"':
        info.pop(0)
    if (info[1] == "'" or info[0] == '"') and info[0] == 'b':
        info.pop(0)
        info.pop(0)
    last_id_index = 0
    for i in range(len(info[5:])):
        if info[5:][i] == "\\x00":
            last_id_index = i + 5
            break
    struct = {
        "mark": info[0],
        "type": info[2],
        "flag": info[5] + info[6],
        "ID": "".join(info[7:last_id_index]),
        "nick_len": arabic[info[last_id_index+1]]
    }
    #print(struct)
    struct["nick"] = ''.join(info[last_id_index+2:last_id_index+2+struct["nick_len"]])
    #print(struct)
    struct["lvl"] = arabic[info[last_id_index + 2 + struct["nick_len"]:][0]]
    return struct, info, last_id_index


#data = b'A"> \x07[\x05\x11\x045G\x00\x08Tokiosex"@\x02\x00\x00\x03\x06\x021\x00\x04\xe9\x11\x13\t\x10\x08|\x16\xf6\x05\x00\x11\n'
#data = b'A#>!\x07Y\x05\x11\x045G\x00\x08Tokiosex"@\x02\x00\x00\x03\x06\x042\x000\x000\x000\x00\x14\r\x08\x0b\xf0 \xf6\x05\x1c\x8bK\x00\x06\x08\t'

#data = b'U\x00[\x0b\x00\x00\x8dZ\xf6\x05$\xd2\xf6\x05\x01W\x00\xab\x03\r<\x01\x00\x00\x8dZ\xf6\x05$\xd2\xf6\x05\x11\xac\x03\x12\x00\x00e\x00\x8dZ\xf6\x05\x1c\x00\x00\x00t'#\x00\x00\xcb\x01V\x00'

#print(item_struct(data))
#print(parse_packet(data))


# DATA: b'A#>!\x07Y\x05\x11\x045G\x00\x08Tokiosex"@\x02\x00\x00\x03\x06\x042\x000\x000\x000\x00\x14\r\x08\x0b\xf0 \xf6\x05\x1c\x8bK\x00\x06\x08\t'
# DATA: b'A"> \x07[\x05\x11\x045G\x00\x08Tokiosex"@\x02\x00\x00\x03\x06\x021\x000\x00\x04\xe9\x11\x13\t\x10\x08|\x16\xf6\x05\x00\x11\n'

