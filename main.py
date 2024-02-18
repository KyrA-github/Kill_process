import keyboard
import psutil
import sys
import time

print("Start")
bool_ = True

def close_process(process_name):
    for process in psutil.process_iter(['pid', 'name']):
        if process.info['name'] == process_name:
            try:
                psutil.Process(process.info['pid']).terminate()
                print(f"Процесс {process_name} успешно завершен.")
            except psutil.NoSuchProcess as e:
                print(f"Ошибка при завершении процесса {process_name}: {e}")

def on_hotkey_pressed(e):
    global bool_
    file_path = 'process_name.txt'
    data = {}
    with open(file_path, 'r') as file:
        for line in file:
            key, value = line.strip().split('=')
            data[key] = value
        file.close()
    if keyboard.is_pressed(data.get('key')):
        close_process(data.get('name_process'))
        print("Процесс завершен.")
        bool_ = False
        sys.exit()

keyboard.hook(on_hotkey_pressed)



try:
    while bool_:
        time.sleep(1)
except KeyboardInterrupt:
    bool_ = False
    print("Скрипт завершен.")
