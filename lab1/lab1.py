import main
from .task8 import task8


def task9():
    pass
    # return lab1.start_task9()


def task10():
    pass
    # return lab1.start_task10()


def print_menu():
    print('Наберите выбрав задачу: \n\n'
          '1 - задача #8\n'
          '2 - задача #9\n'
          '3 - задача #10\n'
          '0 - для выхода в главное меню\n')


def start_lab1():
    main.clear_console()
    while True:
        print_menu()
        menu_choice = main.input_menu_choice()

        if menu_choice == 1:
            return task8.start_task8()
        if menu_choice == 2:
            return task9()
        if menu_choice == 3:
            return task10()
        if menu_choice == 0:
            return main.start_main_menu()
        else:
            main.print_wrong_input_choice()

