import os
import time

directory = r'.'

for root, dirs, files in os.walk(directory):
    for file in files:
        parent_dir = os.path.dirname(fr'{directory}\{file}')
        filepath = os.path.join(fr'{directory}\{file}')
        filetime = os.path.getmtime(fr'{directory}\{file}')
        formatted_time = time.strftime("%d.%m.%Y %H:%M", time.localtime(filetime))
        filesize = os.path.getsize(fr'{directory}\{file}')
        print(f'Обнаружен файл: {file}, Путь: {filepath}, '
              f'Размер: {filesize} байт, Время изменения: {formatted_time}, '
              f'Родительская директория: {parent_dir}')
