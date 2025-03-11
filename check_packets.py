from scapy.all import sniff, IP, TCP, sendp, Raw, show_interfaces
from mailing import time_now, parse_packet, chat_struct
import struct 
import config
from convert_packets import *
from start import start
from actions_db import *

prev_byte = None

def handle_packet_chat(packet):
    if IP in packet and TCP in packet:
        if (packet[IP].src == config.IP_SERVER and packet[IP].dst == config.IP_USER and
                packet[TCP].sport == config.PORT_SERVER):
            payload = packet[TCP].payload
            if payload:
                # try:
                global prev_byte
                data = payload.load
                # print(data)
                parsed_packet = parse_packet(data)
                # print(parsed_packet)
                segments = []
                i = 0
                current_segment = None  # Текущий сегмент пока пустой

                if prev_byte is not None:
                    # Если prev_byte начинается с \xab и следующий пакет начинается с \xab и \r
                    if prev_byte.startswith(b'\xab') and data[:2] == b'\xab\r':
                        needed_bytes = 14 - len(prev_byte)
                        if len(data) >= needed_bytes:
                            prev_byte += data[:needed_bytes]
                            segments.append(bytes(prev_byte))
                            prev_byte = None
                            data = data[needed_bytes:]  # Удаляем использованные байты

                    # Если prev_byte начинается с \xab\x03 и следующий пакет начинается с \r
                    elif prev_byte.startswith(b'\xab\x03') and data[:1] == b'\r':
                        needed_bytes = 14 - len(prev_byte)
                        if len(data) >= needed_bytes:
                            prev_byte += data[:needed_bytes]
                            segments.append(bytes(prev_byte))
                            prev_byte = None
                            data = data[needed_bytes:]  # Удаляем использованные байты

                    # Если prev_byte начинается с \xab\x03\r
                    elif prev_byte.startswith(b'\xab\x03\r'):
                        needed_bytes = 14 - len(prev_byte)
                        if len(data) >= needed_bytes:
                            prev_byte += data[:needed_bytes]
                            segments.append(bytes(prev_byte))
                            prev_byte = None
                            data = data[needed_bytes:]  # Удаляем использованные байты

                # Если остались неполные данные в prev_byte
                if prev_byte and len(prev_byte) == 14:
                    segments.append(bytes(prev_byte))
                    prev_byte = None

                while i < len(data):
                    if data[i:i+1] == b'\xab':
                        # Если находим \xab, начинаем новый сегмент
                        if current_segment:  # Добавляем предыдущий сегмент, если он был
                            segments.append(bytes(current_segment))
                        current_segment = bytearray(data[i:i+1])  # Начинаем новый сегмент с \xab
                    elif current_segment is not None:
                        # Добавляем байты только если сегмент уже начался с \xab
                        current_segment.append(data[i])
                        # Если длина сегмента превышает 14 байт, завершаем его
                        if len(current_segment) >= 14:
                            segments.append(bytes(current_segment))
                            current_segment = None 
                    i += 1

                # Добавляем последний сегмент, если он начинается с \xab
                if current_segment:
                    segments.append(bytes(current_segment))

                # print(segments)
                if len(segments) > 0:
                    for segment in segments:
                        if len(segment) == 1:
                            print(segment)
                            prev_byte = segment
                        elif b'\xab\x03' in segment:
                            print(segment)
                            if len(segment) < 14:
                                prev_byte = segment
                    print("--")

                # with open('logs.txt', 'w') as log_file:
                #     for segment in segments:
                #         print(segment)
                #         log_file.write(repr(segment) + '\n')
                #         log_file.flush()
                # except:
                #     print("хз")


start()
sniff(iface=config.INTERFACE_USER, prn=handle_packet_chat, filter="ip and tcp", store=0)