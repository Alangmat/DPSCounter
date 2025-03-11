import sys
import io
import re
from scapy.all import sniff, IP, TCP, sendp, Raw, show_interfaces


def intercept_and_process(ipv4_address):
    # Create a StringIO object to capture the output
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

# Пример использования
ipv4 = '192.168.0.101'
name = intercept_and_process(ipv4)
show_interfaces()
if name:
    print(f"Имя интерфейса с IPv4 {ipv4}: {name}")
else:
    print(f"Интерфейс с IPv4 {ipv4} не найден.")
