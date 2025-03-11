import psutil
import subprocess
import scapy.all as scapy
from scapy.all import get_interfaces_info
import io
import re

def get_warspear_info(process_name="warspear.exe"):
    # Найти процесс по имени и получить его PID
    warspear_pid = None
    for proc in psutil.process_iter(['pid', 'name']):
        if proc.info['name'].lower() == process_name.lower():
            warspear_pid = proc.info['pid']
            break
    
    if warspear_pid is None:
        print(f"Процесс {process_name} не найден")
        return None
    
    print(f"PID процесса {process_name}: {warspear_pid}")
    
    # Получить сетевые соединения для процесса с найденным PID
    connections = psutil.net_connections(kind='inet')
    warspear_connections = [conn for conn in connections if conn.pid == warspear_pid]
    
    if not warspear_connections:
        print(f"Нет активных сетевых соединений для процесса {process_name}")
        return None
    
    # Найти активное соединение (находим серверный порт)
    for conn in warspear_connections:
        if conn.status == 'ESTABLISHED' and conn.raddr:
            user_ip = conn.laddr.ip      # IP клиента (ваш)
            server_ip = conn.raddr.ip    # IP сервера
            server_port = conn.raddr.port # Порт сервера
            print(f"IP клиента: {user_ip}")
            print(f"IP сервера: {server_ip}")
            print(f"Порт сервера: {server_port}")
            
            # Найти интерфейс
            interface = get_interface_by_ip(user_ip)
            print(f"Интерфейс: {interface}")
            
            return {
                "user_ip": user_ip,
                "server_ip": server_ip,
                "server_port": server_port,
                "interface": interface
            }

    print(f"Нет активных соединений с сервером для процесса {process_name}")
    return None

def get_interface_by_ip(ip_address):
    interfaces = get_interfaces_info()
    for iface in interfaces:
        print(iface)
    
    return None