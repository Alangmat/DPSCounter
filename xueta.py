from scapy.all import sniff, IP, TCP
from mailing import *
from DataBase import *
import datetime

db = Data("warspear")
db.create_table("storage",
                "nickname", "TEXT",
                "DepMoney", "INT",
                "NeedMoney", "INT",
                "StaminaCount", "INT",
                "TPCount","INT",
                "ResCount", "INT",
                "RemCount", "INT",
                "BillsCount", "INT",
                "GladCount", "INT",
                "HealCount", "INT",
                "PetCount","INT",
                "LastOperation", "TEXT")


db.create_table("ID",
                "nickname", "TEXT",
                "id", "TEXT")


columns = {"[Эликсир выносливости искателя]": "StaminaCount",
               "[Свиток телепортации]": "TPCount",
               "[Великий эликсир гладиатора]": "GladCount",
               "[Свиток ремонта]": "RemCount",
               "[Великое зелье жизни]": "HealCount",
               "[Свиток жизни]": "ResCount",
               "[Билет на арену]": "BillsCount",
               #"[Призыв Чумного знахаря]": "PetCount",
                "DepMoney": "DepMoney"}

cost = {"[Эликсир выносливости искателя]": 2000,
               "[Свиток телепортации]": 200,
               "[Великий эликсир гладиатора]": 2000,
               "[Свиток ремонта]": 200,
               "[Великое зелье жизни]": 100,
               "[Свиток жизни]": 1000,
               "[Билет на арену]": 40,
               #"[Призыв Чумного знахаря]": 2000
                }


def storage_counter(item_name, msg):
    db.fill("storage", msg['nick'], 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "0")
    column_name = columns[item_name]
    if not db.ReturnValue("storage","LastOperation",parameter=f'WHERE nickname = "{msg["nick"]}"') == str(time_now()):
        if column_name == "DepMoney":
            value = db.ReturnValue("storage", column_name, parameter=f"WHERE nickname = '{msg['nick']}'")
            db.UpdateValue("storage", column_name, value + int(msg["amount"]), parameter=f'WHERE nickname = "{msg["nick"]}"')
            db.UpdateValue("storage", "LastOperation", str(time_now()), parameter=f'WHERE nickname = "{msg["nick"]}"')
        elif msg["item_name"] == item_name:
            value = db.ReturnValue("storage", column_name, parameter=f"WHERE nickname = '{msg['nick']}'")
            db.UpdateValue("storage", column_name, value + msg["count"], parameter=f'WHERE nickname = "{msg["nick"]}"')
            value = db.ReturnValue("storage", "NeedMoney", parameter=f"WHERE nickname = '{msg['nick']}'")
            db.UpdateValue("storage", "NeedMoney", value + msg["count"]*cost[item_name], parameter=f'WHERE nickname = "{msg["nick"]}"')
            db.UpdateValue("storage", "LastOperation", str(time_now()), parameter=f'WHERE nickname = "{msg["nick"]}"')


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

                    if msg['mark'] == 'A' and msg["type"] not in ['4','$','\\x01','\\x03','<','7']:
                        if msg["flag"] == "[":
                            try:
                                msg = item_struct(str(data))
                                print(f'WITH_ITEM[{time_now()}]: {msg["nick"]}[{msg["lvl"]}]: {msg["item_name"]} - {item_struct(data)["count"]}')
                                storage_counter(msg['item_name'],msg=msg)
                                db.fill("ID", msg['nick'], msg['ID'])
                            except:
                                print(f'WITH_ITEM DATA: {data}')
                        elif msg["flag"] == "X":
                            try:
                                msg = item_struct(str(data))
                                print(f'DEP_ITEM[{time_now()}]: {msg["nick"]}[{msg["lvl"]}]: {msg["item_name"]} - {msg["count"]}')
                                db.fill("ID", msg['nick'], msg['ID'])
                            except:
                                print(f'DEP_ITEM DATA: {data}')
                        elif msg["flag"] == "Y":
                            try:
                                msg = money_struct(str(data))
                                print(f'DEP_MONEY[{time_now()}]: {msg["nick"]}[{msg["lvl"]}]: {msg["amount"]}')
                                storage_counter("DepMoney", msg=msg)
                                db.fill("ID", msg['nick'], msg['ID'])
                            except:
                                print(f'DEP_MONEY DATA: {data}')
                        elif msg["flag"] == "\\\\":
                            try:
                                msg = money_struct(str(data))
                                print(f'WITH_MONEY[{time_now()}]: {msg["nick"]}[{msg["lvl"]}]: {msg["amount"]}')
                                db.fill("ID", msg['nick'], msg['ID'])
                            except:
                                print(f'WITH_MONEY DATA: {data}')
                        # else:
                        #     print('DATA:', data)
                except:
                    # if "b'A" in str(data):
                    #     print("DATA:", data)
                    pass


sniff(filter="ip", prn=packet_callback, store=False)