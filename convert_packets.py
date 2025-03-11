from scapy.all import sniff, IP, TCP, sendp, Raw
from mailing import time_now, parse_packet

def contains_sequence(lst, sequence):
    # Преобразуем список в строку, разделяя элементы пробелами
    lst_str = ' '.join(lst)
    sequence_str = ' '.join(sequence)
    
    # Проверяем, содержится ли строка sequence_str в строке lst_str
    return sequence_str in lst_str

def convert_packet(parsed_packet):
    result = []
    # for i in range(len(parsed_packet) - 3):
    #     if parsed_packet[i] == '\\xe9' and parsed_packet[i + 1] == '}' and parsed_packet[i + 2] == 'K':
    #         print(parsed_packet)
    #print("===================================")
    #print(parsed_packet)
    if parsed_packet[0] == "'":
        parsed_packet.pop(0)
    for i in range(len(parsed_packet) - 1):
        # Добавляем обозначение пакета с действием персонажа
        if parsed_packet[i] == 'U' and parsed_packet[i + 1] == '\\x00':
            # Вырезаем отрывок предыдущего пакета
            parsed_packet = parsed_packet[i:]
            #print(parsed_packet)
            result.append(parsed_packet[0])
            result.append(parsed_packet[1])
            #print(result)
            break
    # if len(parsed_packet) > 13:
    # # Автоатака
    #     if parsed_packet[2] == '[' and parsed_packet[3] == '\\x0b':
    #         result.append(parsed_packet[2])
    #         result.append(parsed_packet[3])
    #         # print("Автоатака")
    #     # Лунное касание \ молния
    #     elif parsed_packet[3] == '\\x0c' and parsed_packet[4] == '\\xef' and parsed_packet[5] == '\\xff':
    #         result.append(parsed_packet[3])
    #         result.append(parsed_packet[4])
    #         result.append(parsed_packet[5])
    #         # print("Лунное касание | молния")
    #     # Аура Леса
    #     elif parsed_packet[2] == '\\x87' and parsed_packet[3] == '\\x01' and parsed_packet[4] == '\\x06':
    #         result.append(parsed_packet[2])
    #         result.append(parsed_packet[3])
    #         result.append(parsed_packet[4])
    #         # print("Аура Леса")
    #     # Автоатака
    #     elif parsed_packet[2] == '\\xab' and parsed_packet[3] == '\\x03':
    #         result.append(parsed_packet[2])
    #         result.append(parsed_packet[3])
    #         # print("Лунный свет | яд")
    #     else:
    #         return None 
    # else:
    #     return None
    if len(parsed_packet) > 15:
        for i in range(2, len(parsed_packet) - 9):
            if parsed_packet[i] == '\\xab' and parsed_packet[i + 1] == '\\x03' and parsed_packet[i + 2] == '\\r':
                # Блок, предшествующий урону
                result.append(parsed_packet[i])
                result.append(parsed_packet[i + 1])
                result.append(parsed_packet[i + 2])
                # Сам урон
                result.append(parsed_packet[i + 3])
                result.append(parsed_packet[i + 4])
                result.append(parsed_packet[i + 5])
                result.append(parsed_packet[i + 6])
                # Блок с айди источника
                result.append(parsed_packet[i + 7]) # -5
                result.append(parsed_packet[i + 8]) # -4
                result.append(parsed_packet[i + 9]) # -3
                # Блок с айди цели
                result.append(parsed_packet[i + 11])
                result.append(parsed_packet[i + 12])

            # print("Урон зафиксирован")
    else:
        return None
            
    # for i in range(3, len(parsed_packet) - 2):
    #     if (parsed_packet[i] == 'U') and (parsed_packet[i + 1] == '\\x00') and (parsed_packet[i + 2] == 'a'):
    #         global killed_id
    #         if f'{result[-2]}{result[-1]}' in killed_id:
    #             killed_id[f'{result[-2]}{result[-1]}'] = True
    #         else:
    #             killed_id[f'{result[-2]}{result[-1]}'] = False


    # if (len(result) > 2):
    #     print(result)
    #print("===================================")
    return result if len(result) > 5 else None

def convert(parsed_packet):
    result = []
    # print(parsed_packet)
    if len(parsed_packet) > 15:
        for i in range(len(parsed_packet) - 10):
            if f"{parsed_packet[i]}{parsed_packet[i + 1]}{parsed_packet[i + 2]}" == "\\xab\\x03\\r":
                result.append(parsed_packet[i])
                result.append(parsed_packet[i + 1])
                result.append(parsed_packet[i + 2])
                # Сам урон
                result.append(parsed_packet[i + 3])
                result.append(parsed_packet[i + 4])
                result.append(parsed_packet[i + 5])
                result.append(parsed_packet[i + 6])
                # Блок с айди источника
                result.append(parsed_packet[i + 7]) # -6
                result.append(parsed_packet[i + 8]) # -5
                result.append(parsed_packet[i + 9]) # -4
                # Блок с айди цели
                result.append(parsed_packet[i + 11]) # -3
                result.append(parsed_packet[i + 12]) # -2
                result.append(parsed_packet[i + 13]) # -1

            elif f"{parsed_packet[i]}{parsed_packet[i + 1]}{parsed_packet[i + 2]}{parsed_packet[i + 3]}{parsed_packet[i + 4]}" == "\\x00\\x00\\x00\\x1d\\x05":
                result.append(parsed_packet[i - 3])
                result.append(parsed_packet[i - 2])
                result.append(parsed_packet[i - 1])
                result.append(parsed_packet[i])
                result.append(parsed_packet[i + 1])
                result.append(parsed_packet[i + 2])
                result.append(parsed_packet[i + 3])
                result.append(parsed_packet[i + 4])
                result.append(parsed_packet[i + 5])
                result.append(parsed_packet[i + 6])
                result.append(parsed_packet[i + 7])
                result.append(parsed_packet[i + 8])
                result.append(parsed_packet[i + 9])
                result.append(parsed_packet[i + 10])


    # print(result)            
            
    if len(result) < 1:
        return None
    else: return result

