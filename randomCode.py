from scapy.all import sniff, IP, TCP, sendp, Raw, show_interfaces
from mailing import time_now, parse_packet, chat_struct
import struct 
import config
from convert_packets import *
from start import start
import chardet


def handle_packet_chat(packet):
    if IP in packet and TCP in packet:
        if (packet[IP].src == config.IP_SERVER and packet[IP].dst == config.IP_USER and
                packet[TCP].sport == config.PORT_SERVER):
            payload = packet[TCP].payload
            if payload:
                data = payload.load
                print(data)
                # print(data.decode('latin1', errors='ignore'))

                print(data.hex())  # Представление в виде шестнадцатеричной строки
                print([hex(b) for b in data])  # Побайтовое представление




start()
sniff(iface=config.INTERFACE_USER, prn=handle_packet_chat, filter="ip and tcp", store=0)











# import json
# import os
# import mailing

# # Путь к JSON файлу
# json_file_path = 'drops_count.json'

# # Загрузка словаря из JSON файла или создание нового, если файл отсутствует
# if os.path.exists(json_file_path):
#     with open(json_file_path, 'r') as f:
#         try:
#             drops_count = json.load(f)
#         except:
#             drops_count = {}
# else:
#     drops_count = {}



# test = b'\x01N\x11'
# test_parse = mailing.parse_packet(test)
# str_test = "".join(test_parse[2:len(test_parse)])
# print(str_test)
# if str_test in drops_count.keys():
#     drops_count[str_test] += 1
# else: drops_count[str_test] = 1

# print(drops_count)

# with open(json_file_path, 'w') as f:
#     json.dump(drops_count, f)
