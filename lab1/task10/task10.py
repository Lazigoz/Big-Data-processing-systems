import main


def print_menu(points: str):
    print('Добро пожаловать в игру "Генератор персонажей"!'
          '\nУ вас есть ' + points + ' очков навыка.'
          '\nИх можно распределить на:'
          '\n1. Сила'
          '\n2. Ловкость'
          '\n3. Мудрость'
          '\n4. Здоровье'
          '\n(Для выхода нажмите Enter, не вводя своей версии.)\n')


def print_skills(skills, points):
    print('Свободное количество очков навыка: ' + str(points) +
          '\nВаше текущее распределение навыков:' +
          '\n{'
          '\n\tСила = ' + str(skills['1']) +
          '\n\tЛовкость = ' + str(skills['2']) +
          '\n\tМудрость = ' + str(skills['3']) +
          '\n\tЗдоровье = ' + str(skills['4']) +
          '\n}'
          )


def start_task10():
    main.clear_console()

    points = 30
    skills = {
        '1': 0,
        '2': 0,
        '3': 0,
        '4': 0,
    }
    print_menu(str(points))

    while True:
        print_skills(skills, points)
        if points < 1:
            print('\nУ вас закончились свободные очки навыка. Жмите Enter чтобы выйти')

        input_choice = input('\nУкажите какой из навыков изменить: ')
        if input_choice == '':
            return main.start_main_menu()

        input_action = input('\nВыберите действие с навыками (+) - добавить. (-) - удалить: ')
        input_points = int(input('\nВведите количество очков навыка для использования: '))

        if input_action == '+':
            if points - input_points >= 0:
                points -= input_points
                new_skill = skills[input_choice] + input_points
                skills[input_choice] = new_skill
            else:
                print('\nУ вас нет такого количества очков навыка')
        elif input_action == '-':
            skill = skills[input_choice]
            if skill - input_points >= 0:
                points += input_points
                new_skill = skill - input_points
                skills[input_choice] = new_skill
            else:
                print('\nУ выбранного навыка нет достаточного количества использованных очков для удаления.')
