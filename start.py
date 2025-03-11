import psutil
import config
import sys
import io
import re
from scapy.all import sniff, IP, TCP, sendp, Raw, show_interfaces

def get_warspear_ip_port():
    # Найти процесс по имени
    process_name = "warspear.exe"
    warspear_pid = None
    for proc in psutil.process_iter(['pid', 'name']):
        if proc.info['name'] == process_name:
            warspear_pid = proc.info['pid']
            break

    if warspear_pid is None:
        print(f"Процесс {process_name} не найден.")
        return None

    # Получить сетевые соединения, связанные с PID
    connections = psutil.net_connections(kind='inet')
    ip_ports = []
    for conn in connections:
        if conn.pid == warspear_pid:
            ip_ports.append((conn.laddr, conn.raddr, conn.status))

    return ip_ports

def get_interface(ipv4_address):
    # Создаем объект StringIO для перехвата вывода
    captured_output = io.StringIO()
    original_stdout = sys.stdout
    sys.stdout = captured_output

    try:
        # Call your function whose output we are intercepting
        show_interfaces()
    finally:
        # Restore the original stdout
        sys.stdout = original_stdout

    # Get the captured output
    output = captured_output.getvalue()

    # Split the output into lines
    lines = output.strip().split('\n')

    if not lines:
        print("Function output is empty.")
        return None

    # Extract the header and determine column positions
    header = lines[0]
    # Use regex to find the start positions of each column
    positions = [m.start() for m in re.finditer(r'\S+', header)]
    column_names = re.findall(r'\S+', header)

    # Function to extract fields based on positions
    def extract_fields(line, positions, count):
        fields = []
        for i in range(count):
            start = positions[i]
            end = positions[i + 1] if i + 1 < count else None
            field = line[start:end].strip() if end else line[start:].strip()
            fields.append(field)
        return fields

    data = []
    for line in lines[1:]:
        if not line.strip():
            continue
        # Check if the line starts with spaces, indicating additional information (e.g., extra IPv6)
        if line.startswith(' '):
            # This is additional information; append it to the last entry
            if data:
                last_entry = data[-1]
                additional_ipv6 = line.strip()
                if 'IPv6' in last_entry and last_entry['IPv6']:
                    last_entry['IPv6'] += f", {additional_ipv6}"
                else:
                    last_entry['IPv6'] = additional_ipv6
            continue

        # Extract fields based on positions
        fields = extract_fields(line, positions, len(column_names))
        # If there are fewer fields than columns, pad with empty strings
        if len(fields) < len(column_names):
            fields += [''] * (len(column_names) - len(fields))
        entry = dict(zip(column_names, fields))
        data.append(entry)

    # Search for the entry with the specified IPv4 address
    for entry in data:
        if entry.get('IPv4') == ipv4_address:
            return entry.get('Name')

    return None

def start():
    ip_ports = get_warspear_ip_port()
    if ip_ports:
        for laddr, raddr, status in ip_ports:
            print(f"Локальный адрес: {laddr}, Удаленный адрес: {raddr}, Статус: {status}")
            print(laddr[0])
            config.IP_USER = laddr[0]
            config.INTERFACE_USER = get_interface(config.IP_USER)
            break
    else:
        print("Соединений с этим процессом не найдено.")


