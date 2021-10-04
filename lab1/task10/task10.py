import random
import math
import main


def print_menu(anagram_word: str, user_score: str):
    print('Добро пожаловать в игру "Анаграммы"!\n'
          'Надо переставить буквы так, чтобы получилось осмысленное слово.'
          '\nВаше количество баллов: ' + user_score + '\n' +
          '\n1 - использование подсказки'
          '\n(Для выхода нажмите Enter, не вводя своей версии.)\n'
          '\nВот анаграмма: ' + anagram_word + '\n' +
          '\nПопробуйте отгадать исходное слово: ')


def print_second_chance():
    print('\n*Если хотите воспользоваться подсказкой введите цифру - 1*'
          '\nВы не отгадали исходное слово, попробуйте снова: ')


def print_victory_chance(score: str):
    print('\nПоздравляем, вы отгадали исходное слово, вам начислено ' + score + ' - количество баллов')


def show_hint(normal_word):
    hint_length_word = math.ceil(len(normal_word) - len(normal_word) / 2)
    hint_word = normal_word[:hint_length_word]
    print('\nВы воспользовались подсказкой, теперь вам будет начислено меньше баллов за отгадку.'
          '\nПодсказка: ' + hint_word +
          '\nПопробуйте отгадать исходное слово: ')


def check_word(normal_word, input_word):
    if normal_word == input_word:
        return True
    return False


def to_anagram_word(normal_word):
    anagram_word = list(normal_word)
    random.shuffle(anagram_word)

    return ''.join(anagram_word)


def start_task10():
    word_file = 'russian_words.txt'
    word_list = open('lab1/' + word_file).read().splitlines()

    user_score = 0

    while True:
        hint_used = False

        random_word = random.choice(word_list)
        anagram_word = to_anagram_word(random_word)

        main.clear_console()
        print_menu(anagram_word, str(user_score))

        while True:
            attempt_choice = str(input())

            if attempt_choice == '1':
                show_hint(random_word)
                hint_used = True
                continue
            if attempt_choice == '':
                return main.start_main_menu()

            if check_word(random_word, attempt_choice):
                if not hint_used:
                    user_score += 3
                    print_victory_chance('3')
                    break
                user_score += 1
                print_victory_chance('1')
                break
            else:
                print_second_chance()

        print('\nХотите попробовать снова?'
              '\nчто-угодно - да'
              '\n0 - выход в главное меню')
        choice = str(input())
        if choice == '0':
            return main.start_main_menu()
        else:
            continue
