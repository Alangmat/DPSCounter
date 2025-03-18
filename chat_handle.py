from scapy.all import sniff, IP, TCP, sendp, Raw, show_interfaces
from mailing import time_now, parse_packet, chat_struct
import struct 
import config
from convert_packets import *
from start import start
from actions_db import *

def hasSpecialSymbols(str_):
    return bool(
        set('.,:;!_*-+()/#¤%&') & set(str_)
    )

def handle_packet_chat(packet):
    if IP in packet and TCP in packet:
        if (packet[IP].src == config.IP_SERVER and packet[IP].dst == config.IP_USER and
                packet[TCP].sport == config.PORT_SERVER):
            payload = packet[TCP].payload
            if payload:
                try:

                    data = payload.load
                    # print(data)
                    # if (len(data) > 6):
                        # print(len(data))

                    parsed_packet = parse_packet(data)
                    
                    # ЭТО ДЕЛАЛ ЧТОБ ТОЛЬКО ОТ АЛАНГМАТОРА ПРИХОДИЛИ ПАКЕТЫ
                    # if b'Alangmator' in data:
                    #     # print(data)
                    #     sequence = b'\x00\x00\x00\x00\x00\x04'
                    #     start_index = data.find(sequence)

                    #     if start_index != -1:
                    #         # Извлекаем два байта после последовательности
                    #         result = data[start_index + len(sequence):start_index + len(sequence) + 2]
                    #         result_parsed = parse_packet(result)[2:4]
                    #         str = "".join(result_parsed)
                    #         print([str])
                    #     else:
                    #         print("Последовательность не найдена")

                    if len(parsed_packet) > 3:
                        if (parsed_packet[2] == 'A'):
                            message = chat_struct(data)
                    
                            if message is not None:
                                if not hasSpecialSymbols(message['nick']):
                                    print(f"{message['ID']} - {message['nick']}: {message['text']}")
                                    create_update_hero(message['ID'], message['nick'])
                except:
                    print("хз")
start()
sniff(iface=config.INTERFACE_USER, prn=handle_packet_chat, filter="ip and tcp", store=0)