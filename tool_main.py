# student_name: Abilash M P
# roll_number: 727823TUCY001
# project_name: Network Port Scanner
# date: 2026-03-29

import socket

target = input("Enter Target IP: ")

print(f"\nScanning {target}...\n")

for port in range(1, 1001):   # changed to 1000
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket.setdefaulttimeout(1)

    result = s.connect_ex((target, port))

    if result == 0:
        print(f"Port {port} is OPEN")

    s.close()