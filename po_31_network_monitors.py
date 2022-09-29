import os

hosts = ["127.0.0.1", "ya.ru", "192.168.22.2", "orsk"]

os.system("CHCP 65001")

for host in hosts:
    command = f"ping {host}"
    os.system(command)
    # 1. Как получить отклик от команды? Подсказка: os.popen
    # 2. Как из текста отклика понять, хороший хост или плохой?