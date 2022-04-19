
"""
5. Выполнить пинг веб-ресурсов yandex.ru, youtube.com и преобразовать результаты из
байтовового в строковый тип на кириллице.
"""

import platform
import subprocess
import chardet

WEBS = ['yandex.ru', 'youtube.com']
PARAM = '-n' if platform.system().lower() == 'windows' else '-c'

for web in WEBS:
    args = ['ping', PARAM, '4', web]
    subproc_ping = subprocess.Popen(args, stdout=subprocess.PIPE)
    for line in subproc_ping.stdout:
        result = chardet.detect(line)
        line = line.decode(result['encoding']).encode('utf-8')
        print(line.decode('utf-8'))
