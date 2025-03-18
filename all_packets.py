from scapy.all import sniff, IP, TCP, sendp, Raw, show_interfaces
from mailing import time_now, parse_packet
import struct
import config
from convert_packets import *
from start import start, get_warspear_ip_port
import threading
import keyboard
import time
import sqlite3
from actions_db import get_heroes
from datetime import datetime
import testfile


show_interfaces()

start()
print(config.INTERFACE_USER)

def segmentation(data):
    split_marker_U = b'U\x00'
    split_marker_damage = b'\xab\x03\r'
    split_marker_create_luna = b'\x1a)\x087'
    segments = []
    current_segment = bytearray()
    i = 0 
    while i < len(data):
        # Пакет с уроном
        if data[i:i+3] == split_marker_damage:
            if current_segment:
                segments.append(bytes(current_segment))
            current_segment = bytearray(data[i:i+7])
            i += 7
        # Пакет с кошкой
        elif data[i:i+4] == split_marker_create_luna:
            if current_segment:
                segments.append(bytes(current_segment))
            current_segment = bytearray(data[i:i+4]) 
            i += 4
        elif data[i:i+2] == split_marker_U:
            if current_segment:
                segments.append(bytes(current_segment))
            current_segment = bytearray(data[i:i+2]) 
            i += 2
        else:
            current_segment.append(data[i])
            i += 1

    if current_segment:
        segments.append(bytes(current_segment))
    
    return segments



def byte_string_to_int(byte_str):
    # Преобразование строкового байта (например, '\\x15') в числовое значение
    if byte_str.startswith('\\x'):
        return int(byte_str[2:], 16)  # Преобразовать шестнадцатеричное значение
    elif byte_str.startswith('\\'):
        return ord(byte_str[1])  # Преобразовать экранированный символ (например, '\\r')
    else:
        return ord(byte_str)  # Преобразовать обычный символ
    
def bytes_to_int(byte_str):
    return struct.unpack('<I', byte_str)[0]

def list_to_bytes(char_list):
    # Преобразуем элементы списка в байты
    byte_list = [eval(f"b'{char}'") for char in char_list]
    
    # Соединяем все байты в один объект типа bytes
    return b''.join(byte_list)


    
def get_gamage(packet):
    global total_damage
    number = None
    
    for i in range(len(packet) - 7):
        currents = []
        # print(f'{packet[i]} ------ {packet[i + 5]}')
        # print(f'{packet[i] == '\\r'} ------ {packet[i + 5] == '\\xe9'}')
        #["\\xf9", "\\xc9", "\\xf6"]
        if (packet[i] == '\\xab') and (packet[i + 1] == '\\x03') and (packet[i + 2] == '\\r'): #and ((packet[i + 7] == '\\xe9') or packet[i + 7] == '\\xca' or packet[i + 7] == ',' or packet[i + 7] == '\\x98'):
            #print(packet)
            currents.append(packet[i + 3])
            currents.append(packet[i + 4])
            currents.append(packet[i + 5])
            currents.append(packet[i + 6])
            #print(currents)
            #number_bytes = [bytes_to_int(b) for b in currents]
                        # Преобразуем 4 байта в число в формате little-endian
            #numbers = int.from_bytes(number_bytes, byteorder='little')
            #total_damage = total_damage + int(numbers)
            bytes = list_to_bytes(currents)
            # print(bytes)
            #print(bytes)
            #print(len(bytes))
            # if len(bytes) == 4:
            if number is None:
                number = bytes_to_int(bytes)
                
                # print(number)
            else:
                number = number + bytes_to_int(bytes)


    return number
    #print("-")

def connect_beastmaster_luna(parsed_packet):
    global beast_masters_lists
    # print("вызов connect_beastmaster_luna")
    # print(f"{parsed_packet}")
    for key in beast_masters_lists.keys():
        # print(key)
        if f"{parsed_packet[-14]}{parsed_packet[-13]}{parsed_packet[-12]}" == key:
            print(f"Луна добавлена игроку {nickname_dict[key]} {parsed_packet[-5] + parsed_packet[-4] + parsed_packet[-3]}")
            beast_masters_lists[key] = (parsed_packet[-5] + parsed_packet[-4] + parsed_packet[-3])
    return 0


def handle_packet(packet):
    if IP in packet and TCP in packet:
        if (packet[IP].src == config.IP_SERVER and packet[IP].dst == config.IP_USER and
                packet[TCP].sport == config.PORT_SERVER):
            payload = packet[TCP].payload
            global total_damage
            global prev_byte
            global flag
            if payload:
                data = payload.load
                # print(data)
                segments = segmentation(data)

                i_segment = 0
                while i_segment < len(segments):
                    segment = segments[i_segment]
                    i_segment += 1
                    if (len(segment) > 3):
                        parsed_packet = parse_packet(segment)
                    else:
                        parsed_packet = []

                    if len(parsed_packet) > 5:
                        if f"{parsed_packet[2]}{parsed_packet[3]}{parsed_packet[4]}" == "\\xab\\x03\\r":
                            converted = convert(parsed_packet)
                            
                            if converted is not None and len(converted) >= 13:
                                damage = get_gamage(converted)

                                if damage is not None:
                                    flag = True
                                    prev_byte = None

                                    # Источник урона
                                    id_damage_source = f"{converted[-6]}{converted[-5]}{converted[-4]}"

                                    # айди цели
                                    id_goal = f"{converted[-3]}{converted[-2]}{converted[-1]}"

                                    with damage_dict_lock:
                                        heroes = get_heroes()
                                        if id_damage_source in beast_masters_lists.values():
                                            id_hero = next(k for k, v in beast_masters_lists.items() if v == id_damage_source)
                                            if id_hero in damage_dict.keys():
                                                damage_dict[id_hero] += damage
                                                if id_hero not in damages_lists:
                                                    damages_lists[id_hero] = {}  # Создаём вложенный словарь для нового источника урона

                                                if id_goal in damages_lists[id_hero]:
                                                    damages_lists[id_hero][id_goal] += damage
                                                else:
                                                    damages_lists[id_hero][id_goal] = damage
                                                # if id_hero in damages_lists.keys():
                                                #     if id_goal in damages_lists[id_hero].keys():
                                                #         damages_lists[id_hero][id_goal] += damage
                                                #     else:
                                                #         damages_lists[id_hero][id_goal] = damage
                                            else:
                                                damage_dict[id_hero] = damage
                                            nickname = next((n for id, n in heroes if id == id_hero), None)
                                            if nickname is not None:
                                                print(f"{nickname} - {damage_dict[id_hero]}")
                                                write_data_file(nickname, id_goal, damage)
                                                

                                        else:
                                            for id, nick in heroes:
                                                if id_damage_source == id:
                                                    if id_damage_source in damage_dict.keys():
                                                        damage_dict[id_damage_source] += damage
                                                        if id_damage_source not in damages_lists:
                                                            damages_lists[id_damage_source] = {}  # Создаём вложенный словарь для нового источника урона

                                                        if id_goal in damages_lists[id_damage_source]:
                                                            damages_lists[id_damage_source][id_goal] += damage
                                                        else:
                                                            damages_lists[id_damage_source][id_goal] = damage
                                                        # if id_damage_source in damages_lists.keys():
                                                        #     if id_goal in damages_lists[id_damage_source].keys():
                                                        #         damages_lists[id_damage_source][id_goal] += damage
                                                        #     else:
                                                        #         damages_lists[id_damage_source][id_goal] = damage
                                                    else:
                                                        damage_dict[id_damage_source] = damage
                                                    print(f"{nick} - {damage_dict[id]}")
                                                    write_data_file(nick, id_goal, damage)
                                                

                                        # if id_damage_source in damage_dict.keys():
                                        #     damage_dict[id_damage_source] += damage
                                        #     print(f"{nickname_dict[id_damage_source]} - {damage_dict[id_damage_source]}")
                                        # elif id_damage_source in beast_masters_lists.values():
                                        #     id_hero = next(k for k, v in beast_masters_lists.items() if v == id_damage_source)
                                        #     damage_dict[id_hero] += damage
                                        #     print(f"{nickname_dict[id_hero]} - {damage_dict[id_hero]}")
                            else:
                                if not flag:
                                    prev_byte = bytes(segment)
                                else: prev_byte = None
                                flag = not flag
                        elif f"{parsed_packet[2]}{parsed_packet[3]}{parsed_packet[4]}{parsed_packet[5]}" == "\\x1a)\\x087":
                            converted = convert(parsed_packet)
                            if converted is not None:
                                connect_beastmaster_luna(converted)
                                prev_byte = None
                                flag = True
                        if (prev_byte is not None) and (not flag):
                            next_segment = bytes(prev_byte + segment)
                            segments.insert(segments.index(segment) + 1, next_segment) 
                            flag = True
                            prev_byte = None
                        if (not flag) and (prev_byte is None) and (parsed_packet[2] == "\\xab" and parsed_packet[3] == "\\x03" and parsed_packet[4] == "\\r"):
                            prev_byte = bytes(segment)
                            flag = True
                        else:
                            flag = False
                            prev_byte = None

                                    


        # if (packet[IP].src == config.IP_USER and packet[IP].dst == config.IP_SERVER and
        #         packet[TCP].dport == config.PORT_SERVER):
        #     packet[TCP].payload = Raw(b'\x08\x07\x1b\x0f\x16\x0fj_\x80\x07\x05\x1b\x0fj_\x80')
        #     payload = packet[TCP].payload
        #     if payload:  # Проверяем, есть ли данные в поле payload
        #         data = payload.load  # Получаем данные
        #         print(f"[{time_now()}]: {data}")


        # if (packet[IP].src == "192.168.0.102" and packet[IP].dst == "85.17.202.49" and
        #         packet[TCP].sport == 57136 and packet[TCP].dport ==15102 ):
        #     payload = packet[TCP].payload
        #     if payload:  # Проверяем, есть ли данные в поле payload
        #         if Raw in payload:
        #             data = payload[Raw].load  # Получаем данные
        #             print(f"[{time_now()}][>>]: {data}")
        #         else:
        #             print(f"[{time_now()}][>>]: данных нет")

        # if (packet[IP].src == config.IP_SERVER and packet[IP].dst == config.IP_USER and
        #         packet[TCP].sport == config.PORT_SERVER):
        #     payload = packet[TCP].payload
        #     if payload:  # Проверяем, есть ли данные в поле payload
        #         data = payload.load  # Получаем данные
        #         parsed_packet = parse_packet(data)
        #         for i in range(1, len(parsed_packet)):
        #             #if parsed_packet[i - 1] == '\\xca' and parsed_packet[i] == 'C':
        #             if parsed_packet[i - 1] == 'U' and parsed_packet[i] == '\\x00':
        #                 #print(f"[{time_now()}][<<]: {payload.load}")

        #                 # Преобразуем 4 байта в число в формате little-endian
        #                 # number_bytes = [byte_string_to_int(b) for b in ['\\x7f', '\\n', '\\x00', '\\x00',]]
        #                 # number = int.from_bytes(number_bytes, byteorder='little')
        #                 # print(number)
        #                 #get_gamage()
        #                 damage = get_gamage(parsed_packet)
        #                 if damage is not None:
        #                     print(parse_packet(data))
        #                     print(damage)
        #                 break

        # if (packet[IP].src == config.IP_SERVER and packet[IP].dst == config.IP_USER and
        #         packet[TCP].sport == config.PORT_SERVER):
        #     if Raw in packet:  # Проверяем, есть ли слой Raw
        #         payload = packet[Raw].load  # Получаем полезную нагрузку
        #         print(f"[{time_now()}][<<]: {payload}")

        # if (packet[IP].src == config.IP_SERVER and packet[IP].dst == config.IP_USER and
        #         packet[TCP].sport == config.PORT_SERVER):
        #     payload = packet[TCP].payload
        #     global total_damage
        #     if payload:  # Проверяем, есть ли данные в поле payload
        #         data = payload.load  # Получаем данные
        #         # print("=======================")

        #         # Разделение пакетов
        #         # Разбиваем строку на массив байтов
        #         split_marker = b'U\x00'
        #         split_marker2 = b'I\x03'
        #         split_marker_create_luna = b'\x1a)\x087'
        #         segments = []
        #         current_segment = bytearray()
        #         global prev_byte
        #         global flag

        #         # print(data)
        #         # print(f"prev = {prev_byte}")

        #         i = 0
        #         while i < len(data):
        #             # Проверяем, что нашли байты U\x00
        #             if data[i:i+2] == split_marker:
        #                 if current_segment:
        #                     segments.append(bytes(current_segment))  # Добавляем текущий сегмент
        #                 current_segment = bytearray(data[i:i+2])  # Начинаем новый сегмент с маркера
        #                 i += 2  # Пропускаем 2 байта маркера
        #             elif data[i:i+4] == split_marker_create_luna:
        #                 if current_segment:
        #                     segments.append(bytes(current_segment))  # Добавляем текущий сегмент
        #                 current_segment = bytearray(data[i:i+4])  # Начинаем новый сегмент с маркера
        #                 i += 4  # Пропускаем 2 байта маркера
        #             else:
        #                 current_segment.append(data[i])  # Добавляем текущий байт (целое число)
        #                 i += 1  # Переходим к следующему байту

        #         # Добавляем последний сегмент
        #         if current_segment:
        #             segments.append(bytes(current_segment))

        #         i_segment = 0
        #         while i_segment < len(segments):
        #             segment = segments[i_segment]
        #             i_segment += 1
        #             # flag = False
        #             if len(segment) > 1000:
        #                 break
        #             # print(f"[{time_now()}][<<]: {segment}")

        #             parsed_packet = parse_packet(segment)
        #             if len(parsed_packet) > 3:
        #                 # print(f"[{time_now()}][<<]: {segment}")
        #                 # for i in range(len(parsed_packet) - 10):
        #                     #print()
        #                     #if f'{parsed_packet[i]}{parsed_packet[i + 1]}{parsed_packet[i + 2]}' == '\\xe9{K':
        #                     #if (parsed_packet[i] == '\xe9') and (parsed_packet[i + 1] == '{'): 
        #                 if parsed_packet[2] == 'U' and parsed_packet[3] == '\\x00':# and parsed_packet[4] == '[' and parsed_packet[5] == '\\x0b':
        #                 # if parsed_packet[2] == 'I' and parsed_packet[3] == '\\x03':# and parsed_packet[4] == '[' and parsed_packet[5] == '\\x0b':
        #                     #print(i)
        #                 # if parsed_packet[i] == '\\xe9':

        #                     # Преобразуем 4 байта в число в формате little-endian
        #                     # number_bytes = [byte_string_to_int(b) for b in ['\\x7f', '\\n', '\\x00', '\\x00',]]
        #                     # number = int.from_bytes(number_bytes, byteorder='little')
        #                     # print(number)
        #                     #get_gamage()
        #                     #print(parse_packet(data))

        #                     #print("===================")
        #                     # print(f"[{time_now()}][<<]: {parsed_packet}")

        #                     # print(data)
        #                     # for i in range(len(parsed_packet) - 3):
        #                     #     if (parsed_packet[i] == '\\xe9') and (parsed_packet[i + 1] == '}') and (parsed_packet[i] == 'K'):
        #                     #         print(data)


        #                     converted = convert_packet(parsed_packet)
        #                     # print(f"[{time_now()}][<<]: {segment}")
                            
        #                     if converted is not None and len(converted) > 10:
        #                         # print("1")
        #                         #print(converted)
        #                         # if f'{converted[-2]}{converted[-1]}' in killed_id:
        #                         #     if killed_id[f'{converted[-2]}{converted[-1]}'] == True:
        #                         #         break

        #                         # if converted[-4] == '{' and converted[-3] == 'K':
        #                         damage = get_gamage(converted)
        #                     # damage = get_gamage(parsed_packet)
        #                         if damage is not None:
        #                             # print("2")
        #                             # if (converted[-5] == '\\xe9') and (converted[-4] == '}') and (converted[-3] == 'K'):
        #                             # print(f"{converted[-5]}{converted[-4]}{converted[-3]} - {beast_masters_lists['\\xe9}K']}")
        #                             if (f"{converted[-5]}{converted[-4]}{converted[-3]}" == "\\xe9}K") or (f"{converted[-5]}{converted[-4]}{converted[-3]}" == beast_masters_lists['\\xe9}K']):
        #                                 # if contains_sequence(parsed_packet, ["\\xf9", "\\xc9", "\\xf6"]):
        #                                 # print(f"[{time_now()}][<<]: {parsed_packet}")
        #                                 # total_damage = total_damage + damage
        #                                 print(damage)
        #                                 damage_list[0] = damage_list[0] + damage
        #                                 print(f"АЛАНГМАТОР - {damage_list[0]}")
        #                                 # print(f'ИТОГОВЫЙ УРОН - {total_damage}')
        #                                 flag = True
        #                                 prev_byte = None
        #                                 # print(converted)

        #                                 # после разделения пакетов не нужен по идее
        #                                 # ВАЖНЫЙ БРЭЙК НЕ ДАЕТ ДУБЛИРОВАТЬСЯ ПРИ УБИЙСТВЕ СКИЛЛОМ
        #                                 # break
        #                             elif (f"{converted[-5]}{converted[-4]}{converted[-3]}" == "+\\x81K") or (f"{converted[-5]}{converted[-4]}{converted[-3]}" == beast_masters_lists['+\\x81K']):
        #                                 print(damage)
        #                                 damage_list[1] = damage_list[1] + damage
        #                                 print(f"СЕПАРАТОР - {damage_list[1]}")
        #                                 flag = True
        #                                 prev_byte = None
        #                         # else:
        #                         #     prev_byte = segment
        #                         #     flag = False
        #                     else:
        #                         if not flag:
        #                             prev_byte = bytes(segment)
        #                         else: prev_byte = None
        #                         flag = not flag
        #                 elif parsed_packet[2] == '\\x1a' and parsed_packet[3] == ')':
        #                     if len(parsed_packet) > 8:
        #                         # if parsed_packet[4] == '\\x02' and parsed_packet[5] == '\\x08' and parsed_packet[6] == '\\x03' and parsed_packet[7] == '\\xee':
        #                         if parsed_packet[4] == '\\x08' and parsed_packet[5] == '7':
        #                             connect_beastmaster_luna(parsed_packet)
        #                             prev_byte = None
        #                             flag = True
        #                 else:
        #                     if (prev_byte is not None) and (not flag):
        #                         next_segment = bytes(prev_byte + segment)
        #                         # print(i_segment)
        #                         # print(next_segment)
        #                         # print(segments)
        #                         segments.insert(segments.index(segment) + 1, next_segment) 
        #                         # print(segments)
        #                         # prev_byte = segment
        #                         flag = True
        #                         # segments.pop(segments.index(segment))
        #                         prev_byte = None
        #                 if not flag:
        #                     if prev_byte is None:
        #                         if (parsed_packet[2] == 'U') and (parsed_packet[3] == '\\x00'):
        #                             prev_byte = bytes(segment)
        #                             flag = True
        #                 else:
        #                     flag = False
        #                     prev_byte = None
                                


                                        #print("===================")

                # print("=======================")

def write_data_file(nickname, id_goal, damage):
    # Получаем текущее время
    current_time = datetime.now()

    # Форматируем время в строку "HH:MM:SS"
    time_string = current_time.strftime("%H:%M:%S")
    res = f"{time_string} - {damage}"
    
    if nickname in data_for_file.keys():
        if id_goal in data_for_file[nickname].keys():
            data_for_file[nickname][id_goal].append(res)
        else:
            data_for_file[nickname][id_goal] = [res]
    else:
        data_for_file[nickname] = { id_goal: [res] }




def reset_damage_dict():
    global damage_dict
    global damages_lists
    global data_for_file
    with damage_dict_lock:
        data_for_file = {}
        for key in damage_dict:
            # print(f"{damage_dict[key]}")
            damage_dict[key] = 0
    with damages_lists_lock:
        for k in damages_lists.keys():
            damages_lists[k] = {}
    print("damage_dict был сброшен до нуля.")


def listen_keys():
    global start_date
    global final_date
    # Бесконечный цикл для отслеживания нажатия клавиш
    while True:
        try:
            # Проверяем, нажата ли комбинация Ctrl+Shift+U
            if keyboard.is_pressed('tab'):
                final_date = datetime.now()
                diff = final_date - start_date
                seconds = diff.total_seconds()
                print(seconds)
                if seconds < 1: seconds = 1
                heroes = get_heroes()
                print("\n========Итоговый урон========\n")
                for k in damage_dict.keys():
                    print(f"{next((n for id, n in heroes if id == k), None)}: ДПС = {damage_dict[k] / seconds} | ДПМ = {damage_dict[k] / seconds * 60}")
                    print(f"{next((n for id, n in heroes if id == k), None)} - {damage_dict[k]}")
                    if k in damages_lists.keys():
                        print("--Урон по целям--")
                        sorted_goals = dict(list(sorted(damages_lists[k].items(), key=lambda item: item[1], reverse=True)[:2]))
                        for id_goal, dd in sorted_goals.items():
                            print(f"\t{dd}\t- {id_goal}")
                        print("-----------------\n")
                testfile.save_data_to_files(data_for_file, damage_dict, seconds)
                reset_damage_dict()
                start_date = datetime.now()
                # Добавляем задержку, чтобы избежать многократных срабатываний при длительном нажатии
                time.sleep(1)
            # Короткая задержка, чтобы снизить нагрузку на процессор
            time.sleep(0.1)
        except:
            break  # В случае ошибки (например, прерывание), выходим из цикла


#===============================================
#========ОСНОВНОЙ БЛОК==========================
#=====================С ПЕРЕМЕННЫМИ=============
#===============================================
#===============================================
start_date = datetime.now()
final_date = None

prev_byte = None
prev_damage_byte = None
flag = False
total_damage = 0
killed_id = []
damage_dict = {
    "\\xe9}K": 0,
    "+\\x81K": 0,
    "\\xe1<R": 0,
}
damages_lists = {
    "\\xe9}K": {},
}
nickname_dict = {
    "\\xe9}K": "Alangmat",
    "+\\x81K": "Cenapamop",
    "\\xe1<R": "Cenapanop",
}
damage_list = [0, 0]
beast_masters_lists = {
                       "\\xe9}K": None,
                       "+\\x81K": None,
                       "\\xe1<R" : None,
                       "!#;": None,
                    #    "(\\x9cM": None,
                       }

data_for_file = {

}

damage_dict_lock = threading.Lock()
damages_lists_lock = threading.Lock()


key_thread = threading.Thread(target=listen_keys, daemon=True)
key_thread.start()
# Настройка фильтра для захвата только IP и TCP трафик
sniff(iface=config.INTERFACE_USER, prn=handle_packet, filter="ip and tcp", store=0)
#15102

#b'U\x00[\x0b\x00\x00\xe9}K\x00\x83\x06\xf6\x05\x01W\x00\xab\x03\r|\x01\x00\x00\xe9}K\x00\x83\x06\xf6\x05\x11V\x00\x1c\x05\x01\xe9}K\x00\x1c\x05\x01\x83\x06\xf6\x05@\x1e\xe9}K\x00\x04\x05\x00\x14\x00\x1f\x00\x1a\x00\x04.\x1c\x00\x00\x8c\x14\x00\x00\xea\x0f\x00\x00\x00\x00\x00\x00\x1d\x05 \x83\x06\xf6\x05'
#b'U\x00[\x0b\x00\x00\xe9}K\x00\x83\x06\xf6\x05\x01W\x00\xab\x03\rl\x03\x00\x00\xe9}K\x00\x83\x06\xf6\x05\x15V\x00'
#айди моего перса
#'\\xe9', '}'

# b"U\x00[\x0b\x00\x00\x8dZ\xf6\x05$\xd2\xf6\x05\x01W\x00\xab\x03\r<\x01\x00\x00\x8dZ\xf6\x05$\xd2\xf6\x05\x11\xac\x03\x12\x00\x00e\x00\x8dZ\xf6\x05\x1c\x00\x00\x00t'\x00\x00\xcb\x01V\x00"







# ip = IP(src="172.16.186.6", dst="85.17.202.49")
# tcp = TCP(sport=packet[TCP].sport, dport=15102, flags="S")
# payload = Raw(b'\x08\x07\x0f\x0f\x0f\x0fj_\x80')
# packet = ip / tcp / payload
#
# ethernet = Ether(dst="00:00:5e:00:01:7f", src="90:de:80:a0:34:c0", type=0x0800)
#
# full_packet = ethernet / packet
#
# sendp(full_packet)




# data = payload.load  # Получаем данные
# new_data = data.replace(data, b"")
# packet[TCP].payload.load = new_data
# del packet[IP].chksum
# del packet[TCP].chksum
# data = payload.load



















# from scapy.all import sniff, IP, TCP
# from mailing import *
#
#
# def packet_callback(packet):
#     if IP in packet and TCP in packet:
#         if packet[IP].src == "85.17.202.49" and packet[TCP].sport == 15102:
#             payload = packet[TCP].payload
#             if payload:  # Проверяем, есть ли данные в поле payload
#                 data = payload.load  # Получаем данные
#                 print(f"[{time_now()}]: {data}")
#
# sniff(filter="ip", prn=packet_callback, store=False)