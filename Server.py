import socket
import os

UDP_IP = "0.0.0.0"
UDP_PORT = 7777
SCRIPT_PATH = "C:\\Users\\Имя\\Saved Games\\DCS\\Scripts\\control.lua"

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((UDP_IP, UDP_PORT))

print(f"UDP сервер запущен на {UDP_IP}:{UDP_PORT}")

while True:
    data, addr = sock.recvfrom(1024)
    command = data.decode("utf-8").strip()
    print(f"Получена команда: {command}")

    if not os.path.exists(SCRIPT_PATH):
        print(f"Ошибка: Файл {SCRIPT_PATH} не найден!")
        continue

    try:
        with open(SCRIPT_PATH, "r") as f:
            content = f.read()

        if f'ProcessCommand("{command}")' not in content:
            with open(SCRIPT_PATH, "a") as f:
                f.write(f'ProcessCommand("{command}")\n')
            print(f"Команда записана: {command}")
        else:
            print(f"Команда {command} уже есть в файле")

    except Exception as e:
        print(f"Ошибка записи в LUA: {e}")

    