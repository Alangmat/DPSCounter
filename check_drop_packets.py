from scapy.all import sniff, IP, TCP, sendp, Raw, show_interfaces
from mailing import time_now, parse_packet, chat_struct
import struct 
import config
from convert_packets import *
from start import start
# from actions_db import *
from items import drops

import json
import os

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

prev_byte = None


def write_file(packet):
    test_parse = parse_packet(packet)
    str_test = "".join(test_parse[2:len(test_parse)])
    # print(str_test)
    if str_test in drops_count.keys():
        drops_count[str_test] += 1
    else: drops_count[str_test] = 1
    # print(drops_count)

    with open(json_file_path, 'w') as f:
        json.dump(drops_count, f)



def handle_packet_chat(packet):
    if IP in packet and TCP in packet:
        if (packet[IP].src == config.IP_SERVER and packet[IP].dst == config.IP_USER and
                packet[TCP].sport == config.PORT_SERVER):
            payload = packet[TCP].payload
            if payload:
                data = payload.load
                triger_drop = b'\x03\x02\x01\x00$'
                if triger_drop in data:
                    print(data)
                # print(data)
                # drop_marker = b'Alangmator'
                drop_marker = b'$\x05\x01'
                double_drop_marker = b'$\t\x02'
                triple_drop_marker = b'$\r\x03'
                split_marker = b'\x02d'
                test_marker = b'\x00\x00\x04'

                current_drop = b''
        
                i = 0
                while i < len(data) - 5:
                    if data[i:i+3] == drop_marker:
                        current_drop = data[i+3:i+5]
                        print(current_drop)
                        write_file(current_drop)
                        print(drops_count)
                        # print(data)
                        break
                    elif data[i:i+3] == double_drop_marker and i < len(data) - 9:
                        f_drop = data[i+3:i+5]
                        s_drop = data[i+7:i+9]
                        print(f_drop, s_drop)
                        write_file(f_drop)
                        write_file(s_drop)
                        # print(drops_count)
                        break
                    elif data[i:i+3] == triple_drop_marker and i < len(data) - 13:
                        f_drop = data[i+3:i+5]
                        s_drop = data[i+7:i+9]
                        t_drop = data[i+11:i+13]
                        print(f_drop, s_drop, t_drop)
                        write_file(f_drop)
                        write_file(s_drop)
                        write_file(t_drop)
                        # print(drops_count)
                        break

                        
                    i += 1
                
                if current_drop in drops:
                    print(drops[current_drop])



start()
sniff(iface=config.INTERFACE_USER, prn=handle_packet_chat, filter="ip and tcp", store=0)