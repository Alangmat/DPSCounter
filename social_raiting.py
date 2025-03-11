from scapy.all import sniff, IP, TCP
from mailing import *
# from DataBase import *

# db = Data("warspear")

def packet_callback(packet):
    if IP in packet and TCP in packet:
        if packet[IP].src == "85.17.202.49" and packet[TCP].sport == 15102:
            payload = packet[TCP].payload
            if payload:  # Проверяем, есть ли данные в поле payload
                data = payload.load  # Получаем данные
                try:
                    data = str(data)
                    if 'A' in data and data[2] != 'A':
                        data = data[data.index('A'):]
                        # print(data)
                    msg = info_struct(data)[0]
                    if msg['mark'] == 'A':
                        if msg['type'] == '4':
                            try:
                                msg = chat_struct(data)
                                print(f'МИР: {msg["nick"]}[{msg["lvl"]}]: {msg["text"]}')
                                # db.fill("ID", msg['nick'], msg['ID'])
                            except:
                                print(f"МИР DATA: {data}")
                        elif msg['type'] == '$':
                            try:
                                msg = chat_struct(data)
                                print(f'СИСТ: {msg["nick"]}[{msg["lvl"]}]: {msg["text"]}')
                                # db.fill("ID", msg['nick'], msg['ID'])
                            except:
                                print(f"СИСТ DATA: {data}")
                        elif msg['type'] == '\\x01':
                            try:
                                msg = chat_struct(data)
                                print(f'ТОРГ: {msg["nick"]}[{msg["lvl"]}]: {msg["text"]}')
                                # db.fill("ID", msg['nick'], msg['ID'])
                            except:
                                print(f"ТОРГ DATA: {data}")
                        elif msg['type'] == '\\x03':
                            try:
                                msg = chat_struct(data)
                                print(f'ЛЧ: {msg["nick"]}[{msg["lvl"]}]: {msg["text"]}')
                                # db.fill("ID", msg['nick'], msg['ID'])
                            except:
                                print(f"ЛЧ DATA: {data}")
                        elif msg['type'] == '<':
                            try:
                                msg = chat_struct(data)
                                print(f'ГИ: {msg["nick"]}[{msg["lvl"]}]: {msg["text"]}')
                                print(msg)
                                # db.fill("ID", msg['nick'], msg['ID'])
                            except:
                                print(f"ГИ DATA: {data}")
                        elif msg['type'] == '7':
                            try:
                                #msg = drop_structure(data)
                                print(f'ДРОП: {msg["nick"]}[{msg["lvl"]}]: {msg["text"]}')
                                # db.fill("ID", msg['nick'], msg['ID'])
                            except:
                                print(f"ДРОП DATA: {data}")
                        else:
                            pass
                            # print('DATA:', data)
                except:
                    # if "b'A" in str(data):
                    #     print("DATA:", data)
                    pass


sniff(filter="ip", prn=packet_callback, store=False)



