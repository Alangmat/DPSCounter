import struct
import psutil
from mailing import chat_struct

# Список строк в шестнадцатеричном формате
data = [
    b'\x1a)\x087',
]


# Функция для перевода 4-байтовой строки в число
def bytes_to_int(byte_str):
    return struct.unpack('<I', byte_str)[0]

# Преобразование каждого элемента и вывод
for byte_str in data:
    print(byte_str)
    num = bytes_to_int(byte_str)
    print(f"{byte_str} -> {num}")


# def bytes_to_int(byte_str):
#     # Проверяем, что длина строки равна 4 байтам
#     if len(byte_str) != 4:
#         raise ValueError("The byte string must be exactly 4 bytes long to unpack as a 32-bit integer.")
    
#     # Преобразуем байтовую строку в 32-битное целое число
#     return struct.unpack('<I', byte_str)[0]

# def convert_to_byte_string(byte_list):
#     # Массив, в который будем собирать байты
#     byte_array = bytearray()
    
#     for byte_str in byte_list:
#         if len(byte_str) == 1:  # Если это одиночный символ, например ','
#             byte_array.append(ord(byte_str))  # Преобразуем в байт
#         elif byte_str.startswith('\\x'):  # Если это байтовая последовательность вида \xNN
#             byte = int(byte_str[2:], 16)  # Преобразуем \xNN в число и затем в байт
#             byte_array.append(byte)
    
#     # Преобразуем массив байтов в байтовую строку
#     return bytes(byte_array)

# # Пример использования
# currents = []

# # Предположим, что packet — это массив байт, где i — индекс
# packet = [',', '\\x00', '\\x00', '\\x00']  # Пример данных
# i = 0

# currents.append(packet[i + 0])  # Добавляем элементы из packet
# currents.append(packet[i + 1])
# currents.append(packet[i + 2])
# currents.append(packet[i + 3])

# # Преобразуем в байтовую строку и затем в число
# numbers = bytes_to_int(convert_to_byte_string(currents))

# print(numbers) 


def list_to_bytes(char_list):
    # Преобразуем элементы списка в байты
    byte_list = [eval(f"b'{char}'") for char in char_list]
    
    # Соединяем все байты в один объект типа bytes
    return b''.join(byte_list)

# Пример использования
char_list = ['z', '\\n', '\\x00', '\\x00']
result = list_to_bytes(char_list)
print(result)  # Вывод: b'z\n\x00\x00'


def parse_packet(data_str):
    decoded = ""
    byte_counter = 0
    counter = 0
    data_str = str(data_str)
    
    for i in range(len(data_str) - 1):
        if counter:
            if counter == 1:
                decoded += data_str[i]
                decoded += "ц"
                counter -= 1
            else:
                decoded += data_str[i]
                counter -= 1
        elif data_str[i] == "x" and (((not data_str[i + 1].isalpha()) and data_str[i-1].isalpha() and data_str[i-2].isalpha()) or ((data_str[i + 1].isalpha()) and (data_str[i + 2].isalpha()) and data_str[i-1].isalpha() and data_str[i-2].isalpha())):
            decoded += data_str[i]
            decoded += "ц"
            byte_counter += 1
        elif data_str[i] == "\\":
            if data_str[i + 1] == "x" and data_str[i+2] != '\\' and data_str[i+3] != '\\':
                counter += 3
                decoded += data_str[i]
                byte_counter += 1
            else:
                decoded += data_str[i]
                counter += 1
                byte_counter += 1
        elif data_str[i] == "x" and data_str[i+1] != '\\' and data_str[i+2] != '\\':
            counter += 2
            decoded += data_str[i]
            byte_counter += 1
        else:
            decoded += data_str[i]
            decoded += "ц"
    
    # Разделяем строку по "ц"
    decoded = decoded.split("ц")
    
    # Убираем логику удаления данных при встрече с кавычкой
    # Просто возвращаем разобранный массив
    return decoded

print(parse_packet(str(b"U\x00[\x0b\x00\x00\xc5\xfc\xf5\x05\xc7\xce\xf6\x05\x03W\x00\xab\x03\r2'\x00\x00\xc5\xfc\xf5\x05\xc7\xce\xf6\x05\x15V\x00U\x00a\x08\x01\x00\x00\x00\xc7\xce\xf6\x05V\x00")))


data = b'\x00\xab\x00U\x00-(\x14I\x03\xef\x00K\x00'

# Разбиваем строку на массив байтов
split_marker = b'U\x00'
split_marker2 = b'I\x03'
segments = []
current_segment = bytearray()

i = 0
while i < len(data):
    # Проверяем, что нашли байты U\x00
    if data[i:i+2] == split_marker or data[i:i+2] == split_marker2:
        if current_segment:
            segments.append(bytes(current_segment))  # Добавляем текущий сегмент
        current_segment = bytearray(data[i:i+2])  # Начинаем новый сегмент с маркера
        i += 2  # Пропускаем 2 байта маркера
    else:
        current_segment.append(data[i])  # Добавляем текущий байт (целое число)
        i += 1  # Переходим к следующему байту

# Добавляем последний сегмент
if current_segment:
    segments.append(bytes(current_segment))

# Выводим результат
for idx, segment in enumerate(segments):
    print(f"Segment {idx + 1}: {segment}")


byte1 = b'\x00\xab\x00'
byte2 = b'U\x00-(\x14'
byte3 = b'U\x00\xef\x00K\x00'

# Соединяем байты
combined_bytes = byte1 + byte2 + byte3

print(combined_bytes)



tests = ['a', 'c', 'd']
for test in tests:
    if test == 'a':
        tests.insert(tests.index(test) + 1, 'b')
    print(test)
    

print(b't' == b"t")
print(parse_packet(b'\x1a)\x087\x19<\xf7\x05\x00\x00\x80?\x18\x05\x18\x05V\x02\x00\x00V\x02\x00\x00d\x00d\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xe1<R\x00\x00\x00\x1d\x05\xa0\x19<\xf7\x05'))


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

ip_ports = get_warspear_ip_port()
if ip_ports:
    for laddr, raddr, status in ip_ports:
        print(f"Локальный адрес: {laddr}, Удаленный адрес: {raddr}, Статус: {status}")
        print(laddr[0])
else:
    print("Соединений с этим процессом не найдено.")


test_Case = {
    "1": 1,
    "2": 3,
    "3": 2,
}
a = "1"
print(a in test_Case)


test_mes = b'AA\x03?\x10\xe1<R\x00\tCenapanop\x04\x00\x00\x00\x00\x00\x06\x14:\x04C\x04?\x04;\x04N\x04 \x00:\x04@\x048\x04A\x04B\x040\x04;\x04;\x04K\x04 \x000\x042\x04B\x04K\x04'

print(chat_struct(test_mes))

test_11 = [
    [1,2],
    [2,4],
    [5,4],
]

for a,b in test_11:
    print(f"{a} - {b}")