import os
import lab1.lab1 as lab1


def clear_console():
    os.system('cls' if os.name in ('nt', 'dos') else 'clear')


def print_menu():
    print('Наберите выбрав лабораторную работу: \n\n'
          '1 - лабораторная работа #1\n'
          '0 - для выхода из программы\n')


def print_wrong_input_choice():
    print('\n-- Такого варианта выбора не существует. Попробуйте снова --\n')


def input_menu_choice():
    try:
        input_choice = int(input())
    except ValueError:
        return 'Повторите ввод, то что вы ввели - не число\n\n'
    else:
        return int(input_choice)


def start_main_menu():
    while True:
        clear_console()
        print_menu()
        menu_choice = input_menu_choice()

        if menu_choice == 1:
            return lab1.start_lab1()
        if menu_choice == 0:
            raise SystemExit(1)
        else:
            print_wrong_input_choice()


if __name__ == '__main__':
    start_main_menu()
