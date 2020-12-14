import re
import time
from colorama import Fore, Style

print(Fore.LIGHTMAGENTA_EX+"!ВНИМАНИЕ! Файл ОБЯЗАТЕЛЬНО должен быть в кодировке ANSI!")
time.sleep(2)


def choice_out(parsed):
    print(Fore.LIGHTMAGENTA_EX + parsed)


def choice_infile(parsed, fname):
    name = input(Fore.GREEN+"Введите название новго файла (либо оставьте пустым) > "+Fore.CYAN)
    if not name:
        # name = fname.sub("."+fname.split('.')[-1])+"_parsed."+fname.split('.')[-1]
        name = "_parsed.".join(fname.split("."))

    with open(name, 'w') as f:
        f.write(parsed)
        f.close()


try:
    fname = input(Fore.GREEN+"Введите имя файла > "+Fore.CYAN)
    with open(fname, 'r') as f:
        text = f.read()
        f.close()

    pattern = input(Fore.GREEN+"Введите паттерн\n"+Fore.CYAN)
    replace = input(Fore.GREEN+"Введите слово/символ для замены > "+Fore.CYAN)

    parsed = re.sub(rf"{pattern}", replace, text)  # <td>[a-f0-9]{4}</td><td>[0-9]{4,5}</td>

    print(Fore.GREEN+"Вы хотите вывести везультат или сохранить его в файл?")

    while True:
        choice = input(Fore.GREEN + "(0 - вывести, 1 - в файл) > " + Fore.CYAN)

        if choice == '0':
            choice_out(parsed)
            break
        elif choice == '1':
            choice_infile(parsed, fname)
            break
        else:
            print(Fore.RED+"Вы выбрали неверный вариант!")

except FileNotFoundError:
    print(Fore.RED)
    print("Ошибка программы!")
    print(" ‣ Неверное имя файла")

except UnicodeDecodeError:
    print(Fore.RED)
    print("Ошибка программы!")
    print(" ‣ Неверная кодировка файла")

print(Style.RESET_ALL)
