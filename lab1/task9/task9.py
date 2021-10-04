import random
import main


def print_menu(length_of_word: str):
    print('Добро пожаловать в игру "Отгадай слово"!\n'
          'Количество букв в слове: ' + length_of_word + '\n'
          '\nВам дается 5 попыток для того, чтобы уточнить у программы есть ли предполагаемая буква в загаданном слове'
          '\nПрограмма умеет отвечать только "Да" и "Нет"'
          '\n(Для выхода нажмите Enter, не вводя своей версии.)\n'
          '\nПосле 5 попыток, попробуйте отгадать загаданное слово.')


def check_symbol(normal_word, input_symbol):
    if input_symbol in normal_word:
        print('\nДа')
    print('\nНет')


def check_word(normal_word, input_word):
    if normal_word == input_word:
        return True
    return False


def start_task9():
    word_file = 'russian_words.txt'
    word_list = open('lab1/' + word_file).read().splitlines()

    while True:
        random_word = random.choice(word_list)
        length_of_word = len(random_word)

        main.clear_console()
        print_menu(str(length_of_word))

        for i in range(1, 6):
            print('Попытка #' + str(i) +
                  '\nВведите вашу букву: ')
            attempt_choice = input()

            if attempt_choice == '':
                return main.start_main_menu()

            check_symbol(random_word, attempt_choice)

        print('\nА теперь предлагается отгадать исходное слово: ')
        input_word = str(input())
        if check_word(random_word, input_word):
            print('\nПоздравляем, вы отгадали исходное слово')
        else:
            print('\nВы не отгадали исходное слово. *ПОТРАЧЕНО*.')

        print('\nХотите попробовать снова?'
              '\nчто-угодно - да'
              '\n0 - выход в главное меню')
        choice = str(input())
        if choice == '0':
            return main.start_main_menu()
        else:
            continue
