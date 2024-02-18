import keyboard
import psutil
import sys
import time
print("Start")

def close_process(process_name):
    for process in psutil.process_iter(['pid', 'name']):
        if process.info['name'] == process_name:
            try:
                # Завершаем процесс
                psutil.Process(process.info['pid']).terminate()
                print(f"Процесс {process_name} успешно завершен.")
            except psutil.NoSuchProcess as e:
                print(f"Ошибка при завершении процесса {process_name}: {e}")

def on_hotkey_pressed(e):
    # Открываем файл с именем процесса
    with open("process_name.txt",'r') as file:
        process_name = file.read()
        file.close()
    # Проверяем, нажата ли горячая клавиша
    if keyboard.is_pressed('ctrl+alt+p'):
        # Закрываем процесс "cs2"
        close_process(process_name)
        # Здесь можете добавить другие действия после завершения процесса
        print("Процесс завершен.")
        sys.exit()

# Регистрируем обработчик событий
keyboard.hook(on_hotkey_pressed)

try:
    # Вечный цикл, чтобы ваш скрипт продолжал работать
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    # Обработка прерывания, если вы решите завершить скрипт
    print("Скрипт завершен.")
