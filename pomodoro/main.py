import plyer
from colorama import Fore, Style, init
init(autoreset=True)

def run_app():
    work = input(Fore.YELLOW + "На сколько по времени погружаемся в роботу: ")
    chill = input(Fore.YELLOW + 'Сколько отдыхаем: ')
    name = 'user'

    while True:
    # сделаем так чтобы еще все стиралось до этих смсок (clear) возможно еще отцентровать но это так 50/50
        print(Fore.CYAN + "=" * 45)
        print(Fore.BLUE + f"⏱  Время потока продуктивности: {work} мин  ⏱")
        print(Fore.GREEN + f"       🌿  Время отдыха: {chill} мин  🌿")
        print(Fore.CYAN + "=" * 45)
        print()
        print(Fore.MAGENTA + f"🔥 Добро пожаловать, {name}, в сессию продуктивности 🔥") # будем запрашивать имя и записывать потом куда-то и брать его от туда
        break
